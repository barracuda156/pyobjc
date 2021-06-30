import SoundAnalysis
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestSNError(TestCase):
    @min_os_level("12.0")
    def test_constants12_0(self):
        self.assertIsInstance(SoundAnalysis.SNClassifierIdentifierVersion1, str)
