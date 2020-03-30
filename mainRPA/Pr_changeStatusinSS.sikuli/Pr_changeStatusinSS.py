from lackey import *
import MonitorMgmt as monitor
import Comment as comment
import Case as case
import tools.wTimes as wTimes
import tools.config as config

w1, w2, w3, w4, w5, w10, w20, w30, w40, w50, w60, w100, wh = wTimes.times


def main(status):
    wait(w2)
    print("PrCs: starting change status IN Site Survey")
    doubleClick(Pattern("Status311.png").targetOffset(55, 0))
    wait("DependentFields313.png", w10)
    wait(w1)
    click(Pattern("StatusINDependedFields456.png").targetOffset(45, 0))
    wait(w1)
    type(status)
    wait(w1)
    click("StatusINDependedFields456.png")
    wait(w1)
    click("OK314.png")
    wait(w1)
    click("Save315.png")
    wait("SSLogo123.png", w30)
    wait(w1)


# main(config.ON_HOLD)
