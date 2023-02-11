from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestStellarburgersConstructor:


    def test_constructor_start_element_is_breads(self, driver):
        url = 'https://stellarburgers.nomoreparties.site/'
        attribute_current = 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'
        driver.get(url)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//span[text() ='Булки']")))
        attribute_breads = driver.find_element(By.XPATH, "//span[text() ='Булки']/parent::div").get_attribute('class')
        assert attribute_breads == attribute_current

    def test_constructor_transition_to_sauses(self, driver):
        url = 'https://stellarburgers.nomoreparties.site/'
        attribute_current = 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'
        driver.get(url)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//span[text() ='Соусы']")))
        driver.find_element(By.XPATH, "//span[text() ='Соусы']").click()
        attribute_souses = driver.find_element(By.XPATH, "//span[text() ='Соусы']/parent::div").get_attribute('class')
        assert attribute_souses == attribute_current

    def test_constructor_transition_to_fillings(self, driver):
        url = 'https://stellarburgers.nomoreparties.site/'
        attribute_current = 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'
        driver.get(url)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//span[text() ='Начинки']")))
        driver.find_element(By.XPATH, "//span[text() ='Начинки']").click()
        attribute_fillings = driver.find_element(By.XPATH, "//span[text() ='Начинки']/parent::div").get_attribute('class')
        assert attribute_fillings == attribute_current

    def test_constructor_transition_from_souses_to_breads(self, driver):
        url = 'https://stellarburgers.nomoreparties.site/'
        attribute_current = 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'
        driver.get(url)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//span[text() ='Соусы']")))
        driver.find_element(By.XPATH, "//span[text() ='Соусы']").click()
        driver.find_element(By.XPATH, "//span[text() ='Булки']").click()
        attribute_breads = driver.find_element(By.XPATH, "//span[text() ='Булки']/parent::div").get_attribute('class')
        assert attribute_breads == attribute_current


        


