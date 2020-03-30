from lackey import *
import MonitorMgmt as monitor
import Comment as comment
import Case as case
import tools.wTimes as wTimes
import tools.config as config
import Pr_Reflow as reflow
import Pr_VerifyPrism as verifyPrism
import Pr_PrismSearch as prismSearch
import getCaseNumber as getCaseNumber

SettingsMaster.MoveMouseDelay = 0
w1, w2, w3, w4, w5, w10, w20, w30, w40, w50, w60, w100, wh = wTimes.times
modNm = config.modNameRoot + "PrismX: "
fiberProducts = ["BCE",
                 "EPL",
                 "BCE EVPL",
                 "Channel Insertion",
                 "Cloud Services",
                 "Cloud Solutions",
                 "Dark Fiber",
                 "Enterprise Trunking(PRI)",
                 "Enterprise Trunking(SIP)",
                 "EPL",
                 "EP-LAN",
                 "Ethernet (Fiber)",
                 "FIA/Ethernet",
                 "Ethernet Video Transport-Direct to TWC",
                 "Ethernet Video Transport-Other Video Transport",
                 "Ethernet Video Transport-PEG to TWC",
                 "EVPL",
                 "FIA",
                 "Fiber Connect Plus",
                 "Channel Insertion/Deletion",
                 "Hosted Communications",
                 "Managed WiFi",
                 "Managed WiFi(GPNS Solution)",
                 "Metro Ethernet",
                 "Fiber Connect (Legacy Pro:I/ClearQAM)",
                 "Transport EPL",
                 "Voice"]

fiberCoax = ["Coax", "Coax/Fiber", "Fiber"]
timesRefresh = 5


