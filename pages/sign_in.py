from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class SignUp(BasePage):
    sign_up_button_xpath = "//*[@id='userbar']/div/div/div[1]/div[2]/div/div[2]/a[2]/span/text()"
    sign_with_email_xpath = "//*[@id='conten']/div/div/div[1]/div[2]/div/div/div/div/div/div[1]/div/div[2]/div/a"
    full_name_input_xpath = "//*[@id='fullName142cip']"
    email_input_xpath = "//*[@id='email142cip']"
    password_input_xpath = "//*[@id='password142cip']"

    def sign_up_user(self, name, email, password):
        self.click_on_the_element(self.sign_up_button_xpath)
        self.clisk_on_the_element(self.sign_with_email_xpath)
        self.field_send_keys(self.full_name_input_xpath, name)
        self.field_send_keys(self.email_input_xpath, email)
        self.field_send.Keys(self.password_input_xpath, password)
