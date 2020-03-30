from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from lackey import *


# driver = webdriver.Chrome()
# driver.implicitly_wait(3)
# driver.maximize_window()
# driver.get("http://www.google.com")
w = 3
print("Wait {}".format(w))
wait(w)
print("Done")