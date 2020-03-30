from lackey import *
import tools.wTimes as wTimes
import pytesseract
from PIL import Image
import tools.config as config

# import matplotlib as mpl

# mpl.use('Agg')
pytesseract.pytesseract.tesseract_cmd = config.tesseractLink #r"C:\Users\p2881790\AppData\Local\Tesseract-OCR\tesseract"
TESSDATA_PREFIX = config.TESSDATA_PREFIX     #r"C:\Users\p2881790\AppData\Local\Tesseract-OCR"
w1, w2, w3, w4, w5, w10, w20, w30, w40, w50, w60, w100, wh = wTimes.times


class Regionalize:
    def getText(self, img, adjX, adjY, w, h):
        wait(w1)
        # print("Reg: find loc of img")
        loc = find(img)
        wait(w1)
        # print("Reg: get region: loc.getX(): ", loc.getX(), " adjX: ", adjX, " loc.getY(): " , loc.getY(), " adjY: ", adjY, " w: ", w,  " h: ", h)
        reg = Region(loc.getX() + adjX, loc.getY() + adjY, w, h)
        reg.highlight(wh, "RED")

        # print("Reg: capture reg")
        img = capture(reg)  # reg.getBitmap()
        # print("Reg: Image.fromarray(img)")
        img = Image.fromarray(img)
        fileName = "temp.bmp"
        # print("Reg: img.save(fileName)", fileName)
        img.save(fileName)
        # print("Reg: text = pytesseract.image_to_string(img)")
        text = pytesseract.image_to_string(img)
        print("Reg: return text", text)
        return text

    def checkEmptyArea(self, img, adjX, adjY, w, h):
        wait(w1)
        # print("Reg: find loc of img")
        loc = find(img)
        wait(w1)
        reg = Region(loc.getX() + adjX, loc.getY() + adjY, w, h)
        reg.highlight(wh, "RED")
        adj = 10
        reg.dragDrop(Location(loc.x + adjX, loc.y + adjY), Location(loc.x + w - adj, loc.y + h - adj))
        type("c", KeyModifier.CTRL)
        areaText = getClipboard()

        if not bool(areaText):
            return True

        else:
            return False
