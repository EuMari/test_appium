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
        desired_caps['app'] = PATH('ApiDemos-debug.apk')
        desired_caps['udid'] = 'localhost:43515'  #uzupelnic nr hosta
        desired_caps['appPackage'] = 'io.appium.android.apis'
        desired_caps['appActivity'] = 'io.appium.android.apis.ApiDemos'

        # connect to Appium
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_form_app(self):
        #self.driver.is_app_installed('com.example.android.contactmanager')
        self.driver.find_element_by_accessibility_id('Preference').click()
        self.driver.find_element_by_accessibility_id('3. Preference dependencies').click()

        checkboxes = self.driver.find_elements_by_android_uiautomator('new UiSelector().checkable(true)')

        for el in checkboxes:
            is_checked_value = self.driver.find_element_by_class_name('android.widget.CheckBox').get_attribute("checked")
            if is_checked_value == 'true':
                print('checkboxy sa zaznaczone')
            else:
                el.click()

                passwordInput = "1234"

                self.driver.find_element_by_xpath('//*[@text="WiFi settings"]').click()
                self.driver.find_element_by_class_name("android.widget.EditText").send_keys(passwordInput)

                passwordCurrent = self.driver.find_element_by_class_name("android.widget.EditText").get_attribute("text")
                self.assertEqual(passwordInput,passwordCurrent)

                self.driver.find_element_by_id('android:id/button1').click()

                self.driver.back()
                self.driver.keyevent(4)





        sleep(3)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestingApp)
    unittest.TextTestRunner(verbosity=2).run(suite)