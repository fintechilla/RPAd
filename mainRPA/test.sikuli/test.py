from lackey import *
from datetime import datetime
import mainMerge as mainMerge
import P_password as password
import R_ratecenter as rateCenter
import tools.wTimes as wTimes
import getCaseNumber as getCaseNumber
import Comment as comment
import tools.config as config
import tools.Case as case
import MonitorMgmt as monitor

w1, w2, w3, w4, w5, w10, w20, w30, w40, w50, w60, w100, wh = wTimes.times
SettingsMaster.MoveMouseDelay = 0
n = 0
lastN = 0
lastCaseNumber = 0
successful = False
module: str = ""
while True:
    currentDT = datetime.now()
    dateTime = currentDT.strftime("%Y-%m-%d-%H:%M:%S")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("T: Current Time: ", dateTime, " @loop: ", n)
    n = n + 1
    recordsDisplayed = True
    print(
        "T: LAST: module @loop:", lastN, " case number:  ", lastCaseNumber,
        " module: ", module, " successful?: ", successful)
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    try:
        if exists("RefreshBtn1229.png"):
            click("RefreshBtn1229.png")

        elif exists("CasesHome415.png"):
            click(Pattern("Go417.png").targetOffset(-60, 0))
            wait(w1)
            type("x")
            wait(w1)
            click("Go417.png")


        sleep(2)
        if exists("NoRecordsToDisplay450.png"):
            recordsDisplayed = False
            print("T: recordsDisplayed = False", " @loop: ", n)
            wait(w10)
            # popup("No records to display")

        if recordsDisplayed:
            print("T: recordsDisplayed: ", recordsDisplayed)
            click(Pattern("CaseNumber1223.png").similar(0.74).targetOffset(-15, -185))
            click(Pattern("CaseNumber1223.png").similar(0.74).targetOffset(-15, 23))
            wait("FindDuplicates1225.png", 15)
            wait(1)
            print("T: past Find Duplicates")
            wait(3)
            caseNumber: object = getCaseNumber.useNoTess()

            if exists(Pattern("RootCauseAccountMerge1225.png").similar(0.84)):
                print("T: Account Merge +++ ",)
                print("T: Date/Time: ", dateTime, " CASE: ", caseNumber)
                module = "Merge"
                lastN = n
                lastCaseNumber = caseNumber
                successful = False
                mainMerge.main(caseNumber)
                successful = True

            elif exists(Pattern("1565011562815.png").similar(0.79)):
                print("T: test: Other Sub Reason == SalesEdge/Altify")
                print("T: Date/Time: ", dateTime, " CASE: ", caseNumber)
                module = "SalesEdge/Altify"
                lastN = n
                lastCaseNumber = caseNumber
                successful = False
                hover("CaseComments1224.png")
                click("New1226.png")
                wait(2)
                click(Pattern("CommentDetails1227.png").targetOffset(238, 61))
                type("This case cannot be completed by ST Automated User. Thank you")
                wait(1)
                click(Pattern("Save1228.png").similar(0.75))
                wait("CaseDetail1230.png", 10)
                wait(w1)
                doubleClick(Pattern("Status1231.png").similar(0.73).targetOffset(44, 1))
                type("On Hold")
                successful = True
                wait(3)

            elif exists("RootCausePasswordReset1227.png"):
                print("T: Password Reset +++")
                print("T: Date/Time: ", dateTime, " CASE: ", caseNumber)
                module = "Password"
                lastN = n
                lastCaseNumber = caseNumber
                successful = False
                password.main()
                successful = True

            elif exists("RootCauseRateCenterIncorrect1228.png"):
                print("T: Rate Center Incorrect +++")
                print("T: Date/Time: ", dateTime, " CASE: ", caseNumber)
                module = "Rate Center"
                lastN = n
                lastCaseNumber = caseNumber
                successful = False
                successful = rateCenter.main()

            elif exists("1539290166288.png"):
                print("T: PRISM - not supported yet+++")
                print("T: Date/Time: ", dateTime, " CASE: ", caseNumber)
                # import prism

            elif exists(Pattern("1512674665954.png").similar(0.75)):
                print("T: A Hidden Offer +++")
                # import hiddenoffer

            elif exists("1546531630030.png"):
                print("T: CPQ Ethernet Test +++")
                # import tenmftest

            elif exists("1518634010154.png"):
                print("T: ARCF +++")
                # import rcf

            elif exists("1518812807938.png"):
                print("T: ADIR +++")
                # import dir

            elif exists("1545431550191.png"):
                print("Disco Workaround +++")
                # import disco

            elif exists("1545079501583.png"):
                print("T: CPQ Offer Report +++")
                # import OCPQ

            # elif exists(Pattern("1565011562815.png").similar(0.79)):
            #     print("T: test: Other Sub Reason == SalesEdge/Altify")
            #     hover(Pattern("1565011830290.png").similar(0.72))
            #     click("1565011847339.png")
            #     wait(2)
            #     click(Pattern("1565011959895.png").targetOffset(46,30))
            #     type("This case cannot be completed by ST Automated User. Thank you")
            #     wait(1)
            #     click("1565012071914.png")
            #     doubleClick(Pattern("1565012120268.png").similar(0.77))
            #     type("On Hold")
            #     wait(3)

    except:
        print("T: FindFailed occurred @loop: ", n)
        dateTimeFF = currentDT.strftime("%Y-%m-%d-%H:%M:%S")
        print(
        "T: FF-Time: ", dateTimeFF, " module: ", module, " last module @loop:", lastN, " last case number:  ", lastCaseNumber,
        " successful?: ", successful)
        print("recordsDisplayed: ", recordsDisplayed)
        sleep(5)
        type(Key.HOME, KeyModifier.CTRL)
        wait(1)

        if exists("RefreshBtn1229.png"):
            print("T: arrived in xRegional")

        elif exists("CasesGolden313.png"):
            click("CasesGolden313.png")
            print("T: CasesGolden clicked, get top case in cases home, go to xRegional")
            monitor.goFromRecentCasesToxRegionalView()

        elif exists("CasesLightBlue433.png"):
            click("CasesLightBlue433.png")
            print("T: CasesLightBlue - clicked, go to xRegional")
            monitor.goFromRecentCasesToxRegionalView()

        else:
            success = False
            loopHr = 0
            limitLoopHr = 6
            while not success and loopHr < limitLoopHr:
                type(Key.HOME, KeyModifier.CTRL)
                wait(w1)

                if not exists("CasesHome415.png") and not exists("RefreshBtn1229.png"):
                    print("T: did Not find CasesHome or RerfreshBtn")
                    type("w", KeyModifier.CTRL)
                    loopHr = loopHr + 1

                else:
                    homeRefresh = True
                    print("T: Found CasesHome or RerfreshBtn")

                    if exists("CasesHome415.png"):
                        print("T: IN CasesHome, go to xRegional")
                        monitor.goFromRecentCasesToxRegionalView()

                    else:
                        print ("T: IN xRegional, pass at this loop")
                        pass

        print("T: arrived at xRegional, go to the next loop")
        wait(0.5)
