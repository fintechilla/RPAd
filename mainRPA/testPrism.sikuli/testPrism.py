from lackey import *
import Comment as comment
import Case as case
import Pr_Reflow as reflow

import tools.wTimes as wTimes

import MonitorMgmt as monitor

w1, w2, w3, w4, w5, w10, w20, w30, w40, w50, w60, w100, wh = wTimes.times
SettingsMaster.MoveMouseDelay = 0
wait(w2)

print("Pr: Test 12. ++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Pr: Test 12. SCCE Field - is it populated? ")
print("Pr: IN Site Survey")

type(Key.HOME, KeyModifier.CTRL)
wait(w1)
monitor.doFSearch("SCCE Requested Date")
wait(w1)
scceReqDate = ""

dragDrop(Pattern("SCCERequestedDate149-1.png").targetOffset(65, 1),
    Pattern("SCCERequestedDate149-1.png").targetOffset(205, 0))

if exists("SCCERequesteedDateEmpty115-1.png"):

    print("Pr: REFLOW Prism Trigger - below")

    reflow.main()

    print("Pr: End of Reflow")
    timeRefresh = 5
    for i in range(timesRefresh):
        type(Key.F5)
        wait(w5)

    prismPopulated: bool = verifyPrism.main()

    type("w", KeyModifier.CTRL)
    wait(w1)
    type("c", KeyModifier.CTRL)
    scceReqDate = getClipboard()
    print("Pr: SCCE Requested date: {}".format(scceReqDate))
    scceFlag = not bool(scceReqDate)
    print("Pr: not bool(scceReqDate): {}".format(scceFlag))

    if prismPopulated:
        print("Pr: Prism populated after reflow")
        comment.addNewCommentInCase(config.commentPrismPopulated)
        case.changeStatusInCase(config.CLOSE)

    else:

        print("Pr: Prism is NOT populated after reflow")
        comment.addNewCommentInCase(config.commentPrismIntReflowFailed)
        case.changeStatusInCase(config.ONHOLD)

else:
    print("Pr: SCCE Requested Date is populated, please go to Prism. Current Prism Id: ")