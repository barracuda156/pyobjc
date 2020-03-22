# This file is generated by objective.metadata
#
# Last update: Sun Mar 22 17:12:49 2020
#
# flake8: noqa

import objc, sys

if sys.maxsize > 2 ** 32:
    def sel32or64(a, b): return b
else:
    def sel32or64(a, b): return a

misc = {
}
constants = '''$SLServiceTypeFacebook$SLServiceTypeLinkedIn$SLServiceTypeSinaWeibo$SLServiceTypeTencentWeibo$SLServiceTypeTwitter$'''
enums = '''$SLRequestMethodDELETE@2$SLRequestMethodGET@0$SLRequestMethodPOST@1$SLRequestMethodPUT@3$'''
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b'SLComposeServiceViewController', b'isContentValid', {'retval': {'type': b'Z'}})
    r(b'SLRequest', b'performRequestWithHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}, 3: {'type': b'@'}}}}}})
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
