from lackey import *
import MonitorMgmt as monitor
import Comment as comment
import Case as case
import tools.wTimes as wTimes
import tools.config as config

SettingsMaster.MoveMouseDelay = 0
w1, w2, w3, w4, w5, w10, w20, w30, w40, w50, w60, w100, wh = wTimes.times
modNm = config.modNameRoot + "SEAltify: "

def main():
    wait(1)
    click("CaseDetail1005.png")
    wait(w1)
    if exists("0nBehalfofUser116.png"):
        click(Pattern("0nBehalfofUser116.png").targetOffset(90,1))
    else:
        type("f", KeyModifier.CTRL)
        wait(w1)
        type("On Behalf of User")
        wait(w1)
        click(Pattern("OnBehalfofUser1.png").targetOffset(90,-1))             #(Pattern("OnBehalfofUser.png").targetOffset(88,0))

    print(modNm + "Done On Behalf...")
    wait("ChatterPeople.png", w5)
    wait(1)
    click(Pattern("FollowBtn.png").targetOffset(32,0))
    wait(1)
    click("UserDetailDropDown.png")
    wait(1)
    wait("UserDetail.png", w30)
    wait(w5)

    print(modNm + "addPermissions - START+++++++++++++++")
    click("Euser400.png")
    click(Pattern("PermissionSetAssignments.png").similar(0.86))
    wait(1)
    click(Pattern("PermissionSetAssEditAssign.png").similar(0.78).targetOffset(211,-2))
    wait("Addwlemove.png",w20)

    wait(w2)
    #click("AvailablePerx.png")
    #App.focus("Chrome")
    wait(w1)
    print(modNm + "Permission Set Assignment page++++++++++++")
    aps = find(Pattern("AvailablePer1210-2.png").similar(0.81))
    reg = Region(aps.getX() - 75, aps.getY() + 26, 285, 168)
    reg.highlight(3)

    found = False
    type("f", KeyModifier.CTRL)
    type("Altify Call Planner Permission Set")
    if reg.exists("AltifyCallPl1212-1.png"):
        wait(w1)
        reg.click("AltifyCallPl1212-1.png")
        wait(w1)
        click("AddBtn-1.png")
        found = True
        print(modNm + "Altify Call Planner Permission Set FOUND")
        wait(w1)
    #reg.hover()
    type("f", KeyModifier.CTRL)
    type("Altify Max User")
    if reg.exists("AltifvMaxUse1215-1.png"):
        wait(w1)
        reg.click("AltifvMaxUse1215-1.png")
        click("AddBtn-1.png")
        found = True
        wait(w1)
        print(modNm + "Altify Max User FOUND")

    #reg.hover()
    #reg.click()
    wait(w2)
    click("AvailablePer258.png")
    wait(w1)
    type("f", KeyModifier.CTRL)
    wait(w1)
    type("Dealmaker Permission Set")
    wait(w2)
    if reg.exists("set413.png"):
        #dps = find("set413.png")
        #if reg.exists("DealmakerPerAP152.png") and !reg.exists("DealmakerPerAdm156.png") and reg.exists("DealmakerPerOM158.png") :
        wait(w1)
        reg.click(Pattern("set413.png").targetOffset(-80,2))
        wait(w1)
        click("AddBtn-1.png")
        found = True
        wait(w1)
        print(modNm + "Dealermaker Permission Set Blue found")

    type("f", KeyModifier.CTRL)
    type("Dealmaker Permission Set - Align User")
    if reg.exists("DealmakerPer1227.png"):
        wait(w1)
        reg.click("DealmakerPer1227.png")
        wait(w2)
        click("AddBtn-1.png")
        found = True
        wait(w1)
        print(modNm + "Dealermaker Per- Align User - FOUND")

    wait(w1)
    if found:
        click("Save340-1.png")
    else:
        click("Cancel1238-1.png")

    wait(w2)
    wait("UserDetail455.png",w30)
    wait(w2)

    print(modNm + "addPermissions - End===============================")

    #packages = ["ManageLicensesAltMax-1.png", "ManageLicensesAltConversationMgr-1.png", "ManageLicensesAltAccMgr-1.png","ManageLicensesAltOppMgr-1.png", "ManageLicensesAltSalesProcMgr.png", "ManageLicensesDealmaker.png"]

    print(modNm + "addPackages - START+++++++++++++++")
    wait(w1)
    packages = [Pattern("AltifyMax132.png").targetOffset(-124,1), Pattern("AltifyConversationManager250.png").targetOffset(-134,3), Pattern("AltifyAccountManager252.png").similar(0.73).targetOffset(-106,1),Pattern("AltifyOpptyManager254.png").similar(0.73).targetOffset(-105,3), Pattern("AltifySalesProcessManager255.png").similar(0.78).targetOffset(-116,2),Pattern("AltifyCallPlanner257.png").similar(0.83).targetOffset(-71,1),Pattern("LicensesDealmaker258.png").targetOffset(-43,1)]
    packagesTx = ["Altify Max", "Altify Conversation Manager", "Altify Account Manager", "Altify Opportunity Manager", "Altify Sales Process Manager", "Altify Call Planner", "Dealmaker"]
    instPackages = "Installed Packages"
    newComment = "Requested case - added permissions and packages, case will be closed"
    n = 0

    for package in packages:
        print(modNm + n, package)
        #Start with the user detail page to copy email address
        pkgTx = packagesTx[n]

        if package == packages[0]:
            print(modNm + "Getting User ID++++++++++++")
            type("f", KeyModifier.CTRL)
            type("User ID")
            doubleClick(Pattern("UserID319-1.png").targetOffset(81,1))
            wait(w1)
            type("c", KeyModifier.CTRL)
            wait(w1)
            type("f", KeyModifier.CTRL)
            wait(w1)
            type(Key.HOME, KeyModifier.CTRL)
            #type("Quick Find / Search")
            #wait(w1)
            #click("QuickFindISe340-1.png")
            wait(w1)
            click("QuickFindISearch127.png")
            type(instPackages)
            wait(w1)
            click("InstalledPackages-3.png")
            wait("Action1241-1.png", w60)

            if exists("InstalledPac318.png") or exists("InstalledPac319.png") or exists("Action320.png"):
                click(package)
                wait(w1)
                wait("PackageDetails-1.png", w20)

            click("AddUsers134.png")
            wait("AddUsersAltiMax-3.png", w20)
            wait(w1)
            click(Pattern("EditBtn1-1.png").similar(0.78))
            wait(w2)
            wait("Users1EditVi-1.png", w20)
            wait(w2)
            field = find("Field136.png")
            wait(1)
            click(field.below(30))
            wait(0.1)
            click(field.below(30))
            type("User ID")
            operator = find("Operator1113-1.png")
            wait(1)
            click(operator.below(30))
            wait(0.1)
            click(operator.below(30))
            type("equals")
            value = find("Value1114-1.png")
            wait(1)
            click(value.below(30))
            wait(0.1)
            #click(value.below(30)
            mouseDown(Button.LEFT)
            mouseUp(Button.LEFT)
            wait(0.01)
            mouseDown(Button.LEFT)
            mouseUp(Button.LEFT)
            wait(1)
            type("v",KeyModifier.CTRL)
            click(Pattern("SaveBtn-1.png").similar(0.86).targetOffset(0,2))
            print(modNm + "Getting User ID - End==================")
            wait("AddUsersAltiMax-2.png", w20)

        #Here we start from anywhere to get to installed packages
        print(modNm + "Install Packages - START++++++++++++++++")
        type(Key.HOME, KeyModifier.CTRL)
        wait(w1)
        click(Pattern("SearchArea-1.png").targetOffset(-149,-1))
        wait(w1)
        type(instPackages)
        wait("InstalledPac508-1.png",w60)
        click("InstalledPac508-1.png")
        wait("InstalledPackages-2.png", w30)

        if n != 0:
            type("f", KeyModifier.CTRL)
            type(pkgTx)

        if n > 4:
            wheel(WHEEL_DOWN, 3)

        wait(w1)
        click(package)
        wait(w1)
        wait("LicensedUsers-1.png", w20)
        click("AddUsersBtn-2.png")
        wait(w1)
        wait("AvailableUse306-1.png", w100)
        wait(w1)

        if exists(Pattern("Action513-1.png").similar(0.81).targetOffset(0,12)):
            wait(w1)
            click(Pattern("Action513-1.png").similar(0.81).targetOffset(0,12))
            wait(w1)
            click("AddBtn1-1.png")
            wait(w1)

        else:
            wait(w1)
            click("Cancel1136-1.png")
            wait(w1)
        n = n + 1

    print(modNm + "options all done")
    print(modNm + "Install packages - END===============")
    wait(w1)
    print(modNm + "Comments - Start++++++++++++")
    click("Cases1230-1.png")
    wait("CasesHome1246-1.png",w20)
    click("Gol435-1.png")
    wait("xRegionalST436-1.png", w30)
    click(Pattern("CaseNumber1012-1.png").similar(0.77).targetOffset(-1,17))
    wait(w1)
    wait("CaseDetail1108.png", w10)
    click("CaseDetail1209.png")
    wait(0.5)
    click("NewComment1109.png")
    wait(1)
    wait("AddComment1110.png", w30)
    click(Pattern("CannedCommen1111.png").similar(0.75).targetOffset(72,39))
    type(newComment)
    click("SaveSend1122.png")
    wait("CaseDetail1123.png", w30)
    doubleClick(Pattern("Status1124.png").targetOffset(60,2))
    wait(w1)
    #click("ArrowDown1125.png")
    type("closed")
    wait(w1)
    click("Status1124.png")
    wait(w1)
    click("SaveBtn1129.png")
    wait("EditDelete1130.png", w20)
    click("Cases1131.png")
    wait("CasestHome1132.png", w30)


    print(modNm + "Comments - End================")
    #popup("SUCCESS!!!================")
    print(modNm + "Program done")

main()

