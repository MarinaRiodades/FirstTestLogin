import time
import pytest
from selenium.webdriver.common.by import By
import conftest
from pages.login_page import LoginPage



@pytest.mark.usefixtures("setup_teardown")
class TestLogin:
#fazendo o login na pagina
    def test_login_valido(self):
        self.driver = conftest.driver
        login_page = LoginPage()

        login_page.fazer_login("standard_user", "secret_sauce")
        time.sleep(2)

        assert self.driver.find_element(By.XPATH, "//span[@class = 'title']").is_displayed()

