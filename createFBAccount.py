import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


def email():
    pass
# https://pythonprogramminglanguage.com/read-gmail-using-python/


def emailGetKey(driver, email, email_pw):
    js = "window.open('{}','_bank')"
    driver.execute_script(js.format('https://accounts.google.com/v3/signin/identifier?dsh=S553721998%3A1668583499751536&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%3Ftab%3Drm%26ogbl&emr=1&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%3Ftab%3Drm%26ogbl&osid=1&passive=1209600&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=ARgdvAve47XlYyPuWh-dwRV7yvIaSK4o-mZGnSPkLbvnNHulNWAdmoebkEinOTK7FgkjvQrAm1HLpg#inbox'))
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[-1])
    driver.find_element(
        By.XPATH, '//*[@id="identifierId"]').send_keys(email[:-2])
    time.sleep(1)
    driver.find_element(
        By.XPATH, '//*[@id="identifierId"]').send_keys(email[-2:])
    time.sleep(2)
    driver.find_element(
        By.XPATH, '//*[@id="identifierNext"]/div/button/span').click()
    time.sleep(5)
    driver.find_element(
        By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(email_pw[:-2])
    time.sleep(1)
    driver.find_element(
        By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(email_pw[-2:])
    time.sleep(2)
    driver.find_element(
        By.XPATH, '//*[@id="passwordNext"]/div/button/span').click()
    time.sleep(5)
    html = driver.find_element(By.XPATH, '//*').get_attribute('outerHTML')
    start = html.index('FB-')+3
    end = start+5
    KEY = html[start:end]
    driver.switch_to.window(driver.window_handles[0])
    return driver, KEY


def main(driver, f_name, l_name, email, email_pw, pw, bth_y, bth_m, bth_d, sex):
    login_url = 'https://zh-tw.facebook.com/reg/'
    driver.get(login_url)
    # input first name
    driver.find_element(By.NAME, "firstname").send_keys(f_name)
    # input last name
    driver.find_element(By.NAME, "lastname").send_keys(l_name)
    # input phone or email
    driver.find_element(By.NAME, "reg_email__").send_keys(email)
    # input phone or email again(if exist)
    time.sleep(0.5)
    try:
        driver.find_element(
            By.NAME, "reg_email_confirmation__").send_keys(email)
    except:
        pass
    # input password
    driver.find_element(By.NAME, "reg_passwd__").send_keys(pw)
    # choose birth year
    dropdown = driver.find_element(By.ID, "year")
    dropdown.find_element(By.XPATH, f"//option[. = '{bth_y}']").click()
    # choose birth month
    dropdown = driver.find_element(By.ID, "month")
    dropdown.find_element(By.XPATH, f"//option[. = '{bth_m} 月']").click()
    # choose birth day
    dropdown = driver.find_element(By.ID, "day")
    dropdown.find_element(By.XPATH, f"//option[. = '{bth_d}']").click()
    # choose sex
    if sex == 'male':
        driver.find_element(
            By.CSS_SELECTOR, ".\\_5k_2:nth-child(2) > .\\_58mt").click()
    else:
        driver.find_element(
            By.CSS_SELECTOR, ".\\_5k_2:nth-child(1) > .\\_58mt").click()
    # click submit btn
    driver.find_element(By.NAME, "websubmit").click()
    time.sleep(5)
    try:
        driver.find_element(By.CSS_SELECTOR, value="[aria-label=繼續]").click()
    except:
        pass
    try:
        WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it(
            (By.CSS_SELECTOR, 'iframe[id="captcha-recaptcha"]')))
        WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it(
            (By.CSS_SELECTOR, 'iframe[title="reCAPTCHA"]')))
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, "//div[@class='recaptcha-checkbox-border']"))).click()
        driver.switch_to.default_content()
        driver.switch_to.default_content()
        driver.find_element(
            By.XPATH, '//*[@id="scrollview"]/div/div/div/div[2]/div/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div/div/div[3]/div/div/div/div').click()
    except:
        pass
    # driver.find_elements_by_css_selector()
    driver, KEY = emailGetKey(driver, email, email_pw)
    driver.find_element(By.NAME, "code").send_keys(KEY)
    driver.find_element(By.NAME, "confirm").click()
    # except:
    #     pass
    time.sleep(5000)


# <div class="x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz xt0b8zv x1qq9wsj x1s688f" role="button" tabindex="0">重新傳送確認碼</div>
if __name__ == '__main__':
    driver = webdriver.Chrome()
    f_name = '浩婷'
    l_name = '張'
    # email = 'nycuqq1234@gmail.com'
    email = 'testimf2022.2@gmail.com'
    email_pw = 'fef3554r4321'
    pw = 'fef3554r4321'
    bth_y = 2002
    bth_m = 6
    bth_d = 21
    sex = 'female'
    main(driver, f_name, l_name, email, email_pw, pw, bth_y, bth_m, bth_d, sex)


# https://www.facebook.com/r.php?locale=zh_TW&display=page


# 7.FB帳號久存原則

# 申請完帳號 塗鴉牆留個訊息 放三天

# 開始加友 第一次 加10個就好 隔2~3天

# 第二次以上加友 可以加到20個 但點好友數度要慢 如 123 停 456 停 ......20

# 不要加看起像廣告的帳號 如 美的不像話的女生

# 以共同好友數多的先加

# 帳號數越多 間隔加友時間越長 越好

# 每次加友前 先寫寫塗鴉牆 按按 朋友的 讚 再開始加友

# testimf2022.2@gmail.com
# fef3554r4321
