# BELUM FIX

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pytest
import time
# random
import string
import random

# LOGIN


def test_update_foto():
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

    # DI HOME
    # CLICK PENGATURAN
    time.sleep(2)
    driver.find_element_by_css_selector("i.fas.fa-cog").click()
    time.sleep(2)

    # PILIH FOTO
    upld = driver.find_element_by_xpath(
        "/html/body/div/div[2]/section/div/div[2]/div[3]/form/div[1]/input")
    upld.click()
    upld.click()
    # TIDAK MAU DI KLIK


time.sleep(60)
