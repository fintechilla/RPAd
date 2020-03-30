from lackey import *
import tools.wTimes as wTimes

w1, w2, w3, w4, w5, w10, w20, w30, w40, w50, w60, w100, wh = wTimes.times

SettingsMaster.MoveMouseDelay = 0


def closeFSearch():

    if exists("AvX1116.png"):
        doubleClick(Pattern("AvX1116.png").targetOffset(-150, -2))
        type(Key.BACKSPACE)

        wait(w1)

        click(Pattern("AvX1116.png").targetOffset(29, -2))
        wait(w1)

    else:
        pass


def doFSearch(expression):
    # if exists("AvX1116.png"):
    #     closeFSearch()

    type("f", KeyModifier.CTRL)
    type(expression)
    wait(w1)


def changeAccountName(textName):
    print("McAN: Change Account Name to: ", textName)
    doubleClick(Pattern("AccountName327.png").similar(0.84).targetOffset(90, 0))
    wait(w1)
    type(textName)
    click("AccountRecordType328.png")
    wait(w1)
    click("Save329.png")
    wait(w1)
    wait("EditDeleteBtns336.png", w100)
    wait(w1)


def clickIfAccounts():
    if exists("Accounts101.png"):
        click("Accounts101.png")
    elif exists("AccountsBlueOrange231.png"):
        click("AccountsBlueOrange231.png")
    elif exists("AccountsOrange354.png"):
        click("AccountsOrange354.png")

    wait(w1)


def goFromRecentCasesToxRegionalView():
    click(Pattern("Go1242.png").targetOffset(-61, -1))
    wait(1)
    type('x')
    wait(0.5)
    click("Go1242.png")
    wait("CaseNumber1223.png", w60)
    wait(w1)
    click(Pattern("CaseNumber1243.png").similar(0.73).targetOffset(0, 20))
    # wait("CaseDetail1230.png", w30)
    wait(1)


def reverseAccountNames(textName, noAccounts):
    print("mA: move tabs to the right - to the main account")
    for k in range(noAccounts):
        type(Key.TAB, KeyModifier.CTRL)

    print("mA: restore original account names")
    for k in range(noAccounts):
        print("MrAN: k: ", k, " name to be changed: ", textName[k])
        changeAccountName(textName[k])
        wait(w1)
        type(Key.TAB, Key.SHIFT + KeyModifier.CTRL)


def goFromQueueViewToCaseDetail():
    click(Pattern("CaseNumber224.png").similar(0.78).targetOffset(0, 23))
    wait("CaseDetail1230.png", w30)
    wait(w1)


def goFromRecentCasesToCaseDetail():
    click(Pattern("CaseNumber1223.png").similar(0.74).targetOffset(0, 23))
    wait("CaseDetail1230.png", w30)
    wait(w1)


def mapzillaLoggin(id, password):
    wait(w1)
    click(Pattern("EIDVID1218.png").targetOffset(70, 1))
    type(id)
    type(Key.TAB)
    wait(w1)
    type(password)
    wait(w1)
    print("rC: click Login")  # ; loopPrivacy: ", loopPrivacy)
    click("Login1219.png")
    wait(2)

    if exists("WarningUser1251.png"):
        print("R: concurrent Mapzilla sessions exist")
        click("OKContinueActiveSession329.png")
        wait(w2)


def splitAndRemoveLeadBlanks(line, separator):
    split_words = line.split(separator)
    outLine = []
    for word in split_words:
        outLine.append(word.lstrip(" "))

    return outLine
# mapzillaLoggin("V881790", "gthb<101")
