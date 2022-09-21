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


def test_login():
    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Firefox(
        options=options)
    driver.get('https://pilihjurusan.net/admin')

    email = driver.find_element_by_xpath(
        '//*[@id="input-email"]').send_keys(random_input(5), "@gmail.com")
    pwd = driver.find_element_by_xpath(
        '//*[@id="input-password"]').send_keys(random_input(5))
    login = driver.find_element_by_xpath(
        "/html/body/section/div/div/div[2]/form/div[3]/button").click()
    time.sleep(2)

    email = driver.find_element_by_xpath(
        '//*[@id="input-email"]').send_keys("novanindipradana@gmail.com")
    pwd = driver.find_element_by_xpath(
        '//*[@id="input-password"]').send_keys("cobacoba")
    login = driver.find_element_by_xpath(
        "/html/body/section/div/div/div[2]/form/div[3]/button").click()
    time.sleep(2)
    driver.quit()
