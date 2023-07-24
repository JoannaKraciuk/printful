import os
import unittest
from selenium import webdriver

from pages.sign_in import SignUp
from utils.settings import DRIVER_PATH, IMPLICITY_WAIT


class TestSignUpPage(unittest.TestCase):

    @classmethod
    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://www.printful.com/ca')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_sign_up_page(self):
        sign_up = SignUp(self.driver)

        sign_up.sign_up_user("Emilia", "emi@gmail.com", "Test_1234!")