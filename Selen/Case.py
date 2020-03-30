from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import lackey as lk
from selenium import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import re
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import tools.config as config
modNm = config.modNameRoot + "Case."


class Case:

    def __init__(self, browser):
        print(modNm + "Init called.")
        self.browser = browser

    def waitForElement(self, by, element):

        response = True
        try:
            element = WebDriverWait(self.browser, config.elementWaitTime).until(
                EC.presence_of_element_located((by, element))
            )
        finally:
            response = False

        return response

    def readRootCause(self):

        if self.waitForElement("By.ID", config.el_id_rootCause):

            elem = self.browser.find_element_by_id(config.el_id_rootCause).text
            # elem = self.browser.find_element_by_xpath("//*[@id='00N40000001xFr9_ileinner']")
            print(modNm + "readRootCause(self, browser): {}".format(elem))

        else:
            elem = "N/A"

        return elem

    def readOtherSubReason(self):

        if self.waitForElement("By.ID", config.el_id_otherSubReason):

            elem = self.browser.find_element_by_id(config.el_id_otherSubReason).text
            # elem = self.browser.find_element_by_xpath("//*[@id='00N40000003K4nq_ileinner']")
            print(modNm + "readOtherSubReason(self, browser): {}".format(elem))

        else:
            elem = "N/A"

        return elem

    def commentMake(self, comment):

        elem = self.browser.findElement(By.NAME, config.el_nm_newComment)
        elem.send_keys(Keys.ENTER)

        if self.waitForElement("By.ID", config.el_id_commentBody):

            elemCommentBody = self.browser.findElement(By.ID, config.el_id_commentBody)
            elemCommentBody.send_keys(comment)

        elemSave = self.browser.findElement("By.XPATH", config.el_x_SaveComment)
        elemSave.send_keys(Keys.ENTER)




