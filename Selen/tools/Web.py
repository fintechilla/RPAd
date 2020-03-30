from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import lackey as lk
from selenium import *
import ErrorLoadingExtension as error
import re
import tools.config as config

modNm = config.modNameRoot + "Web"


def loginIntoSF_ifLoginMenu(browser):

    print(modNm + ".loginIntoSF_ifLoginMenu(browser) - START")
    lk.wait(2)
    try:

        lk.wait("tools/images/CasesGolden1024.png", 2)
        wait(1)
        print("No need to login into SF")

    except:

        lk.wait("tools/images/UserName1103.png", 30)
        lk.wait(1)

        session_id = browser.session_id
        print(modNm + "loginIntoSF_ifLoginMenu(browser):session_id: " + session_id)

        print(modNm + "a/browser.get...")
        url = browser.current_url
        print(modNm + "loginIntoSF_ifLoginMenu(browser):url: " + str(url))

        try:

            elem = browser.find_element_by_id("hint_back_chooser")
            elem.send_keys("Keys.RETURN")
            lk.wait(2)

            elem = browser.find_element_by_id("use_new_identity")
            # elem.send_keys("Keys.RETURN")
            lk.wait(5)

        except:
            print(modNm + ".loginIntoSF_ifLoginMenu(browser): No hint_back_user")

        lk.wait(2)
        elem = browser.find_element_by_id("username")
        elem.send_keys(config.username)
        print(modNm + "a/username")

        elem = browser.find_element_by_id("password")
        elem.send_keys(config.password)
        print(modNm + "a/password")

        elem = browser.find_element_by_id("Login")
        elem.send_keys(Keys.RETURN)
        print(modNm + "a/Login")

        lk.wait(1)

    print(modNm + "b/waiting for Home")
    lk.wait("tools/images/Home1252.png",30)
    lk.wait(1)

    return browser


# try:
#     print(modNm + "test for 'use different method")
#     elem = browser.find_element_by_class_name("small mt8 ib")
#     elem.click()
#     lk.wait(1)
#
#     elem = browser.find_element_by_id("sem0")
#     elem.click()
#     lk.wait(1)
#     elem = browser.find_element_by_id("save")
#     elem.click()
#     lk.wait(1)
#
#     elem = browser.find_element_by_id("tc")
#     elem.click()
#     lk.wait(1)
#
#
# except:
#     print(modNm + "NO test for 'use different method")
