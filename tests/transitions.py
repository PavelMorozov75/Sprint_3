from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestStellarburgersTransitions:

    def test_transition_from_main_to_personal_account_authorozed_user(self, driver_authorized):
        driver_authorized.find_element(By.XPATH, "//p[contains(text(), 'Личный Кабинет')]").click()
        WebDriverWait(driver_authorized, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Сохранить')]")))
        assert driver_authorized.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

    def test_transition_from_personal_account_to_constructor(self, driver_authorized):
        driver_authorized.find_element(By.XPATH, "//p[contains(text(), 'Личный Кабинет')]").click()
        WebDriverWait(driver_authorized,3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'Конструктор')]")))
        driver_authorized.find_element(By.XPATH, "//p[contains(text(), 'Конструктор')]").click()
        WebDriverWait(driver_authorized, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h1[contains(text(), 'Соберите бургер')]")))
        elm = driver_authorized.find_element(By.XPATH,
                                  "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']").text
        assert driver_authorized.current_url == 'https://stellarburgers.nomoreparties.site/' and elm == 'Оформить заказ'

    def test_transition_from_personal_account_to_constructor_click_on_logo(self, driver_authorized):
        driver_authorized.find_element(By.XPATH, "//p[contains(text(), 'Личный Кабинет')]").click()
        WebDriverWait(driver_authorized, 3).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "div > a > svg")))
        driver_authorized.find_element(By.CSS_SELECTOR, "div > a > svg").click()
        WebDriverWait(driver_authorized, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//h1[contains(text(), 'Соберите бургер')]")))
        elm = driver_authorized.find_element(By.XPATH,
                                             "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']").text
        assert driver_authorized.current_url == 'https://stellarburgers.nomoreparties.site/' and elm == 'Оформить заказ'