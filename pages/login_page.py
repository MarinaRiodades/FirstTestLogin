from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage


class LoginPage(BasePage):
#construindo metodos para serem utilizados no login
    def __int__(self):
        self.texto_encontrado = None

    def __init__(self):
        self.driver = conftest.driver

        # locations
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_massage_login = (By.XPATH, "//h3[@data-test = 'error']")

    def fazer_login(self, usuario, senha):
        self.escrever(self.username_field, usuario)
        self.escrever(self.password_field, senha)
        self.clicar(self.login_button)

    def verificar_mensagem_erro_login_existe(self):
        self.verificar_se_elemento_existe(self.error_massage_login)

