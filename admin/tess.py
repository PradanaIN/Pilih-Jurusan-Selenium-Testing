from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import pytest
import time


def test_token():
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

# menu tes
    tes_menu = driver.find_element_by_xpath(
        '/html/body/div/div[1]/nav/ul/li[4]/a').click()

# add tes
    tes_add = driver.find_element_by_xpath(
        '/html/body/div/div[1]/nav/ul/li[4]/ul/li[2]/a').click()

# tes list
    tes_list = driver.find_element_by_xpath(
        '/html/body/div/div[1]/nav/ul/li[4]/ul/li[1]/a').click()

    time.sleep(2)
    driver.quit()
