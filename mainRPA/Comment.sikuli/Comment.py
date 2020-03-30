from lackey import *
import tools.wTimes as wTimes

w1, w2, w3, w4, w5, w10, w20, w30, w40, w50, w60, w100, wh = wTimes.times
SettingsMaster.MoveMouseDelay = 0

def addNewCommentInCase(commentText):
    print("C: addNewCommentInCase: ", commentText)
    wait(w1)

    if exists("RecentCases354.png"):
        print("C: exists('RecentCases1149.png')")
        try:
            click(Pattern("CaseNumber606.png").similar(0.73).targetOffset(0, 22))
        except FindFailed:
            click("CasesGolden353.png")
            wait("RecentCases1149.png", w100)
            wait(w1)
            click(Pattern("CaseNumber606.png").similar(0.75).targetOffset(0, 22))
            wait("CaseDetail350.png", w20)
            wait(w1)

    wait("CaseComments959.png", w30)
    wait(w1)
    click("CaseComments959.png")
    wait(w2)
    click("New1122.png")
    wait(w2)
    layoutStrange = False
    if exists("CommentDetails513.png"):
        click(Pattern("CommentDetails513.png").targetOffset(248, 58))

    elif exists("CommentEdit440.png"):
        layoutStrange = True
        click(Pattern("CommentEdit440.png").targetOffset(260, 44))

    wait(w1)
    type(commentText)
    wait(w1)

    if exists(Pattern("Save443.png").similar(0.82)):
        layoutStrange = True
        click(Pattern("Save443.png").similar(0.82).targetOffset(8, 5))

    elif exists("SaveUpGreen520.png"):
        click(Pattern("SaveUpGreen520.png").similar(0.76).targetOffset(3, 2))

    wait(w1)
    wait("CaseDetail350.png", w30)
    wait(w1)


def addNewCommentInAccount(commentText):
    print("C: addNewCommentInAccount: ", commentText)
    wait(w3)
    if exists(Pattern("CommentsBillingAccount530.png").similar(0.80).targetOffset(-1, 2)):
        click(Pattern("CommentsBillingAccount530.png").similar(0.80).targetOffset(-1, 2))
        wait(w1)
        wait("NewComment530.png", w100)
        wait(w1)
        click("NewComment530.png")
        wait(w2)
        wait("CommentEdit531.png")
        wait(w1)
        click(Pattern("CommentEdit531.png").targetOffset(264, 43))
        wait(w1)
        type(commentText)
        wait(w1)
        click(Pattern("SaveBtnUpper532.png").similar(0.87))
        wait(w2)
        wait("CommentDetail534.png", w100)
        wait(w5)


# addNewCommentInAccount("Merge performed as requested.")
