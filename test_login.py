import pytest
from pages.login_page import LoginPage

def test_login(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login_page = LoginPage(driver)
    login_page.enter_username('Admin')
    login_page.enter_password('admin123')
    login_page.click_login()
    # Add assertions to verify successful login
