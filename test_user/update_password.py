from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pytest
import time


def test_update_pw():
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

    # KLIK ATUR PROFIL
    time.sleep(3)
    profil = driver.find_element_by_css_selector(
        "a#profile-main-menu.text-capitalize.d-flex.justify-content-between")
    profil.click()
    time.sleep(2)
    atur = driver.find_element_by_link_text("Ubah Kata Sandi")
    atur.click()

    # UBAH PASSWORD SENGAJA SALAH
    time.sleep(2)
    pwd = driver.find_element_by_id('password').send_keys(
        'sengajasalah')
    pwd_baru = driver.find_element_by_id('password_new').send_keys(
        'inibaru')
    pwd_bru2 = driver.find_element_by_id('password_confirm').send_keys(
        'inibaru')
    ubah_pwd = driver.find_element_by_id('edit-complete')
    ubah_pwd.click()

    time.sleep(5)
    driver.quit()
