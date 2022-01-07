#include "pyobjc.h"

NS_ASSUME_NONNULL_BEGIN

@implementation OC_PythonNumber

+ (instancetype _Nullable)numberWithPythonObject:(PyObject*)v
{
    if (PyLong_Check(v)) {
        unsigned long long lv = PyLong_AsUnsignedLongLong(v);
        if (PyErr_Occurred()) {
            PyErr_Clear();
        } else if (lv >= 1ULL << 63) {
            /* Workaround for round-trip problems... */
#ifdef __clang__
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wincompatible-pointer-types"
#endif
            /*
             * This should return an autoreleased value, but that causes
             * a crash in pyobjc-framework-Cocoa/test_regr.py
             *
             * XXX: Further investigate (in particular
             *
             *      This is caused by callers of this method assuming
             *      that the result is an instance of an OC_ class that
             *      will unregister itself in dealloc. That's not true
             *      of instances like this.
             *
             *      I'm leaving the code like this for now and need
             *      to perform more testing before fixing this.
             */
            return [[NSNumber alloc] initWithUnsignedLongLong:lv];
#ifdef __clang__
#pragma clang diagnostic pop
#endif
        }
    }

    return [[[self alloc] initWithPythonObject:v] autorelease];
}

- (instancetype _Nullable)initWithPythonObject:(PyObject*)v
{
    self = [super init];
    if (unlikely(self == nil))
        return nil;

    SET_FIELD_INCREF(value, v);
    return self;
}

- (PyObject*)__pyobjc_PythonObject__
{
    Py_INCREF(value);
    return value;
}

- (PyObject*)__pyobjc_PythonTransient__:(int*)cookie
{
    *cookie = 0;
    Py_INCREF(value);
    return value;
}

+ (BOOL)supportsSecureCoding
{
    return NO;
}

- (oneway void)release
{
    /* See comment in OC_PythonUnicode */
    if (unlikely(!Py_IsInitialized())) {
        [super release];
        return;
    }

    PyObjC_BEGIN_WITH_GIL

        @try {
            [super release];
        } @catch (NSObject* exc) {
            PyObjC_LEAVE_GIL;
            @throw;
        }

    PyObjC_END_WITH_GIL
}

- (void)dealloc
{
    if (unlikely(!Py_IsInitialized())) {
        [super dealloc];
        return;
    }

    PyObjC_BEGIN_WITH_GIL
        PyObjC_UnregisterObjCProxy(value, self);
        Py_CLEAR(value);

    PyObjC_END_WITH_GIL

    [super dealloc];
}

- (const char*)objCType
{
    PyObjC_BEGIN_WITH_GIL
        if (PyBool_Check(value)) {
            PyObjC_GIL_RETURN(@encode(BOOL));
        } else if (PyFloat_Check(value)) {
            PyObjC_GIL_RETURN(@encode(double));
        } else if (PyLong_Check(value)) {
            (void)PyLong_AsLongLong(value);
            if (!PyErr_Occurred()) {
                PyObjC_GIL_RETURN(@encode(long long));
            } else {
                PyErr_Clear();
                (void)PyLong_AsUnsignedLongLong(value);
                if (!PyErr_Occurred()) {
                    PyObjC_GIL_RETURN(@encode(unsigned long long));
                }
                PyErr_Clear();

                /* Wrap on overflow */
                PyObjC_GIL_RETURN(@encode(long long));
            }
        }
    PyObjC_END_WITH_GIL
    [NSException raise:NSInvalidArgumentException
                format:@"Cannot determine objective-C type of this number"];
    return @encode(char);
}

