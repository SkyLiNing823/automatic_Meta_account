from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import os


def getURL(driver, url):
    driver.get(url)
    time.sleep(5)
    webdriver.ActionChains(driver).move_by_offset(200, 100).click().perform()
    return driver


def maintainScraper():
    time.sleep(5000)
