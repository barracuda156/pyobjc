"""
Python mapping for the ScreenSaver framework on MacOS X

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


# Load the ScreenSaver framework, and gather all classes defined there
import objc

import AppKit
del AppKit

# Custom method signature (undocumented class, this is a guess)
objc.set_signature_for_selector("ScreenSaverUserInfo", "loginUserName:andID:", "v@:o^@o^I")

objc.loadBundle("ScreenSaver", globals(), bundle_path="/System/Library/Frameworks/ScreenSaver.framework")

del objc
# NOTE: One MacOSX 10.2.4 the framework doesn't define constants,
# therefore there is no _ScreenSaver module.

# Define usefull utility methods here
