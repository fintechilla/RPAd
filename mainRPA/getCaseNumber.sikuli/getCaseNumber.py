from lackey import *
import tools.wTimes as wTimes
# from tools.Carret import Carret
import pytesseract
import tools.Regionalize as Reg
import MonitorMgmt as monitor
import tools.config as config

def useTess():
    pytesseract.pytesseract.tesseract_cmd = config.tesseractLink
    TESSDATA_PREFIX = config.TESSDATA_PREFIX
    w1, w2, w3, w4, w5, w10, w20, w30, w40, w50, w60, w100, wh = wTimes.times
    reg = Reg.Regionalize()
    # click(Pattern("CaseNumber1159.png").similar(0.73))
    wait(w2)
    wh = 5

    locBegName = find(Pattern("CaseNumber1159.png").similar(0.73).targetOffset(67, 0))
    regBegName = Region(locBegName.getX(), locBegName.getY(), 100, 25)
    locEndName = find(Pattern("alterName.sikuli/VewHierarchv1246.png").targetOffset(-46, 0))
    regEndName = Region(locEndName.getX(), locEndName.getY(), 100, 25)
    coordW = locEndName.getX() - locBegName.getX()
    shift = 120
    caseNumber = reg.getText(Pattern("CaseNumber1159.png").similar(0.73), shift, -3, coordW - shift - 2, 25)
    print("gCN: caseNumber: ", caseNumber)
    return caseNumber

def useNoTess():
    w1, w2, w3, w4, w5, w10, w20, w30, w40, w50, w60, w100, wh = wTimes.times
    dragDrop(Pattern("CaseNumber1159.png").similar(0.74).targetOffset(55,0), Pattern("CaseNumber1159.png").similar(0.74).targetOffset(110,0))
    type("c", KeyModifier.CTRL)
    caseNumber = getClipboard()

    return caseNumber

# main()