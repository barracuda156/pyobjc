
/*
 *     *** GENERATED FILE ***
 *
 * This file is generated by Tools/generate-category-tests.py
 */
#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>
__attribute__((__visibility__("default")))
@interface OC_Category_GP28 : NSObject {
}
@end

__attribute__((__visibility__("default")))
@interface OC_Category_P28 : OC_Category_GP28 {
}
@end

__attribute__((__visibility__("default")))
@interface OC_Category_C28 : OC_Category_P28 {
}
@end

@implementation
OC_Category_P28 (Cat)
- (id)gpMethod1
{
    return @"P28 - gpMethod1 - P28(Cat)";
}
- (id)gpMethod5
{
    return @"P28 - gpMethod5 - P28(Cat)";
}
- (id)pMethod1
{
    return @"P28 - pMethod1 - P28(Cat)";
}
- (id)pMethod3
{
    return @"P28 - pMethod3 - P28(Cat)";
}
- (id)method1
{
    return @"P28 - method1 - P28(Cat)";
}
- (id)method2
{
    return @"P28 - method2 - P28(Cat)";
}
@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "category_p28", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit_category_p28(void);

PyObject* __attribute__((__visibility__("default"))) PyInit_category_p28(void)
{
    PyObject* m;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    PyObjC_ImportAPI(m);

    return m;
}