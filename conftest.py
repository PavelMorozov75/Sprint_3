import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture()
def driver():
    url = 'https://stellarburgers.nomoreparties.site/register'
    options = Options()
    options.add_argument("--window-size=1200,600")
    browser_driver = webdriver.Chrome(options=options)
    browser_driver.get(url)
    yield browser_driver
    browser_driver.quit()

@pytest.fixture()
def driver_authorized():
    url = 'https://stellarburgers.nomoreparties.site/'
    valid_email = '789@mail.ru'
    valid_password = '181927'
    options = Options()
    options.add_argument("--window-size=1200,600")
    browser_driver = webdriver.Chrome(options=options)
    browser_driver.get(url)
    browser_driver.find_element(By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]").click()
    WebDriverWait(browser_driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'Вход')]")))
    browser_driver.find_element(By.XPATH, "//main/div/form/fieldset[1]/div/div/input").clear()
    browser_driver.find_element(By.XPATH, "//main/div/form/fieldset[1]/div/div/input").send_keys(valid_email)
    browser_driver.find_element(By.XPATH, "//input[@name='Пароль']").clear()
    browser_driver.find_element(By.XPATH, "//main/div/form/fieldset[2]/div/div/input").send_keys(valid_password)
    browser_driver.find_element(By.XPATH, "//button[contains(text(), 'Войти')]").click()
    WebDriverWait(browser_driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")))

    yield browser_driver
    browser_driver.quit()