- (void)getValue:(void*)buffer
{
    const char* encoded = [self objCType];
    int         r;
    PyObjC_BEGIN_WITH_GIL
        r = depythonify_c_value(encoded, value, buffer);
        if (r == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
}

- (void)getValue:(void*)buffer forType:(const char*)type
{
    int r;
    PyObjC_BEGIN_WITH_GIL
        r = depythonify_c_value(type, value, buffer);
        if (r == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
}

- (BOOL)boolValue
{
    return (BOOL)PyObject_IsTrue(value);
}

- (char)charValue
{
    return (char)[self longLongValue];
}

- (NSDecimal)decimalValue
{
    NSDecimal result;
    int       r;

    PyObjC_BEGIN_WITH_GIL
        r = PyObjC_number_to_decimal(value, &result);

        if (r == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }

    PyObjC_END_WITH_GIL

    return result;
}

- (double)doubleValue
{
    PyObjC_BEGIN_WITH_GIL
        if (PyFloat_Check(value)) {
            PyObjC_GIL_RETURN(PyFloat_AsDouble(value));
        }
    PyObjC_END_WITH_GIL
    return (double)[self longLongValue];
}

- (float)floatValue
{
    return (float)[self doubleValue];
}

- (NSInteger)integerValue
{
    return (NSInteger)[self longLongValue];
}

- (int)intValue
{
    return (int)[self longLongValue];
}

- (long)longValue
{
    return (long)[self longLongValue];
}

- (short)shortValue
{
    return (short)[self longLongValue];
}

- (unsigned char)unsignedCharValue
{
    return (unsigned char)[self unsignedLongLongValue];
}

- (NSUInteger)unsignedIntegerValue
{
    return (NSUInteger)[self unsignedLongLongValue];
}

- (unsigned int)unsignedIntValue
{
    return (unsigned int)[self unsignedLongLongValue];
}

- (unsigned long)unsignedLongValue
{
    return (unsigned long)[self unsignedLongLongValue];
}

- (unsigned short)unsignedShortValue
{
    return (unsigned short)[self unsignedLongLongValue];
}

- (long long)longLongValue
{
    long long result;

    PyObjC_BEGIN_WITH_GIL
        if (PyFloat_Check(value)) {
            result = (long long)PyFloat_AsDouble(value);
            PyObjC_GIL_RETURN(result);
        } else if (PyLong_Check(value)) {
            result = PyLong_AsUnsignedLongLongMask(value);
            PyObjC_GIL_RETURN(result);
        }
    PyObjC_END_WITH_GIL

    [NSException raise:NSInvalidArgumentException
                format:@"Cannot determine objective-C type of this number"];
    return -1;
}

- (unsigned long long)unsignedLongLongValue
{
    unsigned long long result;

    PyObjC_BEGIN_WITH_GIL
        if (PyLong_Check(value)) {
            result = PyLong_AsUnsignedLongLongMask(value);
            PyObjC_GIL_RETURN(result);
        } else if (PyFloat_Check(value)) {
            double temp = PyFloat_AsDouble(value);
            if (temp < 0) {
                /* Conversion of negative numbers to
                 * unsigned long long is undefined behaviour,
                 * the code below seems to get the behaviour
                 * we'd like: casting to unsigned long long
                 * behaves simular to casting a signed integer
                 * to undefined.
                 */
                long long t = (long long)temp;
                result      = (unsigned long long)t;
            } else {
                result = (unsigned long long)temp;
            }
            PyObjC_GIL_RETURN(result);
        }
    PyObjC_END_WITH_GIL

    [NSException raise:NSInvalidArgumentException
                format:@"Cannot determine objective-C type of this number"];
    return -1;
}

- (NSString*)description
{
    return [self stringValue];
}

- (NSString*)stringValue
{
    PyObject* repr;
    NSString* result = nil;

    PyObjC_BEGIN_WITH_GIL
        repr = PyObject_Repr(value);
        if (repr == NULL) {
            PyObjC_GIL_FORWARD_EXC();
        }

        if (depythonify_python_object(repr, &result) == -1) {
            Py_DECREF(repr);
            PyObjC_GIL_FORWARD_EXC();
        }
        Py_DECREF(repr);
    PyObjC_END_WITH_GIL
    return result;
}

/* NSCoding support */

- (void)encodeWithCoder:(NSCoder*)coder
{
    int use_super = 0;

    PyObjC_BEGIN_WITH_GIL
        if (PyFloat_CheckExact(value)) {
            /* Float is a C double and can be roundtripped using
             * NSNumber.
             */
            use_super = 1;
        } else if (PyLong_CheckExact(value)) {
            /* Long object that fits in a long long */
            (void)PyLong_AsLongLong(value);
            if (PyErr_Occurred()) {
                PyErr_Clear();
                (void)PyLong_AsUnsignedLongLong(value);
                if (PyErr_Occurred()) {
                    PyErr_Clear();
                    use_super = 0;
                } else {
                    use_super = 1;
                }
            } else {
                use_super = 1;
            }
        }
    PyObjC_END_WITH_GIL

    if (use_super) {
        [super encodeWithCoder:coder];
    } else {
        /* XXX: Should check if coder requiresSecureCoding, and bail out in
         * that case.
         */
        PyObjC_encodeWithCoder(value, coder);
    }
}

/*
 * Helper method for initWithCoder, needed to deal with
 * recursive objects (e.g. o.value = o)
 */
- (void)pyobjcSetValue:(NSObject*)other
{
    PyObjC_BEGIN_WITH_GIL
        PyObject* v = id_to_python(other);

        SET_FIELD(value, v);
    PyObjC_END_WITH_GIL
}

- (id _Nullable)initWithCoder:(NSCoder*)coder
{
    if (PyObjC_Decoder != NULL) {
        PyObjC_BEGIN_WITH_GIL
            PyObject* cdr = id_to_python(coder);
            PyObject* setValue;
            PyObject* selfAsPython;
            PyObject* v;

            if (cdr == NULL) {
                PyObjC_GIL_FORWARD_EXC();
            }

            selfAsPython = PyObjCObject_New(self, 0, YES);
            if (selfAsPython == NULL) {
                PyObjC_GIL_FORWARD_EXC();
            }
            setValue = PyObject_GetAttrString(selfAsPython, "pyobjcSetValue_");

            v = PyObjC_CallDecoder(cdr, setValue);
            Py_DECREF(cdr);
            Py_DECREF(setValue);
            Py_DECREF(selfAsPython);

            if (v == NULL) {
                PyObjC_GIL_FORWARD_EXC();
            }

            Py_XDECREF(value);
            value = v;

            self = PyObjC_FindOrRegisterObjCProxy(value, self);

        PyObjC_END_WITH_GIL

        return self;

    } else {
        [NSException raise:NSInvalidArgumentException
                    format:@"decoding Python objects is not supported"];
        return nil;
    }
}

- (BOOL)isEqualToValue:(NSValue*)other
{
    return [self compare:(NSNumber*)other] == NSOrderedSame;
}

- (NSComparisonResult)compare:(NSNumber*)number
{
    /* Rely on -[NSNumber compare:] when the other value
     * is a number and we're not a python int that doesn't
     * fit into a 'long long'.
     *
     * In all other cases use Python's comparison semantics.
     */
    if ([number isKindOfClass:[NSNumber class]]
        && ![number isKindOfClass:[OC_PythonNumber class]]) {
        int use_super = 0;

        PyObjC_BEGIN_WITH_GIL
            if (PyLong_Check(value)) {
                PY_LONG_LONG r;
                r = PyLong_AsLongLong(value);
                if (r == -1 && PyErr_Occurred()) {
                    PyErr_Clear();
                } else {
                    use_super = 1;
                }
            }

        PyObjC_END_WITH_GIL;

        if (use_super) {
            return [super compare:number];
        }
    }

    PyObjC_BEGIN_WITH_GIL
        PyObject* other = id_to_python(number);
        int       r, ok;

        if (other == NULL) {
            PyObjC_GIL_FORWARD_EXC();
        }

        ok = PyObjC_Cmp(value, other, &r);
        Py_DECREF(other);
        if (ok == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }

        if (r < 0) {
            PyObjC_GIL_RETURN(NSOrderedAscending);
        } else if (r > 0) {
            PyObjC_GIL_RETURN(NSOrderedDescending);
        } else {
            PyObjC_GIL_RETURN(NSOrderedSame);
        }

    PyObjC_END_WITH_GIL
}

#define COMPARE_METHOD(NAME, OPERATOR)                                                   \
    -(BOOL)NAME : (NSObject* _Nullable)number                                            \
    {                                                                                    \
        PyObjC_BEGIN_WITH_GIL                                                            \
            PyObject* other = id_to_python(number);                                      \
            int       r;                                                                 \
            if (other == NULL) {                                                         \
                PyObjC_GIL_FORWARD_EXC();                                                \
            }                                                                            \
                                                                                         \
            r = PyObject_RichCompareBool(value, other, OPERATOR);                        \
            Py_DECREF(other);                                                            \
            if (r == -1) {                                                               \
                PyObjC_GIL_FORWARD_EXC();                                                \
            }                                                                            \
                                                                                         \
            if (r) {                                                                     \
                PyObjC_GIL_RETURN(YES);                                                  \
            } else {                                                                     \
                PyObjC_GIL_RETURN(NO);                                                   \
            }                                                                            \
                                                                                         \
        PyObjC_END_WITH_GIL                                                              \
    }

COMPARE_METHOD(isEqualTo, Py_EQ)
COMPARE_METHOD(isNotEqualTo, Py_NE)
COMPARE_METHOD(isGreaterThan, Py_GT)
COMPARE_METHOD(isGreaterThanOrEqualTo, Py_GE)
COMPARE_METHOD(isLessThan, Py_LT)
COMPARE_METHOD(isLessThanOrEqualTo, Py_LE)

- (BOOL)isEqualToNumber:(NSNumber*)number
{
    return [self isEqualTo:number];
}

- (Class)classForArchiver
{
    PyObjC_BEGIN_WITH_GIL
        @try {
            if (PyFloat_CheckExact(value)) {
                /* Float is a C double and can be roundtripped using
                 * NSNumber.
                 */
                PyObjC_GIL_RETURN([NSNumber class]);
            } else if (PyLong_CheckExact(value)) {
                /* Long object that fits in a long long */
                (void)PyLong_AsLongLong(value);
                if (PyErr_Occurred()) {
                    PyErr_Clear();
                    PyObjC_GIL_RETURN([self class]);
                } else {
                    PyObjC_GIL_RETURN([NSNumber class]);
                }
            } else {
                PyObjC_GIL_RETURN([self class]);
            }
        } @catch (NSObject* exc) {
            PyObjC_LEAVE_GIL;
            @throw;
        }
    PyObjC_END_WITH_GIL
}

- (Class _Nullable)classForKeyedArchiver
{
    return [self classForArchiver];
}

- (Class)classForCoder
{
    return [self classForArchiver];
}

- (id)copy
{
    return [self copyWithZone:NULL];
}

- (id)copyWithZone:(NSZone* _Nullable)zone __attribute__((__unused__))
{
    /* XXX: This is ok if value is a python builtin
     *      but not for arbitrary python objects.
     */
    [self retain];
    return self;
}

@end

NS_ASSUME_NONNULL_END
