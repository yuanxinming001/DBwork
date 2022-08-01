from appium.webdriver.common.mobileby import MobileBy
from base.app_base_page import AppBasePage
from common.loging import log
import time

# 影视tab av_tab
class Cav_tab(AppBasePage):
    def __init__(self):
        # --------------------------------------------------------------------------------
        # (页面左侧一列数据元素)
        # --------------------------------------------------------------------------------
        # 视频点播 Video on demand
        self.Video_on_demand =(MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                                '/android.widget.FrameLayout/android.widget.RelativeLayout/android'
                                                '.support.v4.view.ViewPager/android.widget.HorizontalScrollView/android.widget.RelativeLayout/android.widget.ImageView[1]')

        # 体育电竞 Sports e-sports
        self.Sports_esports = (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                               '/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.HorizontalScrollView/android.widget.RelativeLayout/android.widget.ImageView[7]')

        # 音乐娱乐 Music_entertainment
        self.Music_entertainment = (MobileBy.XPATH,
                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.HorizontalScrollView/android.widget.RelativeLayout/android.widget.ImageView[7]')

        # -------------------------------------------------------------------------------
        # 页面中间两列元素
        # --------------------------------------------------------------------------------
        # 中间两列，左面第一个元素 In the middle left one
        self.inthe_middle_left_1 = (MobileBy.XPATH,
                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.HorizontalScrollView/android.widget.RelativeLayout/android.widget.ImageView[3]')

        # 中间两列，左面第二个元素 In the middle left two
        self.inthe_middle_left_2 = (MobileBy.XPATH,
                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.HorizontalScrollView/android.widget.RelativeLayout/android.widget.ImageView[8]')

        # 中间两列，右面第2个元素 In the middle right one
        self.inthe_middle_right_1 = (MobileBy.XPATH,
                                     '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.HorizontalScrollView/android.widget.RelativeLayout/android.widget.ImageView[4]')

        # 中间两列，右面第2个元素 In the middle right two
        self.inthe_middle_right_2 = (MobileBy.XPATH,
                                     '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.HorizontalScrollView/android.widget.RelativeLayout/android.widget.ImageView[9]')

        # --------------------------------------------------------------------------------
        # (页面右侧一列数据元素)
        # --------------------------------------------------------------------------------
        # 热门影音模块 hotmv
        self.hotmv = (MobileBy.XPATH,
                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.HorizontalScrollView/android.widget.RelativeLayout/android.widget.ImageView[10]')

        # 热播影视 hot play av
        self.hot_play_av = (MobileBy.XPATH,
                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.HorizontalScrollView/android.widget.RelativeLayout/android.widget.ImageView[12]')

        # --------------------------------------------------------------------------------
        # 热门影视模块 hotmv resources 3  推荐资源元素 3
        self.hotmv_resources_3 = (MobileBy.XPATH,
                                  '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.HorizontalScrollView/android.widget.RelativeLayout/android.widget.ImageView[11]')


    # 1、开始收集日志 To_obtain
    def To_obtain(self):
        self.search_element(self.logget_start_button).click()