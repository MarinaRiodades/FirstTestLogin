from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage


#classe verificando se conseguiu entrar na home page do site
class HomePage (BasePage):

    def __int__(self):
        self.driver = conftest.driver
        self.page_title = (By.XPATH, "//span[@class = 'title']")


    def verificar_login_sucesso(self):
        self.verificar_se_elemento_existe(self.page_title)

