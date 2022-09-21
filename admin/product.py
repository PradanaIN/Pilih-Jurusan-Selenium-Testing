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

# menu prodduk
    product_menu = driver.find_element_by_xpath(
        '/html/body/div/div[1]/nav/ul/li[5]/a').click()

# product add
    product_add = driver.find_element_by_xpath(
        '/html/body/div/div[1]/nav/ul/li[5]/ul/li[2]/a').click()
    nama = driver.find_element_by_xpath(
        '//*[@id="new-token-name"]').send_keys("test")
    links = driver.find_element_by_xpath(
        '//*[@id="token-string"]').send_keys("test")
    desc = driver.find_element_by_xpath(
        '//*[@id="assigned-email"]').send_keys("test")
    add = driver.find_element_by_xpath(
        '/html/body/div/div[2]/section/div/form/div[4]/button').click()

# product list
    product_list = driver.find_element_by_xpath(
        '/html/body/div/div[1]/nav/ul/li[5]/ul/li[1]/a').click()
    time.sleep(2)
    driver.quit()
