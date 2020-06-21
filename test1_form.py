import os
import unittest
from appium import webdriver
from time import sleep


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__),p)
)

class TestingApp(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        #desired_caps['platformVersion'] = '8.0' tak sie robi, jak jest fizyczny telefon
        desired_caps['deviceName'] = 'Genymotion Cloud'
        desired_caps['app'] = PATH('ContactManager.apk')
        desired_caps['udid'] = 'localhost:43515'  #uzupelnic nr hosta
        desired_caps['appPackage'] = 'com.example.android.contactmanager'
        desired_caps['appActivity'] = 'com.example.android.contactmanager.ContactManager'

        # connect to Appium
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_form_app(self):
        self.driver.is_app_installed('com.example.android.contactmanager')
        self.driver.find_element_by_class_name('android.widget.Button').click()
        #self.driver.find_element_by_id('contactName').send_keys('Anna')
        sleep(3)
        textfields = self.driver.find_elements_by_class_name('android.widget.EditText')
        textfields[0].send_keys("Anna")
        textfields[1].send_keys("981071470")
        textfields[2].send_keys("anna@wsb.pl")
        sleep(2)

        self.assertTrue(textfields[0],"Anna")
        self.assertTrue(textfields[1],"981071470")
        self.assertTrue(textfields[2],"anna@wsb.pl")

        self.driver.find_element_by_id('com.example.android.contactmanager:id/contactSaveButton').click()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestingApp)
    unittest.TextTestRunner(verbosity=2).run(suite)