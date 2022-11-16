# https://forum.gamer.com.tw/C.php?page=1&bsn=60076&snA=3175175

# NYCUIMF2022

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def main(driver, f_name, l_name, email_name, pw):
    login_url = 'https://accounts.google.com/signup/v2/webcreateaccount?biz=false&cc=TW&dsh=S-871672726%3A1668515973917173&flowEntry=SignUp&flowName=GlifWebSignIn&ifkv=ARgdvAvwoATlPpNYmCWYzvFtmiCI6sbLA86ELFdQBkcwsl5RgF25rh0jI6jF6imro_cfRrwqHRPL'
    driver.get(login_url)
    time.sleep(3)
    driver.find_element(By.ID, "lastName").send_keys(l_name)
    time.sleep(3)
    driver.find_element(By.ID, "firstName").send_keys(f_name)
    time.sleep(3)
    driver.find_element(By.ID, "username").send_keys(email_name)
    time.sleep(3)
    driver.find_element(By.NAME, "Passwd").send_keys(pw)
    time.sleep(3)
    driver.find_element(By.NAME, "ConfirmPasswd").send_keys(pw)
    time.sleep(3)
    driver.find_element(
        By.CSS_SELECTOR, ".VfPpkd-LgbsSe-OWXEXe-k8QpJ > .VfPpkd-vQzf8d").click()
    time.sleep(200)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    f_name = 'peter'
    l_name = 'lee'
    email_name = 'imfter83232'
    pw = 'defhed242'
    bth_y = 2000
    bth_m = 6
    bth_d = 20
    sex = 'male'
    main(driver, f_name, l_name, email_name, pw)
