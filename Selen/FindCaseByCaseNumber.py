from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import lackey as lk
from selenium import *
import ErrorLoadingExtension as error
import re
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import tools.config as config
import tools.Web as web
modNm = config.modNameRoot + "FindCaseByCaseNumber: "


def main(caseNumber, browser):

    elemSearch = browser.find_element_by_id("phSearchInput")
    elemSearch.send_keys(caseNumber)

    browser.find_element_by_id("phSearchButton").submit()
    lk.wait(2)

    # elemTag = browser.find_elements_by_tag_name("td")
    # elemTag = browser.find_elements_by_class_name("dataCell")
    elemTag = browser.find_element(By.CSS_SELECTOR("input[name='dataDell'] a"))
    # elemTag1 = elemTag[1].find_element_by_tag_name("a")
    print("Elem.tag :{}".format(str(elemTag)))
    print(modNm + "elemTag1: {}".format(elemTag))
    elemTag.click()

    # i = 0
    # for tag in elemTag:
    #
    #     print("tag {}: innerText: {}".format(i, tag.text))
    #     i += 1


    # elemCaseType = browser.find_element_by_class_name("pageType").text
    #
    # if elemCaseType == "Case":
    #
    #     print(modNm + "IN: Case: {}".format(caseNumber))
    #     return

