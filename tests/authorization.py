from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestStellarburgersAuthorization:

    def test_authorization_from_main_valid_user(self, driver):
        url = 'https://stellarburgers.nomoreparties.site/'
        valid_email = '789@mail.ru'
        valid_password = '181927'
        driver.get(url)
        driver.find_element(By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'Вход')]")))
        driver.find_element(By.XPATH, "//main/div/form/fieldset[1]/div/div/input").clear()
        driver.find_element(By.XPATH, "//main/div/form/fieldset[1]/div/div/input").send_keys(valid_email)
        driver.find_element(By.XPATH, "//input[@name='Пароль']").clear()
        driver.find_element(By.XPATH, "//main/div/form/fieldset[2]/div/div/input").send_keys(valid_password)
        driver.find_element(By.XPATH, "//button[contains(text(), 'Войти')]").click()
        WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h1[contains(text(), 'Соберите бургер')]")))
        elm = driver.find_element(By.XPATH,
                                  "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']").text
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/' and elm == 'Оформить заказ'

    def test_authorization_from_main_invalid_password(self, driver):
        url = 'https://stellarburgers.nomoreparties.site/'
        valid_email = '789@mail.ru'
        invalid_password = '18192'
        driver.get(url)
        driver.find_element(By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'Вход')]")))
        driver.find_element(By.XPATH, "//main/div/form/fieldset[1]/div/div/input").clear()
        driver.find_element(By.XPATH, "//main/div/form/fieldset[1]/div/div/input").send_keys(valid_email)
        driver.find_element(By.XPATH, "//input[@name='Пароль']").clear()
        driver.find_element(By.XPATH, "//main/div/form/fieldset[2]/div/div/input").send_keys(invalid_password)
        driver.find_element(By.XPATH, "//button[contains(text(), 'Войти')]").click()
        assert 'Некорректный пароль' in driver.find_element(By.XPATH, "//p[@class='input__error text_type_main-default']").text

    def test_authorization_from_main_invalid_email(self, driver):
        url = 'https://stellarburgers.nomoreparties.site/'
        invalid_email = '789@mail'
        valid_password = '181927'
        driver.get(url)
        driver.find_element(By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'Вход')]")))
        driver.find_element(By.XPATH, "//main/div/form/fieldset[1]/div/div/input").clear()
        driver.find_element(By.XPATH, "//main/div/form/fieldset[1]/div/div/input").send_keys(invalid_email)
        driver.find_element(By.XPATH, "//input[@name='Пароль']").clear()
        driver.find_element(By.XPATH, "//main/div/form/fieldset[2]/div/div/input").send_keys(valid_password)
        driver.find_element(By.XPATH, "//button[contains(text(), 'Войти')]").click()
        driver.implicitly_wait(3)
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    def test_authorization_from_personal_account(self, driver):
        url = 'https://stellarburgers.nomoreparties.site/'
        valid_email = '789@mail.ru'
        valid_password = '181927'
        driver.get(url)
        driver.find_element(By.XPATH, "//p[contains(text(), 'Личный Кабинет')]").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'Вход')]")))
        driver.find_element(By.XPATH, "//main/div/form/fieldset[1]/div/div/input").clear()
        driver.find_element(By.XPATH, "//main/div/form/fieldset[1]/div/div/input").send_keys(valid_email)
        driver.find_element(By.XPATH, "//input[@name='Пароль']").clear()
        driver.find_element(By.XPATH, "//main/div/form/fieldset[2]/div/div/input").send_keys(valid_password)
        driver.find_element(By.XPATH, "//button[contains(text(), 'Войти')]").click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//h1[contains(text(), 'Соберите бургер')]")))
        elm = driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']").text
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/' and elm == 'Оформить заказ'

    def test_authorization_from_registration_form(self,driver):
        url = 'https://stellarburgers.nomoreparties.site/register'
        valid_email = '789@mail.ru'
        valid_password = '181927'
        driver.get(url)
        driver.find_element(By.XPATH, "//a[contains(text(), 'Войти')]").click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'Вход')]")))
        driver.find_element(By.XPATH, "//main/div/form/fieldset[1]/div/div/input").clear()
        driver.find_element(By.XPATH, "//main/div/form/fieldset[1]/div/div/input").send_keys(valid_email)
        driver.find_element(By.XPATH, "//input[@name='Пароль']").clear()
        driver.find_element(By.XPATH, "//main/div/form/fieldset[2]/div/div/input").send_keys(valid_password)
        driver.find_element(By.XPATH, "//button[contains(text(), 'Войти')]").click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//h1[contains(text(), 'Соберите бургер')]")))
        elm = driver.find_element(By.XPATH,
                                  "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']").text
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/' and elm == 'Оформить заказ'

    def test_authorization_from_password_recovery_form(self, driver):
        url = 'https://stellarburgers.nomoreparties.site/login'
        valid_email = '789@mail.ru'
        valid_password = '181927'
        driver.get(url)
        driver.find_element(By.XPATH, "//a[contains(text(), 'Восстановить пароль')]").click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'Войти')]")))
        driver.find_element(By.XPATH, "//a[contains(text(), 'Войти')]").click()
        driver.find_element(By.XPATH, "//main/div/form/fieldset[1]/div/div/input").clear()
        driver.find_element(By.XPATH, "//main/div/form/fieldset[1]/div/div/input").send_keys(valid_email)
        driver.find_element(By.XPATH, "//input[@name='Пароль']").clear()
        driver.find_element(By.XPATH, "//main/div/form/fieldset[2]/div/div/input").send_keys(valid_password)
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//h1[contains(text(), 'Соберите бургер')]")))
        elm = driver.find_element(By.XPATH,
                                  "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']").text
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/' and elm == 'Оформить заказ'
