from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_login(driver):
    page = LoginPage(driver)
    page.acessar()
    page.login("user", "pass")
    assert page.sucesso()

    driver.execute_script("window.scrollBy(0, 300);")

    botao = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "meu-botao"))
    )
    botao.click()
