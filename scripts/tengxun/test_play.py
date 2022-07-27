from time import sleep

from base.app_base_page import AppBasePage
from common.driver_tool import DriverTool
from common.logging_use import init_log_config
from page.tengxunshiping.home_page import HomePage
from page.tengxunshiping.play_page import PlayPage
from page.tengxunshiping.xieyi_page import XieYiPage


class TestTenXun(AppBasePage):
    # def setup_class(self):
    #     self.app_driver = DriverTool.get_app_driver("com.ktcp.video", ".activity.MainActivity")

    # def teardown_class(self):
    #     # DriverTool.kill_app_driver()

    def test_play(self):
        while True:
            init_log_config("txsp.txt")
            self.app_driver = DriverTool.get_app_driver("com.ktcp.video", ".activity.MainActivity")
            xieyi_page = XieYiPage()
            xieyi_page.click_xieyi()
            home_page = HomePage()
            home_page.click_xhcl()
            sleep(15)
            text = DriverTool.isElementExist("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView[1]")
            sleep(15)
            if text:
                DriverTool.kill_app_driver()
            else:
                break
            continue