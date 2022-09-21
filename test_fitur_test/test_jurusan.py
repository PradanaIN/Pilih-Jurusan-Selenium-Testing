from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import pytest
import time


def test_login_jurusan_ipa_ips():
    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Firefox(
        options=options)
    # driver.get('https://pilihjurusan.xyz/loginuser')
    driver.get('https://pilihjurusan.net/loginuser')

    # INPUT_LOGIN
    time.sleep(2)
    driver.find_element_by_id('inputEmailAddress').send_keys(
        'coba@test.com')
    driver.find_element_by_id('inputPassword').send_keys(
        'cobacoba')
    masuk = driver.find_element_by_css_selector(
        "button.btn.btn-blue.btn-login.btn-lg.text-uppercase")
    masuk.click()
    time.sleep(2)

# TEST_JURUSAN_IPA_IPS
    jur = driver.find_element_by_css_selector(
        "div.col-sm:nth-child(5) > div:nth-child(1) > a:nth-child(1) > div:nth-child(1)").click()
    time.sleep(2)
    cth = driver.find_element_by_css_selector("#test-start").click()
    time.sleep(2)
    cth_soal = driver.find_element_by_xpath(
        '//*[@id="radiobuttonid1"]').click()
    mulai_test = driver.find_element_by_css_selector("#test-start").click()

# KLIK PILIH AWAL SEMUA (Sangat Tidak Setuju)
    for i in range(80):
        klik = driver.find_element_by_css_selector(
            ".container > div:nth-child(2) > div:nth-child(1) > form:nth-child(1) > div:nth-child(2)")
        klik.click()
    time.sleep(3)

    # # Tidak Setuju
    # for i in range(80):
    #     klik = driver.find_element_by_css_selector(
    #         "div.row:nth-child(3) > label:nth-child(1)"
    #     )
    #     klik.click()

    # # Setuju
    # for i in range(80):
    #     klik = driver.find_element_by_css_selector(
    #         "div.row:nth-child(4) > label:nth-child(1)"
    #     )
    #     klik.click()

    # # Sangat Setuju
    # for i in range(80):
    #     klik = driver.find_element_by_css_selector(
    #         "div.row:nth-child(5) > label:nth-child(1)"
    #     )
    #     klik.click()


# RESULT
    result = driver.find_element_by_link_text("View Result").click()
    time.sleep(3)

# # RESET TEST
#     reset = driver.find_element_by_id("retakeTest").click()
#     time.sleep(2)

#     # # download hasil
#     # pdf = driver.find_element_by_id("reportgen").click()
#     # time.sleep(3)
#     driver.quit()
