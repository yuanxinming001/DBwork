from selenium.webdriver.support.wait import WebDriverWait
from common.driver_tool import DriverTool


class AppBasePage(object):
    def search_element(self, locator, timeout=50, poll_frequency=0.1):
        # 显示查找元素
        # timeout、poll时间
        return WebDriverWait(DriverTool.get_app(), timeout, poll_frequency).until(
            lambda x: x.find_element(*locator))

    def search_elements(self, locator, timeout=30, poll_frequency=0.1):
        return WebDriverWait(DriverTool.get_app(), timeout, poll_frequency).until(
            lambda x: x.find_elements(*locator))

    # def input(self, element, txt):
    #
    #     element.clear()
    #     element.send_keys(txt)
