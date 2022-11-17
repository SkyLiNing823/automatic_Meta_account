from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from funcLIB import *


def FBlogin(driver, email, pw):
    driver = getURL(driver, 'https://www.facebook.com/')
    # input email
    driver.find_element(By.NAME, "email").send_keys(email)
    # input password
    driver.find_element(By.NAME, "pass").send_keys(pw)
    time.sleep(0.5)
    # click login btn
    driver.find_element(By.NAME, "login").click()
    time.sleep(5)
    webdriver.ActionChains(driver).move_by_offset(200, 100).click().perform()
    return driver


if __name__ == '__main__':
    driver = webdriver.Chrome()
    email = 'testimf2022.2@gmail.com'
    pw = 'fef3554r4321'
    driver = FBlogin(driver, email, pw)
    maintainScraper()

    # # https://stackoverflow.com/questions/21928368/login-to-facebook-using-python-requests

# data = {
#     'lsd': lsd,
#     'charset_test': csettest,
#     'version': version,
#     'ajax': ajax,
#     'width': width,
#     'pxr': pxr,
#     'gps': gps,
#     'm_ts': mts,
#     'li': li,
# }
# data['email'] = email
# data['pass'] = pass
# data['login'] = 'Log In'

# s = requests.Session()
# r = s.post(url, data=data)
# r.raise_for_status()

# https://www.facebook.com/SeleniumIDERCWebdriver/posts/how-to-automate-facebook-login-and-signup-with-help-of-selenium-webdriver-execut/979064995492723/
