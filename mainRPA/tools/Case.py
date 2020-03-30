from lackey import *
import tools.wTimes as wTimes
w1, w2, w3, w4, w5, w10, w20, w30, w40, w50, w60, w100, wh = wTimes.times

class Case:
    def changeStatus(self, status):
        doubleClick(Pattern(r"Cimages.sikuli/StatusLabel421.png").similar(0.75).targetOffset(42, 1))
        # doubleClick(Pattern(r"C:\SikuliX\Desktop\MergeX\images.sikuli\StatusLabel421.png").similar(0.75).targetOffset(42, 1))
        click()
        type(status)
        click(Pattern(r"images.sikuli/StatusLabel421.png").similar(0.75).targetOffset(-5, 1))
        # click(Pattern(r"C:\SikuliX\Desktop\MergeX\images.sikuli\StatusLabel421.png").similar(0.75).targetOffset(-5, 1))
        wait(w1)
        click(r"images.sikuli/SaveBtn455.png")
        # click(r"C:\SikuliX\Desktop\MergeX\images.sikuli\SaveBtn455.png")
        wait(w5)
        click(r"Cimages.sikuli/Cases424.png")
        # click(r"C:\SikuliX\Desktop\MergeX\images.sikuli\Cases424.png")
        wait(w2)

