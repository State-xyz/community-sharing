from selenium import webdriver
import time
import os


class captcha:
    def __init__(self):
        # type: () -> object
        core_value = 0
        position_value = 0

captcha_element = []
captcha_res = ""

driver = webdriver.PhantomJS()
start_time = time.time()
driver.get("https://userscloud.com/?op=registration")

_table = driver.find_element_by_tag_name("table")

# filtering span tag
_spans = _table.find_elements_by_tag_name("span")
for span in _spans:
    raw_captcha = captcha()
    raw_captcha.core_value = int(span.get_attribute("innerHTML"))
    raw_captcha.position_value = int(span.get_attribute("style").split(';')[1][15:].replace("px",""))
    captcha_element.append(raw_captcha)

captcha_sorted = sorted(captcha_element, key=lambda captcha: captcha.position_value)
for elm in captcha_sorted:
    captcha_res = captcha_res + str(elm.core_value)

print "[R] Captcha: " + captcha_res

print "[T] Cost: %.2f" % (time.time() - start_time)

print "---"

os.system("taskkill /im phantomjs.exe /F")