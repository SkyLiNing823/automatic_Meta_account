from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup


email = 'nycuimf2@gmail.com'
email_pw = '!23qweasd'

js = "window.open('{}','_bank')"

driver = webdriver.Chrome()
driver.get('https://www.youtube.com/?gl=TW&hl=zh-tw')
driver.execute_script(js.format('https://accounts.google.com/v3/signin/identifier?dsh=S553721998%3A1668583499751536&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%3Ftab%3Drm%26ogbl&emr=1&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%3Ftab%3Drm%26ogbl&osid=1&passive=1209600&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=ARgdvAve47XlYyPuWh-dwRV7yvIaSK4o-mZGnSPkLbvnNHulNWAdmoebkEinOTK7FgkjvQrAm1HLpg#inbox'))
time.sleep(5)
driver.switch_to.window(driver.window_handles[-1])
driver.find_element(By.XPATH, '//*[@id="identifierId"]').send_keys(email)
time.sleep(1)
driver.find_element(
    By.XPATH, '//*[@id="identifierNext"]/div/button/span').click()
time.sleep(5)
driver.find_element(
    By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(email_pw)
time.sleep(1)
driver.find_element(
    By.XPATH, '//*[@id="passwordNext"]/div/button/span').click()
time.sleep(5)
html = driver.find_element(By.XPATH, '//*').get_attribute('outerHTML')
start = html.index('碼：')+2
end = start+5
KEY = html[start:end]
print(KEY)
time.sleep(5)
driver.switch_to.window(driver.window_handles[0])
time.sleep(30)
