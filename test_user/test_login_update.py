# Tes Ini untuk login, kemudian update data

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pytest
import time
# random
import string
import random


def get_random_string(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    kalimat = ''.join(random.choice(characters) for i in range(length))
    return kalimat

# LOGIN


def test_login_sample():
    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    driver.get('https://pilihjurusan.net/loginuser')

    # INPUT
    time.sleep(3)
    driver.find_element_by_id('inputEmailAddress').send_keys(
        'VHSJVCKHvchkasvCKHVchkKH@gmail.com')
    driver.find_element_by_id('inputPassword').send_keys(
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
    atur = driver.find_element_by_link_text("Atur Profil")
    atur.click()

    # UPDATE DATA
    time.sleep(2)
    update_nama = driver.find_element_by_css_selector(
        "input#new-username.form-control.my-2.p-2.input-border").send_keys(get_random_string(5))
    update_hp = driver.find_element_by_css_selector(
        "input#new-phone-number.form-control.my-2.p-2.input-border").send_keys(get_random_string(5))
    update_wa = driver.find_element_by_css_selector(
        "input#new-whatsapp-number.form-control.my-2.p-2.input-border").send_keys(get_random_string(5))
    update_sklh = driver.find_element_by_css_selector(
        "input#new-school-name.form-control.my-2.p-2.input-border").send_keys(get_random_string(5))
    update_jur = driver.find_element_by_css_selector(
        "input#degree.form-control.my-1.p-2.input-border").send_keys(get_random_string(5))
    update_kota = driver.find_element_by_id(
        "school-city").send_keys(get_random_string(5))
    update_prov = driver.find_element_by_id(
        "school-province").send_keys(get_random_string(5) + Keys.ENTER)

    time.sleep(3)
    back()
    forward()
    time.sleep(3)
    driver.quit()
