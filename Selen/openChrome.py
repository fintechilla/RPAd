
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
modNm = config.modNameRoot + "openChrome: "
import FindCaseByCaseNumber as findCase
import Case as case

windows = []
browser = webdriver.Edge(config.web_driver_Edge)
# browser = webdriver.Edge
# session_url = browser.current_url              #command_executor._url
# session_id = browser.session_id
# session_id = "6BDA61EB-2C52-45F2-81D6-CBCD72E140E7"
# session_      #command_executor._url  #session_id
# print(modNm + "a/attaching: session_id: " + session_id)

# browser.session_id = session_id
# session_url = browser.current_url              #command_executor._url
#
# session_id = browser.session_id
#
# browser = webdriver.Remote(command_executor=session_url, desired_capabilities={})
# browser.session_id = session_id

# Browser("index:=0").navigate("http://www.google.com")
#command_executor._url  # "http://127.0.0.1:60622/hub"

# session_id = browser.session_id
# print(modNm + "a/attaching: session_id: " + session_id)

print(modNm + "Go to xRegional")
browser.get(config.Url_xRegional)
windows.append(browser.current_window_handle)

print(modNm + "Title: " + str(browser.title))

browser = web.loginIntoSF_ifLoginMenu(browser)

lk.wait(2)

caseNumber = "0"
try:

    print(modNm + "b/find elem cases")
    elem = browser.find_element_by_class_name("x-grid3-col-CASES_CASE_NUMBER")
    caseNumber = elem.text
    print(modNm + "Found caseNumber {}".format(caseNumber))
    findCase.main(caseNumber, browser)

except:
    print(modNm + "Searching for No Records to display...")
    elemNoRecords0 = browser.find_element_by_id("ext-gen12")
    elemNoRecords1 =elemNoRecords0.text
    print(modNm + "elemNoRecords0.text exists: " + str(elemNoRecords1))
    print("Found {}".format(str(elemNoRecords1)))

if caseNumber != "0":
    print(modNm + "Go to case: {}".format(caseNumber))
    cs = case.Case(browser)
    # findCase.main(caseNumber, browser)
    lk.wait(1)
    elemRootCause = cs.readRootCause()
    print(modNm + "RootCause: {}".format(elemRootCause))
    lk.wait(1)
    elemSubReason = cs.readOtherSubReason()
    print(modNm + "OtherSubReason: {}".format(elemSubReason))

    cs.commentMake("Hello")

else:
    print(modNm + "No Records")



# elemRefresh = browser.find_element_by_id("00B1W000007TSla_refresh")
# print("Refresh: {}; elemRefresh: {}".format(i, elemRefresh))
# elemRefresh.send_keys(Keys.RETURN)
# lk.wait(5)

