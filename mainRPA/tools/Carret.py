from lackey import *
import tools.wTimes as wTimes
w1, w2, w3, w4, w5, w10, w20, w30, w40, w50, w60, w100, wh = wTimes.times
class Carret:
    def copyAndPasteWord(self):

        type("c", KeyModifier.CTRL)
        wait(w1)
        # print("In copy...: img: ", img)
        click(r"images.sikuli/WordLogo956.png")
        # click(r"C:\SikuliX\Desktop\MergeX\images.sikuli\WordLogo956.png")
        wait(w2)
        type("v", KeyModifier.CTRL)
        type(Key.ENTER)

    def backspace(self, rLimit):

        for i in range(rLimit):
            type(Key.BACKSPACE)

    def dblClickDelete(self):

        doubleClick()
        type(Key.BACKSPACE)