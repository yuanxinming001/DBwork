from appium.webdriver.common.mobileby import MobileBy
from base.app_base_page import AppBasePage
from common.loging import log
import time


# 游戏tab下面的所有元素记录
class Cgame_tab(AppBasePage):
    def __init__(self):
        # The remote control 遥控器游戏
        self.The_remote_control_game = (MobileBy.XPATH,
                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.HorizontalScrollView/android.widget.RelativeLayout/android.widget.ImageView[1]')

        # The handle 手柄游戏
        self.The_handle_game = (MobileBy.XPATH,
                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.HorizontalScrollView/android.widget.RelativeLayout/android.widget.ImageView[2]')

        # Empty rat 空鼠游戏
        self.Empty_rat_game = (MobileBy.XPATH,
                               '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.HorizontalScrollView/android.widget.RelativeLayout/android.widget.ImageView[7]')

        # In the middle resources_one 中间资源的第一个
        self.inthe_middle_resources_one = (MobileBy.XPATH,
                                           '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.HorizontalScrollView/android.widget.RelativeLayout/android.widget.ImageView[3]')

        # In the middle resources_one 中间资源的第二个
        self.inthe_middle_resources_two = (MobileBy.XPATH,
                                           '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.HorizontalScrollView/android.widget.RelativeLayout/android.widget.ImageView[4]')

        # In the down resources_one 中间资源的第一个
        self.inthe_down_resources_one = (MobileBy.XPATH,
                                         '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.HorizontalScrollView/android.widget.RelativeLayout/android.widget.ImageView[8]')

        self.inthe_down_resources_two = (MobileBy.XPATH,
                                         '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.HorizontalScrollView/android.widget.RelativeLayout/android.widget.ImageView[9]')

        # hot game 热门游戏
        self.hotgame = (MobileBy.XPATH,
                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.HorizontalScrollView/android.widget.RelativeLayout/android.widget.ImageView[10]')

        # hot game down 热门游戏下面的童年经典游戏
        self.hot_game_down = (MobileBy.XPATH,
                              '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.HorizontalScrollView/android.widget.RelativeLayout/android.widget.ImageView[12]')


    # 1、开始收集日志 To_obtain
    def To_obtain(self):
        self.search_element(self.logget_start_button).click()