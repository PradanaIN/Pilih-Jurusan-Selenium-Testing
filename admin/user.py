from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import pytest
import time

import string
import random


def get_random_string(length):
    characters = string.ascii_letters
    kalimat = ''.join(random.choice(characters) for i in range(length))
    return kalimat


def test_admin():
    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Firefox(options=options)
    driver.get('https://pilihjurusan.net/admin')

# Login
    email = driver.find_element_by_xpath(
        '//*[@id="input-email"]').send_keys("novanindipradana@gmail.com")
    pwd = driver.find_element_by_xpath(
        '//*[@id="input-password"]').send_keys("cobacoba")
    login = driver.find_element_by_xpath(
        "/html/body/section/div/div/div[2]/form/div[3]/button").click()
    time.sleep(2)

# user
    user = driver.find_element_by_xpath(
        '/html/body/div/div[1]/nav/ul/li[2]/a').click()

# user add
    user_add = driver.find_element_by_xpath(
        '/html/body/div/div[1]/nav/ul/li[2]/ul/li[2]/a').click()
# masukkan info user
    email = driver.find_element_by_xpath(
        '//*[@id="new-email"]').send_keys(get_random_string(5), "@test.com")
    nama = driver.find_element_by_xpath(
        '//*[@id="new-username"]').send_keys(get_random_string(5))
    tgl_lhr = driver.find_element_by_xpath(
        '//*[@id="new-date"]').send_keys("11111111")
    hp = driver.find_element_by_xpath(
        '//*[@id="new-phone-number"]').send_keys(get_random_string(5))
    wa = driver.find_element_by_xpath(
        '//*[@id="new-whatsapp-number"]').send_keys(get_random_string(5))
    sklh = driver.find_element_by_xpath(
        '//*[@id="new-school-name"]').send_keys("test", get_random_string(5))
    kota = driver.find_element_by_xpath(
        '//*[@id="school-city"]').send_keys("test", get_random_string(5))
    prov = driver.find_element_by_xpath(
        '//*[@id="school-province"]').send_keys("test", get_random_string(5))
    pwd = driver.find_element_by_xpath(
        '//*[@id="password"]').send_keys("cobacoba")
    pwd2 = driver.find_element_by_xpath(
        '//*[@id="password_confirm"]').send_keys("cobacoba")
    add = driver.find_element_by_xpath(
        '//*[@id="registration-complete"]').click()
    time.sleep(2)

# user
    user = driver.find_element_by_xpath(
        '/html/body/div/div[1]/nav/ul/li[2]/a').click()

# user list
    user_list = driver.find_element_by_xpath(
        '/html/body/div/div[1]/nav/ul/li[2]/ul/li[1]/a').click()
# mencari user
    # cari_nama = driver.find_elements_by_xpath('//*[@id="name"]').send_keys("coba")
    # cari = driver.find_elements_by_xpath('//*[@id="btn-filter"]').click()

    cari_email = driver.find_elements_by_xpath(
        '//*[@id="email"]').send_keys("test")
    cari = driver.find_elements_by_xpath('//*[@id="btn-filter"]').click()

# customsearch
    cstm = driver.find_elements_by_xpath(
        '/html/body/div/div[2]/section/div/div[4]/div/div[2]/label/input').send_keys("test")

    driver.sleep(2)
    driver.quit()
