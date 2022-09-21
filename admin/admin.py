from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import pytest
import time

import string
import random


def random_input(length):
    characters = string.ascii_letters
    kalimat = ''.join(random.choice(characters) for i in range(length))
    return kalimat


def test_admin():
    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Firefox(
        options=options)
    driver.get('https://pilihjurusan.net/admin')

# Login
    email = driver.find_element_by_xpath(
        '//*[@id="input-email"]').send_keys("novanindipradana@gmail.com")
    pwd = driver.find_element_by_xpath(
        '//*[@id="input-password"]').send_keys("cobacoba")
    login = driver.find_element_by_xpath(
        "/html/body/section/div/div/div[2]/form/div[3]/button").click()
    time.sleep(2)

# Admin add
    admin = driver.find_element_by_xpath(
        '/html/body/div/div[1]/nav/ul/li[1]/a').click()
    admin_add = driver.find_element_by_xpath(
        '/html/body/div/div[1]/nav/ul/li[1]/ul/li[2]/a').click()
    time.sleep(2)
# masukkan info
    nama = driver.find_element_by_xpath(
        '//*[@id="new-name"]').send_keys(random_input(5))
    email = driver.find_element_by_xpath(
        '//*[@id="new-email"]').send_keys(random_input(5), "@gmail.com")
    pwd = driver.find_element_by_xpath(
        '//*[@id="password"]').send_keys("cobacoba")
    pwd2 = driver.find_element_by_xpath(
        '//*[@id="password_confirm"]').send_keys("cobacoba")
    add = driver. find_element_by_xpath(
        '//*[@id="registration-complete"]').click()
    time.sleep(2)

# admin list
    adm_list = driver.find_element_by_xpath(
        '/html/body/div/div[1]/nav/ul/li[1]/ul/li[1]/a').click()
# edit
    adm_edit = driver.find_element_by_xpath(
        '/html/body/div/div[2]/section/div/div[2]/div/div[4]/table/tbody/tr[3]/td[4]/div/a/button').click()
    nama = driver.find_element_by_xpath(
        '//*[@id="new-name"]').send_keys(random_input(5))
    email = driver.find_element_by_xpath(
        '//*[@id="new-email"]').send_keys(random_input(5), "@gmail.com")
    pwd = driver.find_element_by_xpath(
        '//*[@id="password"]').send_keys("cobacoba")
    pwd2 = driver.find_element_by_xpath(
        '//*[@id="password_confirm"]').send_keys("cobacoba")
    save = driver. find_element_by_xpath(
        '//*[@id="registration-complete"]').click()
    time.sleep(2)
# delete_admin
    adm_del = driver.find_element_by_xpath('//*[@id="delete"]').click()
    time.sleep(2)
    driver.quit()
