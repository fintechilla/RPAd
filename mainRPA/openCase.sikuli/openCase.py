from lackey import *
import tools.wTimes as wTimes
import Case as case
from datetime import datetime

def main():

    w1, w2, w3, w4, w5, w10, w20, w30, w40, w50, w60, w100, wh = wTimes.times
    found = False
    WORKING = "Working"

    currentDT = datetime.now()
    print("oC: currentDT: ", currentDT)

    if exists(Pattern("NewCase243.png").similar(0.82)): #and exists("RefreshSmallBtn244.png"):
        print("oC: NewCase Btn exists")
        type(Key.F5)

    elif exists("CaseLogo140.png") and exists("RecentCases242.png"):
        click(Pattern("view239.png").similar(0.76).targetOffset(36,0))
        wait(w1)
        type("x")
        click()
        wait(w1)

        if exists("Go!241.png"):
            print("oC: Go! exists")
            click("Go!241.png")
            wait(w1)

    elif exists("CasesGolden353.png"):
        click("CasesGolden353.png")
        wait("RecentCases242.png", w100)
        wait(w1)
        click(Pattern("view239.png").similar(0.76).targetOffset(36, 0))
        wait(w1)
        type("x")
        click()
        wait(w1)
        click("Go!241.png")
        wait(w1)

    wait("CaseNumber1252.png", w100)
    wait(w1)

    if exists("UAction104.png"):
        found = True
        click(Pattern("CaseNumber150.png").similar(0.74).targetOffset(-22, 21))
        wait(w1)
        wait("CaseDetail152.png", w60)
        wait(w1)
        print("oC: new case to be merged")

        # case.changeStatusInCase(WORKING)

    return found
        
