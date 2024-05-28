from selenium.webdriver.common.by import By

class PimPage:
    def __init__(self, driver):
        self.driver = driver
        self.pim_menu_option_xpath = (By.XPATH, '//a[@href="/web/index.php/pim/viewPimModule"]')
        self.edit_button_xpath = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[50]/div/div[9]/div/button[2]/i')
        self.firstname_locator = (By.NAME, 'firstName')
        self.lastname_locator = (By.NAME, 'lastName')
        self.save_button_xpath = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button')

    def click_pim_menu(self):
        self.driver.find_element(*self.pim_menu_option_xpath).click()

    def click_edit_button(self):
        self.driver.find_element(*self.edit_button_xpath).click()

    def enter_firstname(self, firstname):
        self.driver.find_element(*self.firstname_locator).send_keys(firstname)

    def enter_lastname(self, lastname):
        self.driver.find_element(*self.lastname_locator).send_keys(lastname)

    def click_save_button(self):
        self.driver.find_element(*self.save_button_xpath).click()