def main():
    wait(w1)
    type(Key.HOME, KeyModifier.CTRL)
    wait(w1)
    monitor.doFSearch("Site Survey URL")
    wait(w1)

    # caseNumber = getCaseNumber()

    specificComments = " "
    lastCopy = ""

    if not exists("SiteSurveyURL1242.png"):
        specificComments = specificComments + "- Wrong format - there is no Site Survey link "
        type(Key.HOME, KeyModifier.CTRL)
        wait(w1)
        comment.addNewCommentInCase(config.commentPrismCore + specificComments)
        case.changeStatusInCase(config.ONHOLD)
        return

    click(Pattern("SiteSurveyURL1242.png").targetOffset(70, 0))

    try:

        wait("SiteSurveyDetail309.png", w10)
        wait(1)

    except:

        if not exists("SiteSurveyDetail309.png"):
            type("w", KeyModifier.CTRL)
            wait(w1)
            specificComments = specificComments + "- No Site Survey Detail Page "
            comment.addNewCommentInCase(config.commentPrismCore + specificComments)
            case.changeStatusInCase(config.ONHOLD)
            return

    prismFailed = False

    print(modNm + "Test 2. ++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(modNm + "Test 2. The field PRISM Enabled on the DFOR is checked")
    type(Key.HOME, KeyModifier.CTRL)
    wait(w1)
    monitor.doFSearch("Prism Enabled")
    wait(w2)

    if not exists("PRISMEnabled446.png"):
        click("AvXDown447.png")

    dragDrop(Pattern("PRISMEnabled446.png").targetOffset(84, 2), Pattern("PRISMEnabled446.png").targetOffset(55, 2))
    type("c", KeyModifier.CTRL)
    prismEnabled = getClipboard()

    print(modNm + "prismEnabled: {}; bool(prismEnabled): {}".format(prismEnabled, bool(prismEnabled)))

    if prismEnabled == "Not Checked":
        print(modNm + "Prism is not enabled, comment and put the case on-hold")
        specificComments = specificComments + "- Prism is NOT enabled "
        prismFailed = True

    else:
        print(modNm + "Prism is enabled - CORRECT, continue ")
        print(modNm + "IN Site Survey")

    lastCopy = prismEnabled

    print(modNm + " Test 3. ++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(modNm + " Test 3. The 'Spectrum Business Unit' field is populated with 'Enterprise'")
    print(modNm + " Test 3.: Possible Values for sBU: Enterprise, SMB, None")
    type(Key.HOME, KeyModifier.CTRL)
    wait(w1)
    monitor.doFSearch("Spectrum Business Unit")
    wait(w1)
    doubleClick(Pattern("SpectrumBusinessUnit1255.png").targetOffset(115, -1))

    if exists("sBUEnterprise1231.png"):
        print(modNm + " sBU is not empty")
        print(modNm + " The Spectrum Business Unit field is populated with 'Enterprise' - CORRECT ")

    else:
        print(modNm + " sBU does not exist or is equal to SMB - INCORRECT")
        print(modNm + " The Spectrum Business Unit field is NOT populated with 'Enterprise', comment and put case on-hold ")
        specificComments = specificComments + "- Spectrum Business Unit is NOT Enterprise "
        prismFailed = True

    click("SpectrumBusinessUnit1255.png")
    wait(w1)

    print(modNm + " Test 4: ++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(modNm + " Test 4: The Survey For These Products field is populated with Fiber-related products")

    type(Key.HOME, KeyModifier.CTRL)
    wait(w1)
    monitor.doFSearch("Survey For These Products")
    wait(w2)

    found = False
    while not found:
        if not exists("SurveyForTheseProduct119.png"):
            type(Key.ENTER)
            wait(w1)

        else:
            print("Survey For these Products - FOUND")
            found = True

    click("SurveyForTheseProduct119.png")
    dragDrop(Pattern("SurveyForTheseProduct119.png").targetOffset(90, 2),
             Pattern("SurveyForTheseProduct119.png").targetOffset(376, 2))
    type("c", KeyModifier.CTRL)
    products = getClipboard()

    products = monitor.splitAndRemoveLeadBlanks(products, ";")

    print(modNm + " Survey For These Products - product: ", products)
    fiber = False
    for prod in products:

        if prod in fiberProducts:
            print(modNm + " fiber product found: {}".format(prod))
            fiber = True

    if not fiber:
        print(modNm + " The Survey For These Products field is populated "
                      "with Fiber-related products, comment and put case on-hold ")
        specificComments = specificComments + "’Survey For These Products’ field is NOT a Fiber-related product"
        prismFailed = True

    else:
        print(modNm + " The Survey For These Products field is populated with a Fiber-related product - CORRECT")

    lastCopy = products

    print(modNm + " Test 5: ++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(modNm + " Test 5: The Survey for Plant Type field is populated with either"
                  " 1) Coax, 2) Coax/Fiber, or 3) Fiber ")

    type(Key.HOME, KeyModifier.CTRL)
    wait(w1)
    monitor.doFSearch("Survey for Plant Type")
    wait(w2)
    click("SurveyforPlantType129.png")
    dragDrop(Pattern("SurveyforPlantType129.png").targetOffset(75, 2),
             Pattern("SurveyforPlantType129.png").targetOffset(364, 3))
    type("c", KeyModifier.CTRL)

    products = getClipboard()

    products = monitor.splitAndRemoveLeadBlanks(products, ";")

    print(modNm + " Survey for Plant Type - product: ", products)
    fiber = False
    for prod in products:

        if prod in fiberCoax:
            print(modNm + " fiberCoax product found: {}".format(prod))
            fiber = True

    if not fiber:
        print(modNm + " The Survey for Plant Type field is NOT populated with either"
              " 1) Coax, 2) Coax/Fiber, or 3) Fiber, comment and put case on-hold ")
        specificComments = specificComments + "- The Survey for Plant Type field is NOT populated with either"
        " 1) Coax, 2) Coax/Fiber, or 3) "
        prismFailed = True

    else:
        print(modNm + " The Survey for Plant Type field is populated with either"
              " 1) Coax, 2) Coax/Fiber, or 3) Fiber - CORRECT")

    lastCopy = products

    print(modNm + " Test 6: ++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(modNm + " Test 6: The Building field is populated and contains a DFOR - Division Field Office Routing")

    type(Key.HOME, KeyModifier.CTRL)
    wait(w1)
    monitor.doFSearch("Information on the Building Assigned to this Service Location")

    dfor1 = ""
    address = ""

    click(Pattern("InformationonBuildingAssigned212.png").targetOffset(10, 23))
    wait(w1)

    dragDrop(Pattern("InformationonBuildingAssigned212.png").targetOffset(600, 22),
             Pattern("InformationonBuildingAssigned212.png").targetOffset(77, 23))
    type("c", KeyModifier.CTRL)
    address = getClipboard()

    print(modNm + " address: ", address)
    print(modNm + " address @ Information on the Building Assigned to this Service Location is populated - CORRECT ")

    if not bool(address) or address == lastCopy:
        print(modNm + " address @ Information on the Building Assigned to this Service "
                      "Location is None, what to do next?")
        specificComments = specificComments + "- Building is missing an address "
        type("w", KeyModifier.CTRL)
        wait(w1)
        comment.addNewCommentInCase(config.commentPrismCore + specificComments)
        case.changeStatusInCase(config.ONHOLD)
        prismFailed = True
        return

    else:
        click(Pattern("InformationonBuildingAssigned212.png").targetOffset(167, 24))
        wait("BuildingDetail427.png", w30)
        wait(w1)

    lastCopy = address

    print(modNm + " IN Building")
    type(Key.HOME, KeyModifier.CTRL)
    wait(w1)
    monitor.doFSearch("Division Field Office Routing")
    wait(w1)

    doubleClick(Pattern("DivisionFieldOfficeRouting1246.png").targetOffset(160, 2))
    wait(w1)
    type("c", KeyModifier.CTRL)
    wait(w1)
    dfor1 = getClipboard()
    print(modNm + " dfor1: {}".format(dfor1))

    if not bool(dfor1) and exists("Routing_DFOR_Empty103.png") or dfor1 == lastCopy:
        print(modNm + " Building is NOT populated with ‘DFOR’ - INCORRECT ")
        print(modNm + " not bool(dfor1): {}".format(not bool(dfor1)))
        specificComments = specificComments + "- Building is NOT populated with ‘DFOR(-1)’ "
        prismFailed = True

    elif bool(dfor1):
        print(modNm + " Building is populated with ‘DFOR’ - CORRECT ")
        # type("c", KeyModifier.CTRL)
        # wait(w1)
        # dfor1 = getClipboard()
        print(modNm + " dfor1: {}".format(dfor1))


    else:
        print(modNm + " Test 6: could not identify dfor1, set prismFailed = True, comment it")
        specificComments = specificComments + "- The system failed to identify value for ‘DFOR(-1)’ "
        prismFailed = True

    lastCopy = dfor1

    print(modNm + " go back to Site Survey")
    type(Key.LEFT, KeyModifier.ALT)
    wait(w1)

    print(modNm + " Test 7: T++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(modNm + " Test 7: The Service Location (SL) DFOR is populated and is the same as the one assigned"
                  " to the Building")

    print(modNm + " IN Site Survey")
    type(Key.HOME, KeyModifier.CTRL)
    wait(w1)
    monitor.doFSearch("Opportunity Service Location")

    click(Pattern("OpportunityServiceLocation436.png").targetOffset(130, 1))
    wait(w1)
    wait("OpportunityServiceLocationDetail448.png", w30)
    print("P: IN Opportunity Service Location")
    type(Key.HOME, KeyModifier.CTRL)
    wait(w1)
    click(Pattern("ServiceLocation452.png").similar(0.89).targetOffset(120, 0))

    wait("AccountDetail453.png", w30)
    wait(w1)
    print(modNm + " IN Account")

    type(Key.HOME, KeyModifier.CTRL)
    monitor.doFSearch("Related Building and ZIP Code Routing Information")
    wait(w1)
    monitor.doFSearch("Division Field Office Routing")
    wait(w1)
    doubleClick(Pattern("DivisionFieldOfficeRouting1246.png").targetOffset(160, 2))
    wait(w1)
    type("c", KeyModifier.CTRL)
    wait(w1)
    dfor2 = ""

    dfor2 = getClipboard()
    print(modNm + " dfor2: {}".format(dfor2))

    if not bool(dfor2) and exists("Routing_DFOR_Empty103.png"):  # or lastCopy == dfor2:
        print(modNm + " Building is NOT populated with ‘SL DFOR - 2’ - INCORRECT ")
        print(modNm + " not bool(dfor2): {}".format(not bool(dfor2)))
        specificComments = specificComments + "- Building is NOT populated with ‘SL DFOR(-2)’ "
        prismFailed = True

    elif bool(dfor2):
        print(modNm + " Building is populated with ‘SL DFOR (-2)’ - CORRECT ")
        print(modNm + " dfor2: {}".format(dfor2))

    else:
        print(modNm + " Test 7: could not identify dfor2, set prismFailed = True, comment it")
        specificComments = specificComments + "- The system failed to identify value for ‘SL DFOR(-2)’ "
        prismFailed = True

    print("P: dfor1: {}  ?== dfor2: {} ".format(dfor1, dfor2))
    lastCopy = dfor2

    if dfor1 != dfor2 and dfor1 != "" and dfor2 != "":
        print("P: Building DFOR (-1) and SL DFOR (-2) are NOT equal, comment it and put case on-hold ")
        specificComments = specificComments + "- DFOR(-1) NOT equal to SL DFOR(-2) "
        prismFailed = True

    else:
        print("P: dfor1 and dfor2 are equal or dfor1 is NOT None - CORRECT, continue")

    type(Key.ESC)
    type(Key.LEFT, KeyModifier.ALT)
    type(Key.LEFT, KeyModifier.ALT)
    wait(w1)
    print(modNm + " IN Site Survey")
    wait("SiteSurveyDetail445.png", w30)

    type(Key.HOME, KeyModifier.CTRL)
    wait(w1)

    if prismFailed:
        print(modNm + " prismFailed is: {} comment and put status to: {} ".format(prismFailed, config.ONHOLD))
        print(modNm + " Full specific comments: " + config.commentPrismCore + specificComments)
        type("w", KeyModifier.CTRL)
        wait(w1)
        comment.addNewCommentInCase(config.commentPrismCore + specificComments)
        case.changeStatusInCase(config.ONHOLD)
        return

    print(modNm + " Test 11. ++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(modNm + " Test 11. The correct Related Contact should be populated in the 'Customer Technical "
          + "Contact Name' field of the 'Additional Contact Information' Section")

    type(Key.HOME, KeyModifier.CTRL)
    wait(w1)
    monitor.doFSearch("Customer Technical Contact Name")
    type(Key.ENTER)
    wait("CustomerTechnicalContactName449.png", w10)
    wait(w1)
    dragDrop(Pattern("CustomerTechnicalContactName449.png").targetOffset(620, 0),
             Pattern("CustomerTechnicalContactName449.png").targetOffset(102, -1))
    type("c", KeyModifier.CTRL)
    nameTechContact = ""
    nameTechContact = getClipboard()
    print(modNm + " nameTechContact: {}".format(nameTechContact))

    if not bool(nameTechContact) or lastCopy == nameTechContact:  # == "" or nameTechContact is None:

        print(modNm + " Customer Technical Contact Name is NOT populated, comment it and put case on-hold ")
        type("w", KeyModifier.CTRL)
        wait(w1)
        comment.addNewCommentInCase(config.commentPrismCore + "- DFOR criteria failed ")
        case.changeStatusInCase(config.ONHOLD)
        return

    else:
        print(modNm + " CORRECT - Customer Technical Contact Name is populated, continue")

    lastCopy = nameTechContact
    click(Pattern("CustomerTechnicalContactName449.png").targetOffset(110, 0))
    wait("ContactDetail213.png", w10)
    wait(w1)
    print(modNm + " IN Contact")
    doubleClick(Pattern("Phone214.png").targetOffset(135, 1))
    wait(w1)
    type("c", KeyModifier.CTRL)
    click("Phone214.png")
    phone = ""
    phone = getClipboard()
    print(modNm + " phone: {}".format(phone))

    if not bool(phone) or lastCopy == phone:  # is None or phone == "":

        print("P: Customer Technical Contact Phone is NOT populated, comment it and put case on-hold ")
        type("w", KeyModifier.CTRL)
        wait(w1)
        comment.addNewCommentInCase(config.commentPrismCore + "- Customer Technical Contact Phone is NOT populated ")
        case.changeStatusInCase(config.ONHOLD)
        return

    else:
        print("P: CORRECT - Customer Technical Contact Phone is populated")

    lastCopy = phone
    type(Key.LEFT, KeyModifier.ALT)
    print(modNm + " Back to Site Survey")

    print(modNm + " Test 1. ++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(modNm + " Test 1. There is no SF-DOCK Integration Record assigned to the SSO "
          + "by verifying that this section is blank on the SSO")
    print(modNm + " IN Site Survey")

    type(Key.HOME, KeyModifier.CTRL)
    wait(w1)

    monitor.doFSearch("SF-DOCK Integration Record")

    if exists("SFDOCKlntegrationRecord226.png"):
        print(modNm + "Found SFDOCKlntegrationRecord226.png - Button")
        click("SFDOCKlntegrationRecord226.png")

    else:
        print(modNm + " type CT+Home again")
        type(Key.HOME, KeyModifier.CTRL)
        wait(w1)
        click("SFDOCKlntegrationRecord226.png")
        
    records = ""
    tentFound = False
    loopTent = 0
    loopTentMax = 8
    while not tentFound and loopTent < loopTentMax: 
        if exists("Tent_SFDOCK1202.png"):
            print(modNm + "Tent-SF-Dock found at loop: {}".format(loopTent))
            dragDrop(Pattern("Tent_SFDOCK1202.png").targetOffset(-43,28), Pattern("Tent_SFDOCK1202.png").targetOffset(102,29))
            type("c", KeyModifier.CTRL)
            records = getClipboard()
            tentFound = True

        else:
            print(modNm + "Tent-SF-Dock NOT found at loop: {}".format(loopTent))
            type(Key.ENTER)
            wait(w1)
            loopTent += 1

    if records == "No records to display":

        print(modNm + " test passed - no record in SF-DOCK Integration Record ")

    else:

        print(modNm + " delete the SF-DOCK Integration Record")
        click(Pattern("ActionEditDel231.png").targetOffset(16, 27))
        wait(w1)
        click("OKBtnBlue430.png")
        wait("SiteSurveyDetail309.png", w30)
        wait(w1)

    lastCopy = records

    print(modNm + " CORRECT - Prism is enabled, continue")
    print(modNm + " ++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(modNm + " Test 9: If the Advanced Services Product field is checked")
    print(modNm + " IN Site Survey")

    type(Key.HOME, KeyModifier.CTRL)
    wait(w1)
    monitor.doFSearch("Advanced Services Product")
    wait("AdvancedServicesProduct1249.png", w10)
    wait(w1)
    dragDrop(Pattern("AdvancedServicesProduct1249.png").targetOffset(90, 3),
             Pattern("AdvancedServicesProduct1249.png").targetOffset(110, 3))
    type("c", KeyModifier.CTRL)
    aSP = getClipboard()
    date = ""

    if aSP != "Checked" or lastCopy == aSP:
        print(modNm + " Advanced Services Product NOT checked, comment, abort")
        type("w", KeyModifier.CTRL)
        wait(w1)
        comment.addNewCommentInCase(config.commentPrismCore + "- Advanced Services Product NOT checked ")
        case.changeStatusInCase(config.ONHOLD)
        return

    else:
        print(modNm + " Advanced Services Product Checked")
        type(Key.HOME, KeyModifier.CTRL)
        wait(w1)
        type("f", KeyModifier.CTRL)
        type("Construction Costing Requested")
        wait("ConstructionCostingRrequested116.png", w10)
        wait(w1)

        click(Pattern("ConstructionCostingRrequested116.png").targetOffset(220, 0))
        wait(w1)
        dragDrop(Pattern("ConstructionCostingRrequested116.png").targetOffset(220, 0),
                 Pattern("ConstructionCostingRrequested116.png").targetOffset(100, 0))

        if exists(Pattern("ConstructionCostingRequestedEmpty1223.png").similar(0.91)):
            print(modNm + " Construction Costing Requested: date is NOT populated, populate it with today")
            doubleClick(Pattern("ConstructionCostingRrequested116.png").targetOffset(115, 0))
            wait(w1)
            click("Today149.png")
            wait(w1)
            click("ConstructionCostingRrequested116.png")
            wait(w1)
            type(Key.HOME, KeyModifier.CTRL)
            wait(w1)
            click("Save415.png")
            wait(w5)

        else:
            print(modNm + " Construction Costing Requested: date is populated, continue")
            type("c", KeyModifier.CTRL)
            cCRdate = getClipboard()
            print(modNm + " cCRdate: {}".format(cCRdate))

    # popup(cCRdate)
    lastCopy = aSP

    print(modNm + " Test 10. ++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(modNm + " Test 10. Cross Road field should be populated")
    print(modNm + " IN Site Survey")

    type(Key.HOME, KeyModifier.CTRL)
    print(modNm + " IN Site Survey")
    wait(w1)
    monitor.doFSearch("Cross Road")
    wait("CrossRoad121.png", w10)
    wait(w1)
    crossRoad = ""

    dragDrop(Pattern("CrossRoad121.png").targetOffset(48, 0), Pattern("CrossRoad121.png").targetOffset(239, 2))
    type("c", KeyModifier.CTRL)
    crossRoad = getClipboard()
    print(modNm + " crossRoad: {}".format(crossRoad))
    click("CrossRoad121.png")

    if not bool(crossRoad) or lastCopy == crossRoad:
        print(modNm + " Cross Road not populated, populated with anything")
        doubleClick(Pattern("CrossRoad121.png").targetOffset(56, 0))
        wait(w1)
        type("na")
        click("CrossRoad121.png")
        wait(w1)
        click("Save415.png")
        wait(w5)

    lastCopy = crossRoad

    print(modNm + " Test 12. ++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(modNm + " Test 12. SCCE Field - is it populated? ")
    print(modNm + " IN Site Survey")

    type(Key.HOME, KeyModifier.CTRL)
    wait(w1)
    monitor.doFSearch("SCCE Requested Date")
    wait(w1)
    scceReqDate = ""

    # dragDrop(Pattern("SCCERequestedDate149-2.png").targetOffset(65, 1),
    # Pattern("SCCERequestedDate149-2.png").targetOffset(205, 0))
    doubleClick(Pattern("SCCERequestedDate149-2.png").targetOffset(230, 0))
    wait(w1)
    type("c", KeyModifier.CTRL)

    scceReqDate: object = getClipboard()
    print(modNm + " " + "scceReqDate: {}".format(scceReqDate))
    click("SCCERequestedDate149-2.png")
    wait(w1)

    if not bool(scceReqDate) and exists("SCCEReqDateEmpty121.png") or lastCopy == scceReqDate:

        print(modNm + " REFLOW Prism Trigger - below")

        reflow.main()

        print(modNm + " End of Reflow")

        for i in range(timesRefresh):
            type(Key.F5)
            wait(w5)

        prismPopulated, newPrismId = verifyPrism.main()

        type("w", KeyModifier.CTRL)
        wait(w1)

        if prismPopulated:
            print(modNm + " Prism populated after reflow")
            comment.addNewCommentInCase(config.commentPrismPopulated + str(newPrismId))
            case.changeStatusInCase(config.CLOSE)

        else:
            print(modNm + " Prism is NOT populated after reflow")
            comment.addNewCommentInCase(config.commentPrismIntReflowFailed)
            case.changeStatusInCase(config.ONHOLD)

    elif bool(scceReqDate):

        print(modNm + " SCCE Requested Date is populated, go to Prism. Current Prism Id: ")
        print(modNm + " scceReqDate: {} is populated".format(scceReqDate))
        print(modNm + " IN Site Survey")

        wait(w1)
        type(Key.HOME, KeyModifier.CTRL)
        wait(w1)
        print(modNm + " copy Site Survey number")
        dragDrop(Pattern("SiteSurveyLogo422.png").targetOffset(21,2), Pattern("SiteSurveyLogo422.png").targetOffset(134,0))
        wait(w1)
        type("c", KeyModifier.CTRL)
        wait(w1)
        siteSurveyNo = getClipboard()
        print(modNm + " Site Survey #: ", siteSurveyNo)

        print(modNm + " Go to Prism")

        success, prismId = prismSearch.main(siteSurveyNo)

        # comment.addNewCommentInCase(
        #     "The request meets validation criteria, is ready to go to PRISM, site survey number: {}".format(
        #         siteSurveyNo))
        # case.changeStatusInCase(config.ONHOLD)
        # print(modNm + " EOProgram")
        print("siteSurveyNo: {}; prismid: {}".format(siteSurveyNo, prismId))
        # popup("siteSurveyNo: {}; prismid: {}".format(siteSurveyNo, prismId))

        if success and prismId != config.prismIdDefaultValue:
            type(Key.HOME, KeyModifier.CTRL)
            wait(w1)
            monitor.doFSearch("prism id")
            doubleClick(Pattern("PRISMId343.png").targetOffset(110, 0))
            type(prismId)
            wait(w1)
            click("PRISMId343.png")
            type(Key.HOME, KeyModifier.CTRL)
            wait(w1)
            # popup(prismId)
            click("Save415.png")
            wait(w1)
            wait("EditDeleteBtns1247.png", w30)
            wait(w1)
            click("SiteSurveyLogo422.png")

            type("w", KeyModifier.CTRL)
            wait(w1)
            type(Key.HOME, KeyModifier.CTRL)
            wait(w1)

            print(modNm + "IN Case")

            comment.addNewCommentInCase(
                config.commentPrismCore + "- Job already created in Prism - Prism is populated ")
            case.changeStatusInCase(config.CLOSE)

        elif success and prismId == config.prismIdDefaultValue:
            print(modNm + "multiple prism ids")
            type("w", KeyModifier.CTRL)
            wait(w1)
            type(Key.HOME, KeyModifier.CTRL)
            wait(w1)
            comment.addNewCommentInCase(config.commentPrismCore + "There are multiple prism ids")
            case.changeStatusInCase(config.ONHOLD)

        elif not success:
            type("w", KeyModifier.CTRL)
            wait(w1)
            comment.addNewCommentInCase(config.commentPrismCore + "- Prism integration failed ")
            case.changeStatusInCase(config.ONHOLD)

    else:
        print(modNm + " SCCE Req Date is NOT read properly, comment and change status to ON-HOLD")
        comment.addNewCommentInCase("Case processing aborted due to technical reasons")
        case.changeStatusInCase(config.ONHOLD)


main()
