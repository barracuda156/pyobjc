import SoundAnalysis
from PyObjCTools.TestSupport import TestCase


class TestSNTimeDurationConstraint(TestCase):
    def test_constants(self):
        self.assertEqual(SoundAnalysis.SNTimeDurationConstraintTypeEnumerated, 1)
        self.assertEqual(SoundAnalysis.SNTimeDurationConstraintTypeRange, 2)
