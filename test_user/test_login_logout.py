from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pytest
import time


def test_login_():
    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    driver.get('https://pilihjurusan.net/loginuser')

    # INPUT LOGIN
    time.sleep(3)
    driver.find_element_by_id('inputEmailAddress').send_keys(
        'VHSJVCKHvchkasvCKHVchkKH@gmail.com')
    driver.find_element_by_id('inputPassword').send_keys(
        'namakamu')
    masuk = driver.find_element_by_css_selector(
        "button.btn.btn-blue.btn-login.btn-lg.text-uppercase")
    masuk.click()
    time.sleep(3)

    # LOG OUT
    keluar = driver.find_element_by_link_text("Keluar")
    keluar.click()
    time.sleep(3)

    # INPUT LOGIN 2
    driver.find_element_by_id('inputEmailAddress').send_keys(
        'VHSJVCKHvchkasvCKHVchkKH@gmail.com')
    driver.find_element_by_id('inputPassword').send_keys(
        'namakam')
    masuk = driver.find_element_by_css_selector(
        "button.btn.btn-blue.btn-login.btn-lg.text-uppercase")
    masuk.click()
    time.sleep(3)
    driver.find_element_by_id('inputEmailAddress').send_keys(
        'VHSJVCKHvchkasvCKHVchkKH@gmail.com')
    driver.find_element_by_id('inputPassword').send_keys(
        'namakamu')
    masuk = driver.find_element_by_css_selector(
        "button.btn.btn-blue.btn-login.btn-lg.text-uppercase")
    masuk.click()
    time.sleep(3)
    driver.quit()
