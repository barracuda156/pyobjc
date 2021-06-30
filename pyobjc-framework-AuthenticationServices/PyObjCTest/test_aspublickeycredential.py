import AuthenticationServices  # noqa: F401
from PyObjCTools.TestSupport import TestCase, min_sdk_level
import objc


class TestASPublicKeyCredential(TestCase):
    @min_sdk_level("12.0")
    def test_protocols(self):
        objc.protocolNamed("ASPublicKeyCredential")
