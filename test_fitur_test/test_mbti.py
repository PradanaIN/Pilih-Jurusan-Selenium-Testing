from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import pytest
import time


def test_login_mbti():
    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Firefox(
        options=options)
    # driver.get('https://pilihjurusan.xyz/loginuser')
    driver.get('https://pilihjurusan.net/loginuser')

    # INPUT_LOGIN
    time.sleep(2)
    driver.find_element_by_id('inputEmailAddress').send_keys(
        'coba@test.com')
    driver.find_element_by_id('inputPassword').send_keys(
        'cobacoba')
    masuk = driver.find_element_by_css_selector(
        "button.btn.btn-blue.btn-login.btn-lg.text-uppercase")
    masuk.click()
    time.sleep(2)

    # TEST_MBTI
    mbti = driver.find_element_by_css_selector(
        "div.col-sm:nth-child(2) > div:nth-child(1) > a:nth-child(1) > div:nth-child(1)").click()
    time.sleep(2)
    mulai = driver.find_element_by_css_selector("#test-start").click()
    time.sleep(2)
    cth = driver.find_element_by_css_selector("#test-start").click()
    time.sleep(2)
    cth_soal = driver.find_element_by_xpath(
        "//*[@id='text']/div[1]/label[1]").click()
    mulai_test = driver.find_element_by_css_selector("#test-start").click()

# mulai test dengan memilih jawaban atas semua
    for i in range(56):
        klik = driver.find_element_by_css_selector(
            ".container > div:nth-child(2) > div:nth-child(1) > form:nth-child(1) > div:nth-child(2) > label:nth-child(1)")
        klik.click()
    time.sleep(2)

    # # bawah semua
    # for i in range(56):
    #     klik = driver.find_element_by_css_selector(
    #         "div.row:nth-child(3) > label:nth-child(1)"
    #     )
    #     klik.click()

# result
    result = driver.find_element_by_link_text("View Result").click()
    time.sleep(3)

# RESET TEST
    reset = driver.find_element_by_id("retakeTest").click()
    time.sleep(2)

    # # download hasil
    # pdf = driver.find_element_by_id("reportgen").click()
    # time.sleep(3)
    driver.quit()
