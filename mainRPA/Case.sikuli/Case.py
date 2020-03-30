from lackey import *
import tools.wTimes as wTimes

w1, w2, w3, w4, w5, w10, w20, w30, w40, w50, w60, w100, wh = wTimes.times


def changeStatusInCase(status):
    wait("VCaseDescription239.png", w100)
    wait(w1)
    click("VCaseDescription239.png")
    click(Pattern("VCaseDescription239.png").targetOffset(300, 0))
    doubleClick(Pattern("Status1131.png").similar(0.71).targetOffset(47, 0))
    click()
    type(status)
    click(Pattern("Status1131.png").targetOffset(-200, 0))
    wait(w1)
    if exists("SaveBtn1132.png"):
        click("SaveBtn1132.png")

    else:
        type(Key.ESC)
        wait(w1)
        click("SaveBtn1132.png")

    wait("Edit1143.png", w10)
    wait(w1)
    click("CasesGolden1133.png")
    wait(w2)


def changeStatusInRecentCases(status):
    wait(w2)
    if exists("RecentCases1149.png"):
        try:
            click(Pattern("CaseNumber1149.png").targetOffset(0, 22))
        except:
            click("CasesGolden1151.png")
            wait("RecentCases1149.png", w100)
            wait(w1)
            click("CaseNumber1149.png")
            wait(w1)

        changeStatusInCase(status)


def changeRootCauseTo(label):
    wait(w2)
    doubleClick(Pattern("RootCauseJ406.png").targetOffset(75, 0))
    wait(w1)
    type(label)
    wait(w1)
    click("RootCauseJ406.png")
    wait(w5)

# closeInCase()
# closeInRecentCases()
