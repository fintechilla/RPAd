from lackey import *
import tools.wTimes as wTimes
import Comment as comment
import Case as case
import tools.config as config
import MonitorMgmt as monitor

w1, w2, w3, w4, w5, w10, w20, w30, w40, w50, w60, w100, wh = wTimes.times
SettingsMaster.MoveMouseDelay = 0

def main(caseNumber):

    caseDetail = False
    loopCD = 0
    limitLoopCD = 5
    while not caseDetail and loopCD < limitLoopCD:

        print("R: LoopCD: ", loopCD, " While loop in except searching for Case page to comment")
        type(Key.HOME, KeyModifier.CTRL)
        wait(w1)

        if exists("CaseDetail511.png"):

            print("R: IN Case: Close the case due to an error")
            comment.addNewCommentInCase(config.commentFailure)
            case.changeStatusInCase(caseNumber, config.ONHOLD)
            caseDetail = True

        elif exists("RefreshBtn1229.png"):

            print("R: click on a case below to go to Case Detail")
            monitor.goFromQueueViewToCaseDetail()

        elif exists("CasesHome415.png"):

            print("R: click on a case below to go to Case Detail")
            monitor.goFromRecentCasesToCaseDetail()

        else:

            print("R: Neither RefreshBtn nor CasesHome nor CaseDetail exist, close the current tab")
            type("w", KeyModifier.CTRL)

        loopCD = loopCD + 1

