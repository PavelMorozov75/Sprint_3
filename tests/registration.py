from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from faker import Faker

faker = Faker('ru_Ru')
class TestStellarburgersRegisration:
    def test_registation_valid_user(self, driver):
        name = faker.name()
        valid_email = faker.email()
        valid_password = faker.password(length=6, special_chars=True, digits=True, upper_case=True, lower_case=True)
        driver.find_element(By.XPATH, "//main/div/form/fieldset[1]/div/div/input").send_keys(name)
        driver.find_element(By.XPATH, "//main/div/form/fieldset[2]/div/div/input").send_keys(valid_email)
        driver.find_element(By.XPATH, "//main/div/form/fieldset[3]/div/div/input").send_keys(valid_password)
        driver.find_element(By.XPATH, "//button[contains(text(),'Зарегистрироваться')]").click()
        WebDriverWait(driver, 7).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, "//button[contains(text(),'Войти')]")))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    def test_registation_not_valid_password_error(self, driver):
        name = faker.name()
        valid_email = faker.email()
        invalid_password = '22222'
        driver.find_element(By.XPATH, "//main/div/form/fieldset[1]/div/div/input").send_keys(name)
        driver.find_element(By.XPATH, "//main/div/form/fieldset[2]/div/div/input").send_keys(valid_email)
        driver.find_element(By.XPATH, "//main/div/form/fieldset[3]/div/div/input").send_keys(invalid_password)
        driver.find_element(By.XPATH, "//button[contains(text(),'Зарегистрироваться')]").click()
        WebDriverWait(driver, 7).until(expected_conditions.visibility_of_element_located(
                (By.XPATH, "//p[contains(text(),'Некорректный пароль')]")))
        assert 'Некорректный пароль' in driver.find_element(By.XPATH, "//p[@class='input__error text_type_main-default']").text

    def test_registation_not_valid_email_not_registration(self, driver):
        name = faker.name()
        invalid_email = '123'
        valid_password = faker.password(length=6, special_chars=True, digits=True, upper_case=True, lower_case=True)
        driver.find_element(By.XPATH, "//main/div/form/fieldset[1]/div/div/input").send_keys(name)
        driver.find_element(By.XPATH, "//main/div/form/fieldset[2]/div/div/input").send_keys(invalid_email)
        driver.find_element(By.XPATH, "//main/div/form/fieldset[3]/div/div/input").send_keys(valid_password)
        driver.find_element(By.XPATH, "//button[contains(text(),'Зарегистрироваться')]").click()
        driver.implicitly_wait(3)
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/register'

    def test_registation_empty_name_not_registration(self, driver):
        empty_name = ''
        valid_email = faker.email()
        valid_password = faker.password(length=6, special_chars=True, digits=True, upper_case=True, lower_case=True)
        driver.find_element(By.XPATH, "//main/div/form/fieldset[1]/div/div/input").send_keys(empty_name)
        driver.find_element(By.XPATH, "//main/div/form/fieldset[2]/div/div/input").send_keys(valid_email)
        driver.find_element(By.XPATH, "//main/div/form/fieldset[3]/div/div/input").send_keys(valid_password)
        driver.find_element(By.XPATH, "//button[contains(text(),'Зарегистрироваться')]").click()
        driver.implicitly_wait(3)
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/register'

