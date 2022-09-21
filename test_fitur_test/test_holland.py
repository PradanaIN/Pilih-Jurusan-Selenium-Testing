from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import pytest
import time


def test_login_holland():
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

# TEST_Holland
    holland = driver.find_element_by_css_selector(
        "div.col-sm:nth-child(3) > div:nth-child(1) > a:nth-child(1) > div:nth-child(1)").click()
    time.sleep(2)
    mulai = driver.find_element_by_css_selector("#test-start").click()
    time.sleep(2)
    mulai = driver.find_element_by_css_selector("#test-start").click()
    time.sleep(2)

# Test Tahap 1
    for i in range(6):
        checkbox = driver.find_elements_by_xpath(
            '/html/body/div/div[2]/section/div/div[2]/div/form/div[1]/div[1]/input').click()
        next = driver.find_element_by_css_selector(".nextbutton").click()

    time.sleep(3)

    # ERROR LIST HAS NO OBJECT CLICK
