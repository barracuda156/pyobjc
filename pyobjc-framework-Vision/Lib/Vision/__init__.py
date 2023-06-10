"""
Python mapping for the Vision framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import Foundation
    import Quartz
    import CoreML
    import objc
    from . import _metadata, _Vision

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="Vision",
        frameworkIdentifier="com.apple.VN",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/Vision.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(
            _Vision,
            Quartz,
            CoreML,
            Foundation,
        ),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    del sys.modules["Vision._metadata"]


globals().pop("_setup")()
