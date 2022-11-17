from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from funcLIB import *
from FB_login import FBlogin

if __name__ == '__main__':
    driver = webdriver.Chrome()
    email = 'testimf2022.2@gmail.com'
    pw = 'fef3554r4321'
    # login
    driver = FBlogin(driver, email, pw)
    try:
        # upload profile img
        element = driver.find_element(
            By.CSS_SELECTOR, 'div[aria-label="新增相片"]')
        webdriver.ActionChains(driver).move_to_element(
            element).click(element).perform()
        time.sleep(5)
        driver.find_element(
            By.XPATH, "//input[@type='file']").send_keys(os.getcwd()+"/media/profile.png")
        time.sleep(10)
        element = driver.find_element(
            By.CSS_SELECTOR, 'div[aria-label="儲存"]')
        webdriver.ActionChains(driver).move_to_element(
            element).click(element).perform()
    except:
        pass
    maintainScraper()
