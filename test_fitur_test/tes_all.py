from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import pytest
import time


def test_login():
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

    # 1.TEST_MBTI
    mbti = driver.find_element_by_css_selector(
        "div.col-sm:nth-child(2) > div:nth-child(1) > a:nth-child(1) > div:nth-child(1)").click()
    mulai = driver.find_element_by_css_selector("#test-start").click()
    cth = driver.find_element_by_css_selector("#test-start").click()
    cth_soal = driver.find_element_by_xpath(
        "//*[@id='text']/div[1]/label[1]").click()
    mulai_test = driver.find_element_by_css_selector("#test-start").click()
    # mulai test dengan memilih jawaban atas semua
    for i in range(56):
        klik = driver.find_element_by_css_selector(
            ".container > div:nth-child(2) > div:nth-child(1) > form:nth-child(1) > div:nth-child(2) > label:nth-child(1)")
        klik.click()
    # result MBTI
    result = driver.find_element_by_link_text("View Result").click()
    time.sleep(2)

    # 2. Tes Jurusan
    halaman_utama = driver.find_element_by_xpath(
        '/html/body/nav/div[1]/div[2]/div/ul/li[1]/a').click()
    jur = driver.find_element_by_css_selector(
        "div.col-sm:nth-child(5) > div:nth-child(1) > a:nth-child(1) > div:nth-child(1)").click()
    cth = driver.find_element_by_css_selector("#test-start").click()
    cth_soal = driver.find_element_by_xpath(
        '//*[@id="radiobuttonid1"]').click()
    mulai_test = driver.find_element_by_css_selector("#test-start").click()
    # KLIK PILIH AWAL SEMUA (Sangat Tidak Setuju)
    for i in range(80):
        klik = driver.find_element_by_css_selector(
            ".container > div:nth-child(2) > div:nth-child(1) > form:nth-child(1) > div:nth-child(2)")
        klik.click()

    result = driver.find_element_by_link_text("View Result").click()
    time.sleep(2)

    # 3. Tes Kemampuan Kerja
    halaman_utama = driver.find_element_by_xpath(
        '/html/body/nav/div[1]/div[2]/div/ul/li[1]/a').click()
    kk = driver.find_element_by_css_selector(
        "div.col-sm:nth-child(4) > div:nth-child(1) > a:nth-child(1) > div:nth-child(1)").click()
    mulai = driver.find_element_by_css_selector("#test-start").click()
    # KLIK PILIHAN PERTAMA
    for i in range(24):
        klik = driver.find_element_by_css_selector(
            ".container > div:nth-child(2) > div:nth-child(1) > form:nth-child(1) > div:nth-child(2) > label:nth-child(1)")
        klik.click()

    result = driver.find_element_by_link_text("View Result").click()
    time.sleep(2)

    # 4. Tes Holland_Riasec
    halaman_utama = driver.find_element_by_xpath(
        '/html/body/nav/div[1]/div[2]/div/ul/li[1]/a').click()
    Holland_R = driver.find_element_by_css_selector(
        "div.col-sm:nth-child(6) > div:nth-child(1) > a:nth-child(1) > div:nth-child(1)").click()
    cth = driver.find_element_by_css_selector("#test-start").click()
    cth_soal = driver.find_element_by_xpath(
        '//*[@id="radiobuttonid1"]').click()
    mulai_test = driver.find_element_by_css_selector("#test-start").click()
    # KLIK PILIH AWAL SEMUA (Sangat Tidak Setuju)
    for i in range(60):
        klik = driver.find_element_by_css_selector(
            ".container > div:nth-child(2) > div:nth-child(1) > form:nth-child(1) > div:nth-child(2)")
        klik.click()

    result = driver.find_element_by_link_text("View Result").click()
    time.sleep(2)

    # 5. Tes IQ
    halaman_utama = driver.find_element_by_xpath(
        '/html/body/nav/div[1]/div[2]/div/ul/li[1]/a').click()
    IQ = driver.find_element_by_css_selector(
        ".mb-1 > div:nth-child(1) > div:nth-child(1) > a:nth-child(1) > div:nth-child(1)").click()
    cth = driver.find_element_by_css_selector(".btn").click()
    cth_soal = driver.find_element_by_xpath(
        '//*[@id="radiobuttonid3"]').click()
    mulai_test = driver.find_element_by_css_selector("button.btn").click()
    cth_soal_2 = driver.find_element_by_xpath(
        '//*[@id="radiobuttonid4"]').click()
    cth_soal_3 = driver.find_element_by_xpath(
        '//*[@id="radiobuttonid2_2"]').click()
    mulai_test = driver.find_element_by_css_selector("button.btn").click()

    # KLIK PILIH AWAL SEMUA
    for i in range(40):
        klik = driver.find_element_by_xpath(
            '//*[@id="radiobuttonid1"]').click()
        next = driver.find_element_by_xpath(
            "/html/body/div[1]/div[2]/section/div/div/div/form/div[5]/div[2]/button").click()

    result = driver.find_element_by_link_text("View Result").click()
    time.sleep(2)

    # 6. Tes Holland
    halaman_utama = driver.find_element_by_xpath(
        '/html/body/nav/div[1]/div[2]/div/ul/li[1]/a').click()
    holland = driver.find_element_by_css_selector(
        "div.col-sm:nth-child(3) > div:nth-child(1) > a:nth-child(1) > div:nth-child(1)").click()
    # mulai = driver.find_element_by_css_selector("#test-start").click()
    # time.sleep(2)
    # mulai = driver.find_element_by_css_selector("#test-start").click()
    # time.sleep(2)

    # Test Tahap 1
    # for i in range(6):
    #    checkbox = driver.find_elements_by_xpath(
    #        '/html/body/div/div[2]/section/div/div[2]/div/form/div[1]/div[1]/input').click()
    #    next = driver.find_element_by_css_selector(".nextbutton").click()

    # ERROR ERROR ERROR

    # ERROR LIST HAS NO OBJECT ATTRIBUTE CLICK
    # opsi checkbox tidak bisa di klik secara otomatis pada tes holland ini

    # pada semua tes, opsi remove report and retake tes ALERT OK tidak bisa secara otomatis
    # belum menemukan problem solvenya

    time.sleep(2)
    driver.quit()
