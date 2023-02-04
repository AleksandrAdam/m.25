from selenium import webdriver
import pytest


@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome('C:\\WebDriver\\bin\\chromedriver.exe')

   pytest.driver.set_window_size(1000, 1000)
   # Переход на страницу авторизации пользователя
   pytest.driver.get('https://petfriends.skillfactory.ru/login')

   yield


   pytest.driver.quit()

