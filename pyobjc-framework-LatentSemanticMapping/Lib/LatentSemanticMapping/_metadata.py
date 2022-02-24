# This file is generated by objective.metadata
#
# Last update: Sun Feb 20 18:56:51 2022
#
# flake8: noqa

import objc, sys
from typing import NewType

if sys.maxsize > 2**32:

    def sel32or64(a, b):
        return b

else:

    def sel32or64(a, b):
        return a


if objc.arch == "arm64":

    def selAorI(a, b):
        return a

else:

    def selAorI(a, b):
        return b


misc = {}
constants = """$$"""
enums = """$kLSMClusterAgglomerative@4$kLSMClusterCategories@0$kLSMClusterKMeans@0$kLSMClusterTokens@2$kLSMClusterWords@1$kLSMMapBadCluster@-6644$kLSMMapBadPath@-6643$kLSMMapDiscardCounts@1$kLSMMapHashText@256$kLSMMapLoadMutable@2$kLSMMapNoSuchCategory@-6641$kLSMMapOutOfState@-6640$kLSMMapOverflow@-6645$kLSMMapPairs@1$kLSMMapTriplets@2$kLSMMapWriteError@-6642$kLSMResultBestWords@1$kLSMTextApplySpamHeuristics@4$kLSMTextPreserveAcronyms@2$kLSMTextPreserveCase@1$"""
misc.update({})
misc.update(
    {
        "kLSMAlgorithmDense": "LSMAlgorithmDense",
        "kLSMPrecisionFloat": "LSMPrecisionFloat",
        "kLSMSweepCutoffKey": "LSMSweepCutoff",
        "kLSMAlgorithmSparse": "LSMAlgorithmSparse",
        "kLSMDimensionKey": "LSMDimension",
        "kLSMAlgorithmKey": "LSMAlgorithm",
        "kLSMPrecisionKey": "LSMPrecision",
        "kLSMPrecisionDouble": "LSMPrecisionDouble",
        "kLSMSweepAgeKey": "LSMSweepAge",
        "kLSMIterationsKey": "LSMIterations",
    }
)
functions = {
    "LSMMapGetCategoryCount": (b"q^{__LSMMap=}",),
    "LSMMapAddTextWithWeight": (b"i^{__LSMMap=}^{__LSMText=}If",),
    "LSMTextAddToken": (b"i^{__LSMText=}^{__CFData=}",),
    "LSMMapSetStopWords": (b"i^{__LSMMap=}^{__LSMText=}",),
    "LSMTextGetTypeID": (b"Q",),
    "LSMMapStartTraining": (b"i^{__LSMMap=}",),
    "LSMMapCompile": (b"i^{__LSMMap=}",),
    "LSMMapWriteToStream": (b"i^{__LSMMap=}^{__LSMText=}^{__CFWriteStream=}Q",),
    "LSMResultCopyWordCluster": (
        b"^{__CFArray=}^{__LSMResult=}q",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "LSMResultGetCount": (b"q^{__LSMResult=}",),
    "LSMResultGetCategory": (b"I^{__LSMResult=}q",),
    "LSMMapCreate": (
        b"^{__LSMMap=}^{__CFAllocator=}Q",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "LSMResultGetTypeID": (b"Q",),
    "LSMResultCreate": (
        b"^{__LSMResult=}^{__CFAllocator=}^{__LSMMap=}^{__LSMText=}qQ",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "LSMResultCopyWord": (
        b"^{__CFString=}^{__LSMResult=}q",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "LSMMapCreateClusters": (
        b"^{__CFArray=}^{__CFAllocator=}^{__LSMMap=}^{__CFArray=}qQ",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "LSMMapApplyClusters": (b"i^{__LSMMap=}^{__CFArray=}",),
    "LSMTextAddWords": (b"i^{__LSMText=}^{__CFString=}^{__CFLocale=}Q",),
    "LSMResultCopyTokenCluster": (
        b"^{__CFArray=}^{__LSMResult=}q",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "LSMMapAddText": (b"i^{__LSMMap=}^{__LSMText=}I",),
    "LSMTextCreate": (
        b"^{__LSMText=}^{__CFAllocator=}^{__LSMMap=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "LSMMapWriteToURL": (b"i^{__LSMMap=}^{__CFURL=}Q",),
    "LSMResultGetScore": (b"f^{__LSMResult=}q",),
    "LSMMapCreateFromURL": (
        b"^{__LSMMap=}^{__CFAllocator=}^{__CFURL=}Q",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "LSMMapSetProperties": (b"v^{__LSMMap=}^{__CFDictionary=}",),
    "LSMResultCopyToken": (
        b"^{__CFData=}^{__LSMResult=}q",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "LSMMapGetProperties": (b"^{__CFDictionary=}^{__LSMMap=}",),
    "LSMMapAddCategory": (b"I^{__LSMMap=}",),
    "LSMTextAddWord": (b"i^{__LSMText=}^{__CFString=}",),
    "LSMMapGetTypeID": (b"Q",),
}
cftypes = [
    ("LSMMapRef", b"^{__LSMMap=}", "LSMMapGetTypeID", None),
    ("LSMResultRef", b"^{__LSMResult=}", "LSMResultGetTypeID", None),
    ("LSMTextRef", b"^{__LSMText=}", "LSMTextGetTypeID", None),
]
expressions = {}

# END OF FILE
