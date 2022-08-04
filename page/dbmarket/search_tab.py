from appium.webdriver.common.mobileby import MobileBy
from common.board import remotecontrol
from base.app_base_page import AppBasePage
from common.loging import log
import time


# 搜索tab页面元素
class Csearch_tab(AppBasePage):
    def __init__(self):
        # 热门应用 hot application title
        self.hot_application_title = (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.TextView[1]')


