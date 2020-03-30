from lackey import *
import tools.wTimes as wTimes
import tools.config as config

w1, w2, w3, w4, w5, w10, w20, w30, w40, w50, w60, w100, wh = wTimes.times
modNm = config.modNameRoot + "Pr-prSearch: "

def main(siteSurveyNo):
    success = False
    wait(w1)
    type("n", KeyModifier.CTRL)
    wait(w1)
    type("prism.charter.com")
    type(Key.ENTER)
    wait("fkHelmetLogo341.png", w10)
    wait(w1)
    click("vManInHelemet342.png")
    wait("SearchByPrism344.png", w10)
    wait(w1)
    click("Survey344.png")
    wait("SurveySearch345.png", w10)
    wait(w1)
    click("SurveySearch345.png")
    wait("SurveyLinks347.png", w10)
    wait(w1)
    click(Pattern("SiteSurveyNo348.png").targetOffset(-23, 18))
    type(siteSurveyNo)
    wait(w1)
    type(Key.ENTER)
    # click("SearchBtn350.png")
    wait(w3)
    prismId = ""

    try:
        wait("SurveyMap1114.png", w30)

        if exists("SurveygSurveyDouble440.png"):
            print(modNm + "double or more prism ids")
            success = True
            prismId = config.prismIdDefaultValue

        elif exists("SurveyMap1114.png"):
            print(modNm + "single prism id")
            dragDrop(Pattern("SurveyMap1114.png").targetOffset(40,0), Pattern("SurveyMap1114.png").targetOffset(105,0))
            type("c", KeyModifier.CTRL)
            prismId = getClipboard()
            success = True

    except:
        print(modNm + "try prism id window to copy number")
        dragDrop(Pattern("PrismIdLabel1123.png").targetOffset(44,18), Pattern("PrismIdLabel1123.png").targetOffset(-20,18))
        type("c", KeyModifier.CTRL)
        prismId = getClipboard()

        if not bool(prismId):
            print(modNm + "prism id exists: {}".format(prismId))
            success = True

    # popup(prismId)

    type("w", KeyModifier.CTRL)
    wait(w1)

    return success, prismId


# main("06375954")
