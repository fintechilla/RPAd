from lackey import *
import MonitorMgmt as monitor
import Comment as comment
import Case as case
import tools.wTimes as wTimes
import tools.config as config
import Pr_changeStatusInSS as changeStatus

w1, w2, w3, w4, w5, w10, w20, w30, w40, w50, w60, w100, wh = wTimes.times
def main():
    print("PrRe: IN Site Survey")
    wait(w2)
    type(Key.HOME, KeyModifier.CTRL)
    wait(w1)

    if exists("AvXDown447.png"):

          click(Pattern("AvXDown447.png").targetOffset(30, -1))
          wait(w1)

    type("f", KeyModifier.CTRL)
    type(Key.BACKSPACE)
    wait(w1)

    monitor.doFSearch("Routing")
    wait("vRouting1220.png", w10)
    wait(w1)
    monitor.doFSearch("Market Development Requested")
    doubleClick(Pattern("MarketDevelopmentRequested213.png").targetOffset(120, 2))
    type("c", KeyModifier.CTRL)
    marketDevReqd = ""
    marketDevReqd = getClipboard()
    print("PrRe: Market Development Requested: ", marketDevReqd)

    if bool(marketDevReqd):     # is not None or marketDevReqd != " ":

        print("Pr: Market Development Required is populated, must clear it")
        type(Key.BACKSPACE)
        click("MarketDevelopmentRequested213.png")
        wait(w1)
        type(Key.HOME, KeyModifier.CTRL)
        wait(w1)

    changeStatus.main(config.ON_HOLD)
    wait(w1)
    changeStatus.main(config.SUBMITTED)
    wait(w1)



    print("PrRe: End of Reflow")

# main()