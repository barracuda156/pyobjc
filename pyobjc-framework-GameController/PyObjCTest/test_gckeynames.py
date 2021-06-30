from PyObjCTools.TestSupport import TestCase, min_os_level
import GameController


class TestGCKeyNames(TestCase):
    @min_os_level("11.0")
    def test_constants11_0(self):
        self.assertIsInstance(GameController.GCKeyA, str)
        self.assertIsInstance(GameController.GCKeyB, str)
        self.assertIsInstance(GameController.GCKeyC, str)
        self.assertIsInstance(GameController.GCKeyD, str)
        self.assertIsInstance(GameController.GCKeyE, str)
        self.assertIsInstance(GameController.GCKeyF, str)
        self.assertIsInstance(GameController.GCKeyG, str)
        self.assertIsInstance(GameController.GCKeyH, str)
        self.assertIsInstance(GameController.GCKeyI, str)
        self.assertIsInstance(GameController.GCKeyJ, str)
        self.assertIsInstance(GameController.GCKeyK, str)
        self.assertIsInstance(GameController.GCKeyL, str)
        self.assertIsInstance(GameController.GCKeyM, str)
        self.assertIsInstance(GameController.GCKeyN, str)
        self.assertIsInstance(GameController.GCKeyO, str)
        self.assertIsInstance(GameController.GCKeyP, str)
        self.assertIsInstance(GameController.GCKeyQ, str)
        self.assertIsInstance(GameController.GCKeyR, str)
        self.assertIsInstance(GameController.GCKeyS, str)
        self.assertIsInstance(GameController.GCKeyT, str)
        self.assertIsInstance(GameController.GCKeyU, str)
        self.assertIsInstance(GameController.GCKeyV, str)
        self.assertIsInstance(GameController.GCKeyW, str)
        self.assertIsInstance(GameController.GCKeyX, str)
        self.assertIsInstance(GameController.GCKeyY, str)
        self.assertIsInstance(GameController.GCKeyZ, str)
        self.assertIsInstance(GameController.GCKeyOne, str)
        self.assertIsInstance(GameController.GCKeyTwo, str)
        self.assertIsInstance(GameController.GCKeyThree, str)
        self.assertIsInstance(GameController.GCKeyFour, str)
        self.assertIsInstance(GameController.GCKeyFive, str)
        self.assertIsInstance(GameController.GCKeySix, str)
        self.assertIsInstance(GameController.GCKeySeven, str)
        self.assertIsInstance(GameController.GCKeyEight, str)
        self.assertIsInstance(GameController.GCKeyNine, str)
        self.assertIsInstance(GameController.GCKeyZero, str)
        self.assertIsInstance(GameController.GCKeyReturnOrEnter, str)
        self.assertIsInstance(GameController.GCKeyEscape, str)
        self.assertIsInstance(GameController.GCKeyDeleteOrBackspace, str)
        self.assertIsInstance(GameController.GCKeyTab, str)
        self.assertIsInstance(GameController.GCKeySpacebar, str)
        self.assertIsInstance(GameController.GCKeyHyphen, str)
        self.assertIsInstance(GameController.GCKeyEqualSign, str)
        self.assertIsInstance(GameController.GCKeyOpenBracket, str)
        self.assertIsInstance(GameController.GCKeyCloseBracket, str)
        self.assertIsInstance(GameController.GCKeyBackslash, str)
        self.assertIsInstance(GameController.GCKeyNonUSPound, str)
        self.assertIsInstance(GameController.GCKeySemicolon, str)
        self.assertIsInstance(GameController.GCKeyQuote, str)
        self.assertIsInstance(GameController.GCKeyGraveAccentAndTilde, str)
        self.assertIsInstance(GameController.GCKeyComma, str)
        self.assertIsInstance(GameController.GCKeyPeriod, str)
        self.assertIsInstance(GameController.GCKeySlash, str)
        self.assertIsInstance(GameController.GCKeyCapsLock, str)

        self.assertIsInstance(GameController.GCKeyF1, str)
        self.assertIsInstance(GameController.GCKeyF2, str)
        self.assertIsInstance(GameController.GCKeyF3, str)
        self.assertIsInstance(GameController.GCKeyF4, str)
        self.assertIsInstance(GameController.GCKeyF5, str)
        self.assertIsInstance(GameController.GCKeyF6, str)
        self.assertIsInstance(GameController.GCKeyF7, str)
        self.assertIsInstance(GameController.GCKeyF8, str)
        self.assertIsInstance(GameController.GCKeyF9, str)
        self.assertIsInstance(GameController.GCKeyF10, str)
        self.assertIsInstance(GameController.GCKeyF11, str)
        self.assertIsInstance(GameController.GCKeyF12, str)
        self.assertIsInstance(GameController.GCKeyPrintScreen, str)
        self.assertIsInstance(GameController.GCKeyScrollLock, str)
        self.assertIsInstance(GameController.GCKeyPause, str)
        self.assertIsInstance(GameController.GCKeyInsert, str)
        self.assertIsInstance(GameController.GCKeyHome, str)
        self.assertIsInstance(GameController.GCKeyPageUp, str)
        self.assertIsInstance(GameController.GCKeyDeleteForward, str)
        self.assertIsInstance(GameController.GCKeyEnd, str)
        self.assertIsInstance(GameController.GCKeyPageDown, str)
        self.assertIsInstance(GameController.GCKeyRightArrow, str)
        self.assertIsInstance(GameController.GCKeyLeftArrow, str)
        self.assertIsInstance(GameController.GCKeyDownArrow, str)
        self.assertIsInstance(GameController.GCKeyUpArrow, str)

        self.assertIsInstance(GameController.GCKeyKeypadNumLock, str)
        self.assertIsInstance(GameController.GCKeyKeypadSlash, str)
        self.assertIsInstance(GameController.GCKeyKeypadAsterisk, str)
        self.assertIsInstance(GameController.GCKeyKeypadHyphen, str)
        self.assertIsInstance(GameController.GCKeyKeypadPlus, str)
        self.assertIsInstance(GameController.GCKeyKeypadEnter, str)
        self.assertIsInstance(GameController.GCKeyKeypad1, str)
        self.assertIsInstance(GameController.GCKeyKeypad2, str)
        self.assertIsInstance(GameController.GCKeyKeypad3, str)
        self.assertIsInstance(GameController.GCKeyKeypad4, str)
        self.assertIsInstance(GameController.GCKeyKeypad5, str)
        self.assertIsInstance(GameController.GCKeyKeypad6, str)
        self.assertIsInstance(GameController.GCKeyKeypad7, str)
        self.assertIsInstance(GameController.GCKeyKeypad8, str)
        self.assertIsInstance(GameController.GCKeyKeypad9, str)
        self.assertIsInstance(GameController.GCKeyKeypad0, str)
        self.assertIsInstance(GameController.GCKeyKeypadPeriod, str)
        self.assertIsInstance(GameController.GCKeyKeypadEqualSign, str)
        self.assertIsInstance(GameController.GCKeyNonUSBackslash, str)

        self.assertIsInstance(GameController.GCKeyApplication, str)
        self.assertIsInstance(GameController.GCKeyPower, str)

        self.assertIsInstance(GameController.GCKeyInternational1, str)
        self.assertIsInstance(GameController.GCKeyInternational2, str)
        self.assertIsInstance(GameController.GCKeyInternational3, str)
        self.assertIsInstance(GameController.GCKeyInternational4, str)
        self.assertIsInstance(GameController.GCKeyInternational5, str)
        self.assertIsInstance(GameController.GCKeyInternational6, str)
        self.assertIsInstance(GameController.GCKeyInternational7, str)
        self.assertIsInstance(GameController.GCKeyInternational8, str)
        self.assertIsInstance(GameController.GCKeyInternational9, str)

        self.assertIsInstance(GameController.GCKeyLANG1, str)

        self.assertIsInstance(GameController.GCKeyLANG2, str)

        self.assertIsInstance(GameController.GCKeyLANG3, str)

        self.assertIsInstance(GameController.GCKeyLANG4, str)

        self.assertIsInstance(GameController.GCKeyLANG5, str)

        self.assertIsInstance(GameController.GCKeyLANG6, str)
        self.assertIsInstance(GameController.GCKeyLANG7, str)
        self.assertIsInstance(GameController.GCKeyLANG8, str)
        self.assertIsInstance(GameController.GCKeyLANG9, str)

        self.assertIsInstance(GameController.GCKeyLeftControl, str)
        self.assertIsInstance(GameController.GCKeyLeftShift, str)
        self.assertIsInstance(GameController.GCKeyLeftAlt, str)
        self.assertIsInstance(GameController.GCKeyLeftGUI, str)
        self.assertIsInstance(GameController.GCKeyRightControl, str)
        self.assertIsInstance(GameController.GCKeyRightShift, str)
        self.assertIsInstance(GameController.GCKeyRightAlt, str)
        self.assertIsInstance(GameController.GCKeyRightGUI, str)

    @min_os_level("12.0")
    def test_constants12_0(self):
        self.assertIsInstance(GameController.GCKeyF13, str)
        self.assertIsInstance(GameController.GCKeyF14, str)
        self.assertIsInstance(GameController.GCKeyF15, str)
        self.assertIsInstance(GameController.GCKeyF16, str)
        self.assertIsInstance(GameController.GCKeyF17, str)
        self.assertIsInstance(GameController.GCKeyF18, str)
        self.assertIsInstance(GameController.GCKeyF19, str)
        self.assertIsInstance(GameController.GCKeyF20, str)
