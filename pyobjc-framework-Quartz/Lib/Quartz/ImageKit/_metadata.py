# This file is generated by objective.metadata
#
# Last update: Sat Jul 22 14:57:27 2017

import objc, sys

if sys.maxsize > 2 ** 32:
    def sel32or64(a, b): return b
else:
    def sel32or64(a, b): return a
if sys.byteorder == 'little':
    def littleOrBig(a, b): return a
else:
    def littleOrBig(a, b): return b

misc = {
}
constants = '''$IKFilterBrowserDefaultInputImage$IKFilterBrowserExcludeCategories$IKFilterBrowserExcludeFilters$IKFilterBrowserFilterDoubleClickNotification$IKFilterBrowserFilterSelectedNotification$IKFilterBrowserShowCategories$IKFilterBrowserShowPreview$IKFilterBrowserWillPreviewFilterNotification$IKImageBrowserBackgroundColorKey$IKImageBrowserCGImageRepresentationType$IKImageBrowserCGImageSourceRepresentationType$IKImageBrowserCellBackgroundLayer$IKImageBrowserCellForegroundLayer$IKImageBrowserCellLayerTypeBackground$IKImageBrowserCellLayerTypeForeground$IKImageBrowserCellLayerTypePlaceHolder$IKImageBrowserCellLayerTypeSelection$IKImageBrowserCellPlaceHolderLayer$IKImageBrowserCellSelectionLayer$IKImageBrowserCellsHighlightedTitleAttributesKey$IKImageBrowserCellsOutlineColorKey$IKImageBrowserCellsSubtitleAttributesKey$IKImageBrowserCellsTitleAttributesKey$IKImageBrowserGroupBackgroundColorKey$IKImageBrowserGroupFooterLayer$IKImageBrowserGroupHeaderLayer$IKImageBrowserGroupRangeKey$IKImageBrowserGroupStyleKey$IKImageBrowserGroupTitleKey$IKImageBrowserIconRefPathRepresentationType$IKImageBrowserIconRefRepresentationType$IKImageBrowserNSBitmapImageRepresentationType$IKImageBrowserNSDataRepresentationType$IKImageBrowserNSImageRepresentationType$IKImageBrowserNSURLRepresentationType$IKImageBrowserPDFPageRepresentationType$IKImageBrowserPathRepresentationType$IKImageBrowserQCCompositionPathRepresentationType$IKImageBrowserQCCompositionRepresentationType$IKImageBrowserQTMoviePathRepresentationType$IKImageBrowserQTMovieRepresentationType$IKImageBrowserQuickLookPathRepresentationType$IKImageBrowserSelectionColorKey$IKOverlayTypeBackground$IKOverlayTypeImage$IKPictureTakerAllowsEditingKey$IKPictureTakerAllowsFileChoosingKey$IKPictureTakerAllowsVideoCaptureKey$IKPictureTakerCropAreaSizeKey$IKPictureTakerImageTransformsKey$IKPictureTakerInformationalTextKey$IKPictureTakerOutputImageMaxSizeKey$IKPictureTakerRemainOpenAfterValidateKey$IKPictureTakerShowAddressBookPicture$IKPictureTakerShowAddressBookPictureKey$IKPictureTakerShowEffectsKey$IKPictureTakerShowEmptyPicture$IKPictureTakerShowEmptyPictureKey$IKPictureTakerShowRecentPictureKey$IKPictureTakerUpdateRecentPictureKey$IKSlideshowAudioFile$IKSlideshowModeImages$IKSlideshowModeOther$IKSlideshowModePDF$IKSlideshowPDFDisplayBox$IKSlideshowPDFDisplayMode$IKSlideshowPDFDisplaysAsBook$IKSlideshowScreen$IKSlideshowStartIndex$IKSlideshowStartPaused$IKSlideshowWrapAround$IKToolModeAnnotate$IKToolModeCrop$IKToolModeMove$IKToolModeNone$IKToolModeRotate$IKToolModeSelect$IKToolModeSelectEllipse$IKToolModeSelectLasso$IKToolModeSelectRect$IKUIFlavorAllowFallback$IKUISizeFlavor$IKUISizeMini$IKUISizeRegular$IKUISizeSmall$IKUImaxSize$IK_ApertureBundleIdentifier$IK_MailBundleIdentifier$IK_PhotosBundleIdentifier$IK_iPhotoBundleIdentifier$'''
enums = '''$IKCameraDeviceViewDisplayModeIcon@1$IKCameraDeviceViewDisplayModeTable@0$IKCameraDeviceViewTransferModeFileBased@0$IKCameraDeviceViewTransferModeMemoryBased@1$IKCellsStyleNone@0$IKCellsStyleOutlined@2$IKCellsStyleShadowed@1$IKCellsStyleSubtitled@8$IKCellsStyleTitled@4$IKDeviceBrowserViewDisplayModeIcon@2$IKDeviceBrowserViewDisplayModeOutline@1$IKDeviceBrowserViewDisplayModeTable@0$IKGroupBezelStyle@0$IKGroupDisclosureStyle@1$IKImageBrowserDropBefore@1$IKImageBrowserDropOn@0$IKImageStateInvalid@1$IKImageStateNoImage@0$IKImageStateReady@2$IKScannerDeviceViewDisplayModeAdvanced@1$IKScannerDeviceViewDisplayModeSimple@0$IKScannerDeviceViewTransferModeFileBased@0$IKScannerDeviceViewTransferModeMemoryBased@1$'''
misc.update({})
aliases = {'IKImagePickerShowEffectsKey': 'IKPictureTakerShowEffectsKey', 'IKImagePickerOutputImageMaxSizeKey': 'IKPictureTakerOutputImageMaxSizeKey', 'IKImagePickerImageTransformsKey': 'IKPictureTakerImageTransformsKey', 'IKImagePickerAllowsFileChoosingKey': 'IKPictureTakerAllowsFileChoosingKey', 'IKImagePickerAllowsEditingKey': 'IKPictureTakerAllowsEditingKey', 'IKImagePickerInformationalTextKey': 'IKPictureTakerInformationalTextKey', 'IKImagePickerCropAreaSizeKey': 'IKPictureTakerCropAreaSizeKey', 'IKImagePickerAllowsVideoCaptureKey': 'IKPictureTakerAllowsVideoCaptureKey', 'IKImagePickerUpdateRecentPictureKey': 'IKPictureTakerUpdateRecentPictureKey', 'IKImagePickerShowRecentPictureKey': 'IKPictureTakerShowRecentPictureKey'}
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b'IKCameraDeviceView', b'canDeleteSelectedItems', {'retval': {'type': b'Z'}})
    r(b'IKCameraDeviceView', b'canDownloadSelectedItems', {'retval': {'type': b'Z'}})
    r(b'IKCameraDeviceView', b'canRotateSelectedItemsLeft', {'retval': {'type': b'Z'}})
    r(b'IKCameraDeviceView', b'canRotateSelectedItemsRight', {'retval': {'type': b'Z'}})
    r(b'IKCameraDeviceView', b'displaysDownloadsDirectoryControl', {'retval': {'type': b'Z'}})
    r(b'IKCameraDeviceView', b'displaysPostProcessApplicationControl', {'retval': {'type': b'Z'}})
    r(b'IKCameraDeviceView', b'hasDisplayModeIcon', {'retval': {'type': b'Z'}})
    r(b'IKCameraDeviceView', b'hasDisplayModeTable', {'retval': {'type': b'Z'}})
    r(b'IKCameraDeviceView', b'selectIndexes:byExtendingSelection:', {'arguments': {3: {'type': b'Z'}}})
    r(b'IKCameraDeviceView', b'setDisplaysDownloadsDirectoryControl:', {'arguments': {2: {'type': b'Z'}}})
    r(b'IKCameraDeviceView', b'setDisplaysPostProcessApplicationControl:', {'arguments': {2: {'type': b'Z'}}})
    r(b'IKCameraDeviceView', b'setHasDisplayModeIcon:', {'arguments': {2: {'type': b'Z'}}})
    r(b'IKCameraDeviceView', b'setHasDisplayModeTable:', {'arguments': {2: {'type': b'Z'}}})
    r(b'IKDeviceBrowserView', b'displaysLocalCameras', {'retval': {'type': b'Z'}})
    r(b'IKDeviceBrowserView', b'displaysLocalScanners', {'retval': {'type': b'Z'}})
    r(b'IKDeviceBrowserView', b'displaysNetworkCameras', {'retval': {'type': b'Z'}})
    r(b'IKDeviceBrowserView', b'displaysNetworkScanners', {'retval': {'type': b'Z'}})
    r(b'IKDeviceBrowserView', b'setDisplaysLocalCameras:', {'arguments': {2: {'type': b'Z'}}})
    r(b'IKDeviceBrowserView', b'setDisplaysLocalScanners:', {'arguments': {2: {'type': b'Z'}}})
    r(b'IKDeviceBrowserView', b'setDisplaysNetworkCameras:', {'arguments': {2: {'type': b'Z'}}})
    r(b'IKDeviceBrowserView', b'setDisplaysNetworkScanners:', {'arguments': {2: {'type': b'Z'}}})
    r(b'IKFilterBrowserPanel', b'beginSheetWithOptions:modalForWindow:modalDelegate:didEndSelector:contextInfo:', {'arguments': {5: {'sel_of_type': sel32or64(b'v@:@i^v', b'v@:@q^v')}}})
    r(b'IKFilterBrowserPanel', b'beginWithOptions:modelessDelegate:didEndSelector:contextInfo:', {'arguments': {4: {'sel_of_type': sel32or64(b'v@:@i^v', b'v@:@q^v')}}})
    r(b'IKFilterBrowserView', b'setPreviewState:', {'arguments': {2: {'type': b'Z'}}})
    r(b'IKImageBrowserCell', b'isSelected', {'retval': {'type': b'Z'}})
    r(b'IKImageBrowserView', b'allowsDroppingOnItems', {'retval': {'type': b'Z'}})
    r(b'IKImageBrowserView', b'allowsEmptySelection', {'retval': {'type': b'Z'}})
    r(b'IKImageBrowserView', b'allowsMultipleSelection', {'retval': {'type': b'Z'}})
    r(b'IKImageBrowserView', b'allowsReordering', {'retval': {'type': b'Z'}})
    r(b'IKImageBrowserView', b'animates', {'retval': {'type': b'Z'}})
    r(b'IKImageBrowserView', b'canControlQuickLookPanel', {'retval': {'type': b'Z'}})
    r(b'IKImageBrowserView', b'constrainsToOriginalSize', {'retval': {'type': b'Z'}})
    r(b'IKImageBrowserView', b'isGroupExpandedAtIndex:', {'retval': {'type': b'Z'}})
    r(b'IKImageBrowserView', b'setAllowsDroppingOnItems:', {'arguments': {2: {'type': b'Z'}}})
    r(b'IKImageBrowserView', b'setAllowsEmptySelection:', {'arguments': {2: {'type': b'Z'}}})
    r(b'IKImageBrowserView', b'setAllowsMultipleSelection:', {'arguments': {2: {'type': b'Z'}}})
    r(b'IKImageBrowserView', b'setAllowsReordering:', {'arguments': {2: {'type': b'Z'}}})
    r(b'IKImageBrowserView', b'setAnimates:', {'arguments': {2: {'type': b'Z'}}})
    r(b'IKImageBrowserView', b'setCanControlQuickLookPanel:', {'arguments': {2: {'type': b'Z'}}})
    r(b'IKImageBrowserView', b'setConstrainsToOriginalSize:', {'arguments': {2: {'type': b'Z'}}})
    r(b'IKImageBrowserView', b'setSelectionIndexes:byExtendingSelection:', {'arguments': {3: {'type': b'Z'}}})
    r(b'IKImagePicker', b'beginImagePickerSheetForWindow:withDelegate:didEndSelector:contextInfo:', {'arguments': {4: {'sel_of_type': sel32or64(b'v@:@I^v', b'v@:@Q^v')}}})
    r(b'IKImagePicker', b'beginImagePickerWithDelegate:didEndSelector:contextInfo:', {'arguments': {3: {'sel_of_type': sel32or64(b'v@:@I^v', b'v@:@Q^v')}}})
    r(b'IKImageView', b'autohidesScrollers', {'retval': {'type': b'Z'}})
    r(b'IKImageView', b'autoresizes', {'retval': {'type': b'Z'}})
    r(b'IKImageView', b'doubleClickOpensImageEditPanel', {'retval': {'type': b'Z'}})
    r(b'IKImageView', b'editable', {'retval': {'type': b'Z'}})
    r(b'IKImageView', b'hasHorizontalScroller', {'retval': {'type': b'Z'}})
    r(b'IKImageView', b'hasVerticalScroller', {'retval': {'type': b'Z'}})
    r(b'IKImageView', b'setAutohidesScrollers:', {'arguments': {2: {'type': b'Z'}}})
    r(b'IKImageView', b'setAutoresizes:', {'arguments': {2: {'type': b'Z'}}})
    r(b'IKImageView', b'setDoubleClickOpensImageEditPanel:', {'arguments': {2: {'type': b'Z'}}})
    r(b'IKImageView', b'setEditable:', {'arguments': {2: {'type': b'Z'}}})
    r(b'IKImageView', b'setHasHorizontalScroller:', {'arguments': {2: {'type': b'Z'}}})
    r(b'IKImageView', b'setHasVerticalScroller:', {'arguments': {2: {'type': b'Z'}}})
    r(b'IKImageView', b'setSupportsDragAndDrop:', {'arguments': {2: {'type': b'Z'}}})
    r(b'IKImageView', b'supportsDragAndDrop', {'retval': {'type': b'Z'}})
    r(b'IKPictureTaker', b'beginPictureTakerSheetForWindow:withDelegate:didEndSelector:contextInfo:', {'arguments': {4: {'sel_of_type': sel32or64(b'v@:@i^v', b'v@:@q^v')}}})
    r(b'IKPictureTaker', b'beginPictureTakerWithDelegate:didEndSelector:contextInfo:', {'arguments': {3: {'sel_of_type': sel32or64(b'v@:@i^v', b'v@:@q^v')}}})
    r(b'IKPictureTaker', b'mirroring', {'retval': {'type': b'Z'}})
    r(b'IKPictureTaker', b'popUpRecentsMenuForView:withDelegate:didEndSelector:contextInfo:', {'arguments': {4: {'sel_of_type': sel32or64(b'v@:@i^v', b'v@:@q^v')}}})
    r(b'IKPictureTaker', b'setMirroring:', {'arguments': {2: {'type': b'Z'}}})
    r(b'IKScannerDeviceView', b'displaysDownloadsDirectoryControl', {'retval': {'type': b'Z'}})
    r(b'IKScannerDeviceView', b'displaysPostProcessApplicationControl', {'retval': {'type': b'Z'}})
    r(b'IKScannerDeviceView', b'hasDisplayModeAdvanced', {'retval': {'type': b'Z'}})
    r(b'IKScannerDeviceView', b'hasDisplayModeSimple', {'retval': {'type': b'Z'}})
    r(b'IKScannerDeviceView', b'setDisplaysDownloadsDirectoryControl:', {'arguments': {2: {'type': b'Z'}}})
    r(b'IKScannerDeviceView', b'setDisplaysPostProcessApplicationControl:', {'arguments': {2: {'type': b'Z'}}})
    r(b'IKScannerDeviceView', b'setHasDisplayModeAdvanced:', {'arguments': {2: {'type': b'Z'}}})
    r(b'IKScannerDeviceView', b'setHasDisplayModeSimple:', {'arguments': {2: {'type': b'Z'}}})
    r(b'IKSlideshow', b'canExportToApplication:', {'retval': {'type': b'Z'}})
    r(b'NSObject', b'cameraDeviceView:didDownloadFile:location:fileData:error:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}, 4: {'type': b'@'}, 5: {'type': b'@'}, 6: {'type': b'@'}}})
    r(b'NSObject', b'cameraDeviceView:didEncounterError:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
    r(b'NSObject', b'cameraDeviceViewSelectionDidChange:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'canExportSlideshowItemAtIndex:toApplication:', {'required': False, 'retval': {'type': b'Z'}, 'arguments': {2: {'type': sel32or64(b'I', b'Q')}, 3: {'type': b'@'}}})
    r(b'NSObject', b'deviceBrowserView:didEncounterError:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
    r(b'NSObject', b'deviceBrowserView:selectionDidChange:', {'required': True, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
    r(b'NSObject', b'hasAdjustMode', {'required': False, 'retval': {'type': b'Z'}})
    r(b'NSObject', b'hasDetailsMode', {'required': False, 'retval': {'type': b'Z'}})
    r(b'NSObject', b'hasEffectsMode', {'required': False, 'retval': {'type': b'Z'}})
    r(b'NSObject', b'image', {'required': True, 'retval': {'type': b'^{CGImage=}'}})
    r(b'NSObject', b'imageBrowser:backgroundWasRightClickedWithEvent:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
    r(b'NSObject', b'imageBrowser:cellAtIndex:', {'retval': {'type': b'@'}, 'arguments': {2: {'type': b'@'}, 3: {'type': sel32or64(b'I', b'L')}}})
    r(b'NSObject', b'imageBrowser:cellWasDoubleClickedAtIndex:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': sel32or64(b'I', b'Q')}}})
    r(b'NSObject', b'imageBrowser:cellWasRightClickedAtIndex:withEvent:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': sel32or64(b'I', b'Q')}, 4: {'type': b'@'}}})
    r(b'NSObject', b'imageBrowser:groupAtIndex:', {'retval': {'type': b'@'}, 'arguments': {2: {'type': b'@'}, 3: {'type': sel32or64(b'I', b'Q')}}})
    r(b'NSObject', b'imageBrowser:itemAtIndex:', {'retval': {'type': b'@'}, 'arguments': {2: {'type': b'@'}, 3: {'type': sel32or64(b'I', b'Q')}}})
    r(b'NSObject', b'imageBrowser:moveCellsAtIndexes:toIndex:', {'retval': {'type': b'Z'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}, 4: {'type': sel32or64(b'I', b'L')}}})
    r(b'NSObject', b'imageBrowser:moveItemsAtIndexes:toIndex:', {'retval': {'type': b'Z'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}, 4: {'type': sel32or64(b'I', b'Q')}}})
    r(b'NSObject', b'imageBrowser:removeCellsAtIndexes:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
    r(b'NSObject', b'imageBrowser:removeItemsAtIndexes:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
    r(b'NSObject', b'imageBrowser:writeCellsAtIndexes:toPasteboard:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}, 4: {'type': b'@'}}})
    r(b'NSObject', b'imageBrowser:writeItemsAtIndexes:toPasteboard:', {'retval': {'type': sel32or64(b'I', b'Q')}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}, 4: {'type': b'@'}}})
    r(b'NSObject', b'imageBrowserSelectionDidChange:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'imageProperties', {'required': False, 'retval': {'type': b'@'}})
    r(b'NSObject', b'imageRepresentation', {'retval': {'type': b'@'}})
    r(b'NSObject', b'imageRepresentationType', {'retval': {'type': b'@'}})
    r(b'NSObject', b'imageSubtitle', {'retval': {'type': b'@'}})
    r(b'NSObject', b'imageTitle', {'retval': {'type': b'@'}})
    r(b'NSObject', b'imageUID', {'retval': {'type': b'@'}})
    r(b'NSObject', b'imageVersion', {'retval': {'type': sel32or64(b'I', b'Q')}})
    r(b'NSObject', b'isSelectable', {'retval': {'type': b'Z'}})
    r(b'NSObject', b'nameOfSlideshowItemAtIndex:', {'required': False, 'retval': {'type': b'@'}, 'arguments': {2: {'type': sel32or64(b'I', b'Q')}}})
    r(b'NSObject', b'numberOfCellsInImageBrowser:', {'retval': {'type': sel32or64(b'I', b'L')}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'numberOfGroupsInImageBrowser:', {'retval': {'type': sel32or64(b'I', b'Q')}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'numberOfItemsInImageBrowser:', {'retval': {'type': sel32or64(b'I', b'Q')}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'numberOfSlideshowItems', {'required': True, 'retval': {'type': sel32or64(b'I', b'Q')}})
    r(b'NSObject', b'provideViewForUIConfiguration:excludedKeys:', {'required': True, 'retval': {'type': b'@'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
    r(b'NSObject', b'saveOptions:shouldShowUTType:', {'retval': {'type': b'Z'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
    r(b'NSObject', b'scannerDeviceView:didEncounterError:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
    r(b'NSObject', b'scannerDeviceView:didScanToBandData:scanInfo:error:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}, 4: {'type': b'@'}, 5: {'type': b'@'}}})
    r(b'NSObject', b'scannerDeviceView:didScanToURL:error:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}, 4: {'type': b'@'}}})
    r(b'NSObject', b'scannerDeviceView:didScanToURL:fileData:error:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}, 4: {'type': b'@'}, 5: {'type': b'@'}}})
    r(b'NSObject', b'setImage:imageProperties:', {'required': True, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'^{CGImage=}'}, 3: {'type': b'@'}}})
    r(b'NSObject', b'slideshowDidChangeCurrentIndex:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': sel32or64(b'I', b'Q')}}})
    r(b'NSObject', b'slideshowDidStop', {'required': False, 'retval': {'type': b'v'}})
    r(b'NSObject', b'slideshowItemAtIndex:', {'required': True, 'retval': {'type': b'@'}, 'arguments': {2: {'type': sel32or64(b'I', b'Q')}}})
    r(b'NSObject', b'slideshowWillStart', {'required': False, 'retval': {'type': b'v'}})
    r(b'NSObject', b'thumbnailWithMaximumSize:', {'required': False, 'retval': {'type': b'^{CGImage=}'}, 'arguments': {2: {'type': sel32or64(b'{_NSSize=ff}', b'{CGSize=dd}')}}})
finally:
    objc._updatingMetadata(False)
protocols={'IKImageBrowserItem': objc.informal_protocol('IKImageBrowserItem', [objc.selector(None, b'imageTitle', b'@@:', isRequired=False), objc.selector(None, b'imageSubtitle', b'@@:', isRequired=False), objc.selector(None, b'imageRepresentationType', b'@@:', isRequired=False), objc.selector(None, b'imageUID', b'@@:', isRequired=False), objc.selector(None, b'isSelectable', b'Z@:', isRequired=False), objc.selector(None, b'imageVersion', sel32or64(b'I@:', b'Q@:'), isRequired=False), objc.selector(None, b'imageRepresentation', b'@@:', isRequired=False)]), 'IKSaveOptionsDelegate': objc.informal_protocol('IKSaveOptionsDelegate', [objc.selector(None, b'saveOptions:shouldShowUTType:', b'Z@:@@', isRequired=False)]), 'IKImageBrowserDataSourceDeprecated': objc.informal_protocol('IKImageBrowserDataSourceDeprecated', [objc.selector(None, b'imageBrowser:moveCellsAtIndexes:toIndex:', sel32or64(b'Z@:@@I', b'Z@:@@L'), isRequired=False), objc.selector(None, b'imageBrowser:cellAtIndex:', sel32or64(b'@@:@I', b'@@:@L'), isRequired=False), objc.selector(None, b'numberOfCellsInImageBrowser:', sel32or64(b'I@:@', b'L@:@'), isRequired=False), objc.selector(None, b'imageBrowser:writeCellsAtIndexes:toPasteboard:', b'v@:@@@', isRequired=False), objc.selector(None, b'imageBrowser:removeCellsAtIndexes:', b'v@:@@', isRequired=False)]), 'IKImageBrowserDelegate': objc.informal_protocol('IKImageBrowserDelegate', [objc.selector(None, b'imageBrowser:cellWasRightClickedAtIndex:withEvent:', sel32or64(b'v@:@I@', b'v@:@Q@'), isRequired=False), objc.selector(None, b'imageBrowserSelectionDidChange:', b'v@:@', isRequired=False), objc.selector(None, b'imageBrowser:cellWasDoubleClickedAtIndex:', sel32or64(b'v@:@I', b'v@:@Q'), isRequired=False), objc.selector(None, b'imageBrowser:backgroundWasRightClickedWithEvent:', b'v@:@@', isRequired=False)]), 'IKImageBrowserDataSource': objc.informal_protocol('IKImageBrowserDataSource', [objc.selector(None, b'imageBrowser:groupAtIndex:', sel32or64(b'@@:@I', b'@@:@Q'), isRequired=False), objc.selector(None, b'numberOfItemsInImageBrowser:', sel32or64(b'I@:@', b'Q@:@'), isRequired=False), objc.selector(None, b'imageBrowser:moveItemsAtIndexes:toIndex:', sel32or64(b'Z@:@@I', b'Z@:@@Q'), isRequired=False), objc.selector(None, b'numberOfGroupsInImageBrowser:', sel32or64(b'I@:@', b'Q@:@'), isRequired=False), objc.selector(None, b'imageBrowser:itemAtIndex:', sel32or64(b'@@:@I', b'@@:@Q'), isRequired=False), objc.selector(None, b'imageBrowser:removeItemsAtIndexes:', b'v@:@@', isRequired=False), objc.selector(None, b'imageBrowser:writeItemsAtIndexes:toPasteboard:', sel32or64(b'I@:@@@', b'Q@:@@@'), isRequired=False)])}
expressions = {}

# END OF FILE
