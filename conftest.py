import pytest
from selenium import webdriver

driver: webdriver.Remote


# Entrando/ fechando o site e fixando para ser acessado no fluxo de teste
@pytest.fixture()
def setup_teardown():
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    # fechando após todos os testes
    yield
    driver.quit()
    