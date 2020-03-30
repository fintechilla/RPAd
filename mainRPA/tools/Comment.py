from lackey import *
import tools.wTimes as wTimes
w1, w2, w3, w4, w5, w10, w20, w30, w40, w50, w60, w100, wh = wTimes.times
class Comment:
    def addNewComment(self, commentText):
        click(Pattern(r"images.sikuli/NewComment603.png").targetOffset(0, 2))
        # click(Pattern(r"C:\SikuliX\Desktop\MergeX\images.sikuli\NewComment412.png").targetOffset(0, 2))
        wait(w1)
        # wait(r"C:\SikuliX\Desktop\MergeX\images.sikuli\NewComment603.png", w20)
        # click(Pattern(r"C:\SikuliX\Desktop\MergeX\images.sikuli\CannedCommentBelow414.png").similar(0.74).targetOffset(74, 36))
        # wait(w1)

        click(Pattern(r"images.sikuli/CommentEdit559.png").targetOffset(460, -2))
        # click(Pattern(r"C:\SikuliX\Desktop\MergeX\images.sikuli\CommentEdit559.png").targetOffset(460, -2)) # SAVE
        type(commentText)
        wait(w1)
        click(r"images.sikuli/SaveBtn455.png")
        # click(r"C:\SikuliX\Desktop\MergeX\images.sikuli\SaveBtn455.png")
        wait(w1)
        wait(r"images.sikuli/CaseDetail1143.png", w100)
        # wait(r"C:\SikuliX\Desktop\MergeX\images.sikuli\CaseDetail347.png", w100)
        wait(w1)

