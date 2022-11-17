from FB_login import FBlogin
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from funcLIB import *


def sendPost(driver, post_content):
    driver.find_element(By.CSS_SELECTOR, ".xkjl1po > .x1lliihq").click()
    # first post only(setting for receiver)
    try:
        driver.find_element(By.CSS_SELECTOR, ".xi3auck").click()
        driver.find_element(By.CSS_SELECTOR, ".xtk6v10 > .x1lliihq").click()
        driver.find_element(By.CSS_SELECTOR, ".xdpxx8g > span").click()
        driver.find_element(By.CSS_SELECTOR, ".xdpxx8g > span").click()
    except:
        pass
    time.sleep(3)
    # type text
    driver.find_element(By.CSS_SELECTOR, ".x14wi4xw").send_keys(post_content)
    # click send btn
    driver.find_element(
        By.CSS_SELECTOR, ".xh8yej3 > .x1i10hfl > .x1n2onr6").click()
    return driver


if __name__ == '__main__':
    driver = webdriver.Chrome()
    email = 'testimf2022.2@gmail.com'
    pw = 'fef3554r4321'
    # login
    driver = FBlogin(driver, email, pw)
    driver = getURL(driver, 'https://www.facebook.com/')
    post_content = '大家好！'
    driver = sendPost(driver, post_content)
    maintainScraper()
