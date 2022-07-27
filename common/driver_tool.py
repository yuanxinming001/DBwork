from appium import webdriver as app
from selenium.webdriver.common.by import By


class DriverTool(object):
    # app打开的会话
    app_driver = None

    @classmethod
    def get_app_driver(cls, package, activity):
        cls.app_driver = app.Remote("http://192.168.18.61:4723/wd/hub", {
            "platformName": "Android",
            "platformVersion": "11",
            "deviceName": "Android",
            "appPackage": package,
            "appActivity": activity,
            "unicodeKeyboard": True,
            "resetKeyboard": True
        })
        return cls.app_driver

    @classmethod
    def get_app(cls):

        return cls.app_driver

    @classmethod
    def kill_app_driver(cls):
        if cls.app_driver:
            cls.app_driver.quit()
        cls.app_driver = None

    def start_activity(self, package, activity):
        self.app_driver.start_activity(package, activity)

    @classmethod
    def isElementExist(cls, element):
        flag = True
        # driver = cls.app_driver
        try:
            cls.app_driver.find_element(By.XPATH, element)
            print(flag)
            return flag
        except:
            flag = False
            print(flag)
            return flag

