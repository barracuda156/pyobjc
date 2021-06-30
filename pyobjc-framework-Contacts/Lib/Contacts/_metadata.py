# This file is generated by objective.metadata
#
# Last update: Sat Jun 27 18:39:16 2020
#
# flake8: noqa

import objc, sys

if sys.maxsize > 2 ** 32:

    def sel32or64(a, b):
        return b


else:

    def sel32or64(a, b):
        return a


misc = {}
constants = """$CNContactBirthdayKey$CNContactDatesKey$CNContactDepartmentNameKey$CNContactEmailAddressesKey$CNContactFamilyNameKey$CNContactGivenNameKey$CNContactIdentifierKey$CNContactImageDataAvailableKey$CNContactImageDataKey$CNContactInstantMessageAddressesKey$CNContactJobTitleKey$CNContactMiddleNameKey$CNContactNamePrefixKey$CNContactNameSuffixKey$CNContactNicknameKey$CNContactNonGregorianBirthdayKey$CNContactNoteKey$CNContactOrganizationNameKey$CNContactPhoneNumbersKey$CNContactPhoneticFamilyNameKey$CNContactPhoneticGivenNameKey$CNContactPhoneticMiddleNameKey$CNContactPhoneticOrganizationNameKey$CNContactPostalAddressesKey$CNContactPreviousFamilyNameKey$CNContactPropertyAttribute$CNContactPropertyNotFetchedExceptionName$CNContactRelationsKey$CNContactSocialProfilesKey$CNContactStoreDidChangeNotification$CNContactThumbnailImageDataKey$CNContactTypeKey$CNContactUrlAddressesKey$CNContainerIdentifierKey$CNContainerNameKey$CNContainerTypeKey$CNErrorDomain$CNErrorUserInfoAffectedRecordIdentifiersKey$CNErrorUserInfoAffectedRecordsKey$CNErrorUserInfoKeyPathsKey$CNErrorUserInfoValidationErrorsKey$CNGroupIdentifierKey$CNGroupNameKey$CNInstantMessageAddressServiceKey$CNInstantMessageAddressUsernameKey$CNInstantMessageServiceAIM$CNInstantMessageServiceFacebook$CNInstantMessageServiceGaduGadu$CNInstantMessageServiceGoogleTalk$CNInstantMessageServiceICQ$CNInstantMessageServiceJabber$CNInstantMessageServiceMSN$CNInstantMessageServiceQQ$CNInstantMessageServiceSkype$CNInstantMessageServiceYahoo$CNLabelContactRelationAssistant$CNLabelContactRelationAunt$CNLabelContactRelationAuntFathersBrothersWife$CNLabelContactRelationAuntFathersElderBrothersWife$CNLabelContactRelationAuntFathersElderSister$CNLabelContactRelationAuntFathersSister$CNLabelContactRelationAuntFathersYoungerBrothersWife$CNLabelContactRelationAuntFathersYoungerSister$CNLabelContactRelationAuntMothersBrothersWife$CNLabelContactRelationAuntMothersElderSister$CNLabelContactRelationAuntMothersSister$CNLabelContactRelationAuntMothersYoungerSister$CNLabelContactRelationAuntParentsElderSister$CNLabelContactRelationAuntParentsSister$CNLabelContactRelationAuntParentsYoungerSister$CNLabelContactRelationBoyfriend$CNLabelContactRelationBrother$CNLabelContactRelationBrotherInLaw$CNLabelContactRelationBrotherInLawElderSistersHusband$CNLabelContactRelationBrotherInLawHusbandsBrother$CNLabelContactRelationBrotherInLawHusbandsSistersHusband$CNLabelContactRelationBrotherInLawSistersHusband$CNLabelContactRelationBrotherInLawSpousesBrother$CNLabelContactRelationBrotherInLawWifesBrother$CNLabelContactRelationBrotherInLawWifesSistersHusband$CNLabelContactRelationBrotherInLawYoungerSistersHusband$CNLabelContactRelationChild$CNLabelContactRelationChildInLaw$CNLabelContactRelationCoBrotherInLaw$CNLabelContactRelationCoFatherInLaw$CNLabelContactRelationCoMotherInLaw$CNLabelContactRelationCoParentInLaw$CNLabelContactRelationCoSiblingInLaw$CNLabelContactRelationCoSisterInLaw$CNLabelContactRelationColleague$CNLabelContactRelationCousin$CNLabelContactRelationCousinFathersBrothersDaughter$CNLabelContactRelationCousinFathersBrothersSon$CNLabelContactRelationCousinFathersSistersDaughter$CNLabelContactRelationCousinFathersSistersSon$CNLabelContactRelationCousinGrandparentsSiblingsChild$CNLabelContactRelationCousinGrandparentsSiblingsDaughter$CNLabelContactRelationCousinGrandparentsSiblingsSon$CNLabelContactRelationCousinMothersBrothersDaughter$CNLabelContactRelationCousinMothersBrothersSon$CNLabelContactRelationCousinMothersSistersDaughter$CNLabelContactRelationCousinMothersSistersSon$CNLabelContactRelationCousinOrSiblingsChild$CNLabelContactRelationCousinParentsSiblingsChild$CNLabelContactRelationCousinParentsSiblingsDaughter$CNLabelContactRelationCousinParentsSiblingsSon$CNLabelContactRelationDaughter$CNLabelContactRelationDaughterInLaw$CNLabelContactRelationDaughterInLawOrSisterInLaw$CNLabelContactRelationDaughterInLawOrStepdaughter$CNLabelContactRelationElderBrother$CNLabelContactRelationElderBrotherInLaw$CNLabelContactRelationElderCousin$CNLabelContactRelationElderCousinFathersBrothersDaughter$CNLabelContactRelationElderCousinFathersBrothersSon$CNLabelContactRelationElderCousinFathersSistersDaughter$CNLabelContactRelationElderCousinFathersSistersSon$CNLabelContactRelationElderCousinMothersBrothersDaughter$CNLabelContactRelationElderCousinMothersBrothersSon$CNLabelContactRelationElderCousinMothersSiblingsDaughterOrFathersSistersDaughter$CNLabelContactRelationElderCousinMothersSiblingsSonOrFathersSistersSon$CNLabelContactRelationElderCousinMothersSistersDaughter$CNLabelContactRelationElderCousinMothersSistersSon$CNLabelContactRelationElderCousinParentsSiblingsDaughter$CNLabelContactRelationElderCousinParentsSiblingsSon$CNLabelContactRelationElderSibling$CNLabelContactRelationElderSiblingInLaw$CNLabelContactRelationElderSister$CNLabelContactRelationElderSisterInLaw$CNLabelContactRelationEldestBrother$CNLabelContactRelationEldestSister$CNLabelContactRelationFather$CNLabelContactRelationFatherInLaw$CNLabelContactRelationFatherInLawHusbandsFather$CNLabelContactRelationFatherInLawOrStepfather$CNLabelContactRelationFatherInLawWifesFather$CNLabelContactRelationFemaleCousin$CNLabelContactRelationFemaleFriend$CNLabelContactRelationFemalePartner$CNLabelContactRelationFriend$CNLabelContactRelationGirlfriend$CNLabelContactRelationGirlfriendOrBoyfriend$CNLabelContactRelationGrandaunt$CNLabelContactRelationGrandchild$CNLabelContactRelationGrandchildOrSiblingsChild$CNLabelContactRelationGranddaughter$CNLabelContactRelationGranddaughterDaughtersDaughter$CNLabelContactRelationGranddaughterOrNiece$CNLabelContactRelationGranddaughterSonsDaughter$CNLabelContactRelationGrandfather$CNLabelContactRelationGrandfatherFathersFather$CNLabelContactRelationGrandfatherMothersFather$CNLabelContactRelationGrandmother$CNLabelContactRelationGrandmotherFathersMother$CNLabelContactRelationGrandmotherMothersMother$CNLabelContactRelationGrandnephew$CNLabelContactRelationGrandnephewBrothersGrandson$CNLabelContactRelationGrandnephewSistersGrandson$CNLabelContactRelationGrandniece$CNLabelContactRelationGrandnieceBrothersGranddaughter$CNLabelContactRelationGrandnieceSistersGranddaughter$CNLabelContactRelationGrandparent$CNLabelContactRelationGrandson$CNLabelContactRelationGrandsonDaughtersSon$CNLabelContactRelationGrandsonOrNephew$CNLabelContactRelationGrandsonSonsSon$CNLabelContactRelationGranduncle$CNLabelContactRelationGreatGrandchild$CNLabelContactRelationGreatGrandchildOrSiblingsGrandchild$CNLabelContactRelationGreatGranddaughter$CNLabelContactRelationGreatGrandfather$CNLabelContactRelationGreatGrandmother$CNLabelContactRelationGreatGrandparent$CNLabelContactRelationGreatGrandson$CNLabelContactRelationHusband$CNLabelContactRelationMaleCousin$CNLabelContactRelationMaleFriend$CNLabelContactRelationMalePartner$CNLabelContactRelationManager$CNLabelContactRelationMother$CNLabelContactRelationMotherInLaw$CNLabelContactRelationMotherInLawHusbandsMother$CNLabelContactRelationMotherInLawOrStepmother$CNLabelContactRelationMotherInLawWifesMother$CNLabelContactRelationNephew$CNLabelContactRelationNephewBrothersSon$CNLabelContactRelationNephewBrothersSonOrHusbandsSiblingsSon$CNLabelContactRelationNephewOrCousin$CNLabelContactRelationNephewSistersSon$CNLabelContactRelationNephewSistersSonOrWifesSiblingsSon$CNLabelContactRelationNiece$CNLabelContactRelationNieceBrothersDaughter$CNLabelContactRelationNieceBrothersDaughterOrHusbandsSiblingsDaughter$CNLabelContactRelationNieceOrCousin$CNLabelContactRelationNieceSistersDaughter$CNLabelContactRelationNieceSistersDaughterOrWifesSiblingsDaughter$CNLabelContactRelationParent$CNLabelContactRelationParentInLaw$CNLabelContactRelationParentsElderSibling$CNLabelContactRelationParentsSibling$CNLabelContactRelationParentsSiblingFathersElderSibling$CNLabelContactRelationParentsSiblingFathersSibling$CNLabelContactRelationParentsSiblingFathersYoungerSibling$CNLabelContactRelationParentsSiblingMothersElderSibling$CNLabelContactRelationParentsSiblingMothersSibling$CNLabelContactRelationParentsSiblingMothersYoungerSibling$CNLabelContactRelationParentsYoungerSibling$CNLabelContactRelationPartner$CNLabelContactRelationSibling$CNLabelContactRelationSiblingInLaw$CNLabelContactRelationSiblingsChild$CNLabelContactRelationSister$CNLabelContactRelationSisterInLaw$CNLabelContactRelationSisterInLawBrothersWife$CNLabelContactRelationSisterInLawElderBrothersWife$CNLabelContactRelationSisterInLawHusbandsBrothersWife$CNLabelContactRelationSisterInLawHusbandsSister$CNLabelContactRelationSisterInLawSpousesSister$CNLabelContactRelationSisterInLawWifesBrothersWife$CNLabelContactRelationSisterInLawWifesSister$CNLabelContactRelationSisterInLawYoungerBrothersWife$CNLabelContactRelationSon$CNLabelContactRelationSonInLaw$CNLabelContactRelationSonInLawOrBrotherInLaw$CNLabelContactRelationSonInLawOrStepson$CNLabelContactRelationSpouse$CNLabelContactRelationStepbrother$CNLabelContactRelationStepchild$CNLabelContactRelationStepdaughter$CNLabelContactRelationStepfather$CNLabelContactRelationStepmother$CNLabelContactRelationStepparent$CNLabelContactRelationStepsister$CNLabelContactRelationStepson$CNLabelContactRelationTeacher$CNLabelContactRelationUncle$CNLabelContactRelationUncleFathersBrother$CNLabelContactRelationUncleFathersElderBrother$CNLabelContactRelationUncleFathersElderSistersHusband$CNLabelContactRelationUncleFathersSistersHusband$CNLabelContactRelationUncleFathersYoungerBrother$CNLabelContactRelationUncleFathersYoungerSistersHusband$CNLabelContactRelationUncleMothersBrother$CNLabelContactRelationUncleMothersElderBrother$CNLabelContactRelationUncleMothersSistersHusband$CNLabelContactRelationUncleMothersYoungerBrother$CNLabelContactRelationUncleParentsBrother$CNLabelContactRelationUncleParentsElderBrother$CNLabelContactRelationUncleParentsYoungerBrother$CNLabelContactRelationWife$CNLabelContactRelationYoungerBrother$CNLabelContactRelationYoungerBrotherInLaw$CNLabelContactRelationYoungerCousin$CNLabelContactRelationYoungerCousinFathersBrothersDaughter$CNLabelContactRelationYoungerCousinFathersBrothersSon$CNLabelContactRelationYoungerCousinFathersSistersDaughter$CNLabelContactRelationYoungerCousinFathersSistersSon$CNLabelContactRelationYoungerCousinMothersBrothersDaughter$CNLabelContactRelationYoungerCousinMothersBrothersSon$CNLabelContactRelationYoungerCousinMothersSiblingsDaughterOrFathersSistersDaughter$CNLabelContactRelationYoungerCousinMothersSiblingsSonOrFathersSistersSon$CNLabelContactRelationYoungerCousinMothersSistersDaughter$CNLabelContactRelationYoungerCousinMothersSistersSon$CNLabelContactRelationYoungerCousinParentsSiblingsDaughter$CNLabelContactRelationYoungerCousinParentsSiblingsSon$CNLabelContactRelationYoungerSibling$CNLabelContactRelationYoungerSiblingInLaw$CNLabelContactRelationYoungerSister$CNLabelContactRelationYoungerSisterInLaw$CNLabelContactRelationYoungestBrother$CNLabelContactRelationYoungestSister$CNLabelDateAnniversary$CNLabelEmailiCloud$CNLabelHome$CNLabelOther$CNLabelPhoneNumberHomeFax$CNLabelPhoneNumberMain$CNLabelPhoneNumberMobile$CNLabelPhoneNumberOtherFax$CNLabelPhoneNumberPager$CNLabelPhoneNumberWorkFax$CNLabelPhoneNumberAppleWatch$CNLabelPhoneNumberiPhone$CNLabelSchool$CNLabelURLAddressHomePage$CNLabelWork$CNPostalAddressCityKey$CNPostalAddressCountryKey$CNPostalAddressISOCountryCodeKey$CNPostalAddressLocalizedPropertyNameAttribute$CNPostalAddressPostalCodeKey$CNPostalAddressPropertyAttribute$CNPostalAddressStateKey$CNPostalAddressStreetKey$CNPostalAddressSubAdministrativeAreaKey$CNPostalAddressSubLocalityKey$CNSocialProfileServiceFacebook$CNSocialProfileServiceFlickr$CNSocialProfileServiceGameCenter$CNSocialProfileServiceKey$CNSocialProfileServiceLinkedIn$CNSocialProfileServiceMySpace$CNSocialProfileServiceSinaWeibo$CNSocialProfileServiceTencentWeibo$CNSocialProfileServiceTwitter$CNSocialProfileServiceYelp$CNSocialProfileURLStringKey$CNSocialProfileUserIdentifierKey$CNSocialProfileUsernameKey$"""
enums = """$CNErrorCodeChangeHistoryInvalidFetchRequest@605$CNAuthorizationStatusAuthorized@3$CNAuthorizationStatusDenied@2$CNAuthorizationStatusNotDetermined@0$CNAuthorizationStatusRestricted@1$CNContactDisplayNameOrderFamilyNameFirst@2$CNContactDisplayNameOrderGivenNameFirst@1$CNContactDisplayNameOrderUserDefault@0$CNContactFormatterStyleFullName@0$CNContactFormatterStylePhoneticFullName@1$CNContactSortOrderFamilyName@3$CNContactSortOrderGivenName@2$CNContactSortOrderNone@0$CNContactSortOrderUserDefault@1$CNContactTypeOrganization@1$CNContactTypePerson@0$CNContainerTypeCardDAV@3$CNContainerTypeExchange@2$CNContainerTypeLocal@1$CNContainerTypeUnassigned@0$CNEntityTypeContacts@0$CNErrorCodeAuthorizationDenied@100$CNErrorCodeChangeHistoryExpired@603$CNErrorCodeChangeHistoryInvalidAnchor@604$CNErrorCodeClientIdentifierCollision@602$CNErrorCodeClientIdentifierDoesNotExist@601$CNErrorCodeClientIdentifierInvalid@600$CNErrorCodeCommunicationError@1$CNErrorCodeContainmentCycle@202$CNErrorCodeContainmentScope@203$CNErrorCodeDataAccessError@2$CNErrorCodeFeatureDisabledByUser@103$CNErrorCodeInsertedRecordAlreadyExists@201$CNErrorCodeNoAccessableWritableContainers@101$CNErrorCodeParentContainerNotWritable@207$CNErrorCodeParentRecordDoesNotExist@204$CNErrorCodePolicyViolation@500$CNErrorCodePredicateInvalid@400$CNErrorCodeRecordDoesNotExist@200$CNErrorCodeRecordIdentifierInvalid@205$CNErrorCodeRecordNotWritable@206$CNErrorCodeUnauthorizedKeys@102$CNErrorCodeVCardMalformed@700$CNErrorCodeVCardSummarizationError@701$CNErrorCodeValidationConfigurationError@302$CNErrorCodeValidationMultipleErrors@300$CNErrorCodeValidationTypeMismatch@301$CNPostalAddressFormatterStyleMailingAddress@0$"""
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(
        b"CNChangeHistoryFetchRequest",
        b"includeGroupChanges",
        {"retval": {"type": b"Z"}},
    )
    r(b"CNChangeHistoryFetchRequest", b"mutableObjects", {"retval": {"type": b"Z"}})
    r(
        b"CNChangeHistoryFetchRequest",
        b"setIncludeGroupChanges:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(
        b"CNChangeHistoryFetchRequest",
        b"setMutableObjects:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(
        b"CNChangeHistoryFetchRequest",
        b"setShouldUnifyResults:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(b"CNChangeHistoryFetchRequest", b"shouldUnifyResults", {"retval": {"type": b"Z"}})
    r(b"CNContact", b"areKeysAvailable:", {"retval": {"type": "Z"}})
    r(b"CNContact", b"imageDataAvailable", {"retval": {"type": b"Z"}})
    r(b"CNContact", b"isKeyAvailable:", {"retval": {"type": "Z"}})
    r(b"CNContact", b"isUnifiedWithContactWithIdentifier:", {"retval": {"type": "Z"}})
    r(b"CNContactFetchRequest", b"mutableObjects", {"retval": {"type": "Z"}})
    r(
        b"CNContactFetchRequest",
        b"setMutableObjects:",
        {"arguments": {2: {"type": "Z"}}},
    )
    r(b"CNContactFetchRequest", b"setUnifyResults:", {"arguments": {2: {"type": "Z"}}})
    r(b"CNContactFetchRequest", b"unifyResults", {"retval": {"type": "Z"}})
    r(
        b"CNContactStore",
        b"containersMatchingPredicate:error:",
        {"arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"CNContactStore",
        b"enumerateContactsWithFetchRequest:error:usingBlock:",
        {
            "retval": {"type": "Z"},
            "arguments": {
                3: {"type_modifier": b"o"},
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"o^Z"},
                        },
                    }
                },
            },
        },
    )
    r(
        b"CNContactStore",
        b"enumeratorForChangeHistoryFetchRequest:error:",
        {"arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"CNContactStore",
        b"enumeratorForContactFetchRequest:error:",
        {"arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"CNContactStore",
        b"executeSaveRequest:error:",
        {"retval": {"type": "Z"}, "arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"CNContactStore",
        b"groupsMatchingPredicate:error:",
        {"arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"CNContactStore",
        b"requestAccessForEntityType:completionHandler:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"Z"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"CNContactStore",
        b"unifiedContactWithIdentifier:keysToFetch:error:",
        {"arguments": {4: {"type_modifier": b"o"}}},
    )
    r(
        b"CNContactStore",
        b"unifiedContactsMatchingPredicate:keysToFetch:error:",
        {"arguments": {4: {"type_modifier": b"o"}}},
    )
    r(
        b"CNContactStore",
        b"unifiedMeContactWithKeysToFetch:error:",
        {"arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"CNContactVCardSerialization",
        b"contactsWithData:error:",
        {"arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"CNContactVCardSerialization",
        b"dataWithContacts:error:",
        {"arguments": {3: {"type_modifier": b"o"}}},
    )
    r(b"CNPhoneNumber", b"init", {"deprecated": 1013})
    r(b"CNPhoneNumber", b"new", {"deprecated": 1013})
    r(
        b"NSObject",
        b"visitAddContactEvent:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"visitAddGroupEvent:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"visitAddMemberToGroupEvent:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"visitAddSubgroupToGroupEvent:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"visitDeleteContactEvent:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"visitDeleteGroupEvent:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"visitDropEverythingEvent:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"visitRemoveMemberFromGroupEvent:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"visitRemoveSubgroupFromGroupEvent:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"visitUpdateContactEvent:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"visitUpdateGroupEvent:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
