from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestStellarburgersExit:
    def test_exit_from_personal_account_authorozed_user(self, driver_authorized):
        driver_authorized.find_element(By.XPATH, "//p[contains(text(), 'Личный Кабинет')]").click()
        WebDriverWait(driver_authorized, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Сохранить')]")))
        driver_authorized.find_element(By.XPATH, "//button[contains(text(), 'Выход')]").click()
        WebDriverWait(driver_authorized, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'Вход')]")))
        assert driver_authorized.current_url == 'https://stellarburgers.nomoreparties.site/login'