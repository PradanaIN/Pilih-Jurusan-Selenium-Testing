from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pytest
import time


def test_update_token():
    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    driver.get('https://pilihjurusan.net/loginuser')

    # INPUT-LOGIN
    time.sleep(3)
    email = driver.find_element_by_id('inputEmailAddress').send_keys(
        'VHSJVCKHvchkasvCKHVchkKH@gmail.com')
    pwd = driver.find_element_by_id('inputPassword').send_keys(
        'namakamu')
    masuk = driver.find_element_by_css_selector(
        "button.btn.btn-blue.btn-login.btn-lg.text-uppercase")
    masuk.click()

    # KLIK TOKEN ATAS
    time.sleep(3)
    tkn = driver.find_element_by_link_text(
        "Token")
    tkn.click()
    time.sleep(2)
    # INPUT TOKEN
    update_tkn = driver.find_element_by_id(
        "update-token").send_keys("test_token" + Keys.ENTER)
    time.sleep(3)

    # Kembali Ke Home
    home = driver.find_element_by_link_text("Home")
    home.click()
    time.sleep(2)

    # KLIK UPDATE TOKEN SAMPING
    menu = driver.find_element_by_link_text("Menu")
    menu.click()
    time.sleep(2)
    tkn_baru = driver.find_element_by_css_selector(
        "#update-token-menu > li:nth-child(1) > a")
    tkn_baru.click()
    # INPUT TOKEN
    update_tkn = driver.find_element_by_id(
        "update-token").send_keys("test_token")
    time.sleep(1)
    submit = driver.find_element_by_css_selector("#update-token-btn")
    submit.click()

    time.sleep(5)
    driver.quit()
