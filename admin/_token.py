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

# token menu
    token_menu = driver.find_element_by_xpath(
        '/html/body/div/div[1]/nav/ul/li[3]/a').click()

# token_add
    token_add = driver.find_element_by_xpath(
        '/html/body/div/div[1]/nav/ul/li[3]/ul/li[2]/a').click()
    name = driver.find_element_by_xpath(
        '//*[@id="new-token-name"]').send_keys('test')
    tkn_str = driver.find_element_by_xpath(
        '//*[@id="token-string"]').send_keys('test')
    tkn_type = driver.find_element_by_xpath(
        '//*[@id="token-type"]').send_keys('test')
    tkn_id = driver.find_element_by_xpath(
        '//*[@id="test-ids"]').send_keys('test')
    qty = driver.find_element_by_xpath('//*[@id="qty"]').send_keys(1)
    asign_email = driver.find_element_by_xpath(
        '//*[@id="assigned-email"]').send_keys('tester@test.com')
    time_stamp = driver.find_element_by_xpath(
        '//*[@id="start-timestamp-date"]').send_keys('01012021')
    end_stamp = driver.find_element_by_xpath(
        '//*[@id="end-timestamp-date"]').send_keys('03032022')
    add = driver.find_element_by_xpath(
        '/html/body/div/div[2]/section/div/form/div[7]/button').click()
# token_list
    token_list = driver.find_element_by_xpath(
        '/html/body/div/div[1]/nav/ul/li[3]/ul/li[1]/a').click()
    time.sleep(2)
    driver.quit()
