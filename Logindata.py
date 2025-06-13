import pytest
from selenium import webdriver
from Login import login  # Assuming login() is in Login.py

@pytest.mark.parametrize(  "username,password", [
    ("Ddttester3@gmail.com", "test@1234"),
    ("testuser1@example.com", "test@1234"),
    ("Ddttester3@gmail.com", "test#123")
])
def test_login(username, password):
    driver = webdriver.Chrome()
    login(driver, username, password)
    driver.quit()