import conftest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():

#construindo metodos para serem utilizados em toda automacao
    def __int__(self):
        self.driver = conftest.driver

    def encontrar_elemento (self, locator):
        return self.driver.find_element(*locator)

    def encontrar_elementos(self, locator):

       return self.driver.find_elements(*locator)

    def escrever(self, locator, text):
       self.encontrar_elemento(locator).send_keys(text)

    def clicar(self, locator):
        self.encontrar_elemento(locator).click()

    def verificar_se_elemento_existe(self, locator):
        assert self.encontrar_elemento(locator).is_displayed(), f"O elemento '{locator}' não foi encontrado na tela"

    def verificar_se_elemento_nao_existe(self, locator):
        assert self.encontrar_elemento(locator) ==0, f"O elemento '{locator}' não existe, teste 'ok'"

    def esperar_elemento_aparecer(self, locator, timeout =10):
        return WebDriverWait(self.driver,timeout).until(EC.presence_of_element_located(*locator))

    def pegar_texto_do_elemento(self, locator, text):
        self.esperar_elemento_aparecer(locator)
        return self.encontrar_elemento(locator).text

