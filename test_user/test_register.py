# REGISTER BELUM FIX KARENA CHECKBOX TIDAK MAU TERKLIK OTOMATIS

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import pytest
import time

# random
import string
import random


# buat random inputan mendaftar


def random_input(length):
    characters = string.ascii_letters
    kalimat = ''.join(random.choice(characters) for i in range(length))
    return kalimat


def test_signup():
    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Firefox(
        options=options)
    driver.get('https://pilihjurusan.xyz/loginuser')

    # klik_signup
    time.sleep(2)
    daftar = driver.find_element_by_link_text("Sign Up")
    daftar.click()

    # masukkan_token
    # SALAH
    input_token = driver.find_element_by_xpath(
        '//*[@id="update-token"]').send_keys(random_input(5))
    validasi_token = driver.find_element_by_xpath(
        '//*[@id="update-token-btn"]').click()
    # BENAR
    input_token = driver.find_element_by_xpath(
        '//*[@id="update-token"]').send_keys("sample")
    validasi_token = driver.find_element_by_xpath(
        '//*[@id="update-token-btn"]').click()
    time.sleep(3)

    # # input_data_pendaftaran_akun
    # time.sleep(2)
    # email = driver.find_element_by_id(
    #     "new-email").send_keys(get_random_string(10) + '@gmail.com')
    # nama = driver.find_element_by_id(
    #     "new-username").send_keys(get_random_string(15))
    # date = driver.find_element_by_id(
    #     "new-date").send_keys('01012000')
    # hape = driver.find_element_by_id(
    #     "new-phone-number").send_keys(get_random_string(15))
    # wa = driver.find_element_by_id(
    #     "new-whatsapp-number").send_keys(get_random_string(15))
    # # tingkat_sekolah(?)
    # sklh = driver.find_element_by_id(
    #     "new-school-name").send_keys('test_', get_random_string(15))
    # # kelas
    # # jur = driver.find_element_by_id("degree")
    # kota = driver.find_element_by_id(
    #     "school-city").send_keys('test_', get_random_string(15))
    # prov = driver.find_element_by_id(
    #     "school-province").send_keys('test_', get_random_string(15))
    # pw = driver.find_element_by_id("password").send_keys('logindulu')
    # pwc = driver.find_element_by_id(
    #     "password_confirm").send_keys('logindulu')
    # centang = driver.find_element_by_xpath(
    #     '//*[@id="terms-checkbox"]').click()
    # # daftar = driver.find_elements_by_css_selector("button#registration-complete.btn.btn-blue.btn-login.btn-lg.text-capitalize")
    # # daftar.click()
    # time.sleep(5)
    # driver.quit()
