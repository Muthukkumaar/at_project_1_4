import pytest
from pages.login_page import LoginPage
from pages.pim_page import PimPage

def test_edit_employee(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login_page = LoginPage(driver)
    login_page.enter_username('Admin')
    login_page.enter_password('admin123')
    login_page.click_login()
    
    pim_page = PimPage(driver)
    pim_page.click_pim_menu()
    pim_page.click_edit_button()
    pim_page.enter_firstname('murugann')
    pim_page.enter_lastname('moorthi')
    pim_page.click_save_button()
    # Add assertions to verify the changes were saved successfully
