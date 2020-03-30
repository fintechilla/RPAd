from lackey import *
import MonitorMgmt as monitor
import Comment as comment
import Case as case
import tools.wTimes as wTimes
import tools.config as config

SettingsMaster.MoveMouseDelay = 0
w1, w2, w3, w4, w5, w10, w20, w30, w40, w50, w60, w100, wh = wTimes.times


def main():
    success = False
    newPrismId = ""
    wait(w2)
    type(Key.HOME, KeyModifier.CTRL)
    wait(w1)
    monitor.doFSearch("Site Survey History")
    click("SiteSurveyHistoryOrangeBtn1216.png")
    wait(w1)

    if exists("SiteSurveyHistory1143.png"):
        if exists("ActionChangePrismIDTo136.png"):
            dragDrop(Pattern("ChangedPRISMTo131.png").targetOffset(59,0), Pattern("ChangedPRISMTo131.png").targetOffset(107,0))
            type("c", KeyModifier.CTRL)
            newPrismId = getClipboard()
            print("PrVp: new prismId: ", newPrismId)
            success = True

        else:
            print("PrVp: Changed Prism Not found")

    return success, newPrismId


# main()
