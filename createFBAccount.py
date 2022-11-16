import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def main(driver, f_name, l_name, email, pw, bth_y, bth_m, bth_d, sex):
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
    time.sleep(15)
    try:
        driver.find_element(By.CSS_SELECTOR, value="[aria-label=繼續]").click()
    except:
        pass
    time.sleep(20)
    try:
        # driver.find_element(
        #     By.CSS_SELECTOR, ".recaptcha-checkbox-border").click()
        driver.find_element(By.XPATH, "//span[@id='recaptcha-anchor']").click()
    except:
        print('recaptcha-checkbox-border error')
    try:
        driver.find_element(By.CSS_SELECTOR, ".xi112ho").click()
    except:
        print('xi112ho error')
    # driver.find_element(By.ID, "jsc_c_5").send_keys("69562")
    # driver.find_element(By.CSS_SELECTOR, ".xtvsq51 > .x6s0dn4").click()
    # driver.find_elements_by_css_selector()
    time.sleep(5000)


# <div class="x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz xt0b8zv x1qq9wsj x1s688f" role="button" tabindex="0">重新傳送確認碼</div>
if __name__ == '__main__':
    driver = webdriver.Chrome()
    f_name = '浩然'
    l_name = '陳'
    email = 'nycuqq1234@gmail.com'
    pw = 'NYCU1234qq'
    bth_y = 2002
    bth_m = 6
    bth_d = 21
    sex = 'male'
    main(driver, f_name, l_name, email, pw, bth_y, bth_m, bth_d, sex)
