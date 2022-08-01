from appium.webdriver.common.mobileby import MobileBy
from base.app_base_page import AppBasePage
from common.board import remotecontrol
from common.loging import log
import time


# 发现tab页面元素
class Cfind_tab(AppBasePage):
    def __init__(self):
        # 一排资源位置第一个元素(top1:页面第一排。resources：资源内容 one：一排第一个 two就是第二个)
        self.top1_resources_one = (MobileBy.XPATH,
                                   '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.ImageView[1]')

        # 二排推荐app资源位的第1个元素
        self.top2_resources_1 = (MobileBy.XPATH,
                                 '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.ScrollView/android.widget.RelativeLayout'
                                 '/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.LinearLayout')

        self.top2_resources_2 = (MobileBy.XPATH,
                                 '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.ScrollView/android.widget.RelativeLayout'
                                 '/android.widget.RelativeLayout[2]/android.widget.RelativeLayout')

        self.top2_resources_3 = (MobileBy.XPATH,
                                 '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.ScrollView'
                                 '/android.widget.RelativeLayout/android.widget.RelativeLayout[3]/android.widget.RelativeLayout')

        # 三排推荐app资源位的第1个元素(1：搜索、2：装机必备、3：运动健康、4：音乐娱乐、5：热门游戏、6：实用工具)

        self.top3_resources_1 = (MobileBy.XPATH,
                                 '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.ImageView[7]')

        self.top3_resources_2 = (MobileBy.XPATH,
                                 '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.ImageView[8]')

        self.top3_resources_3 = (MobileBy.XPATH,
                                 '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.ImageView[9]')

        self.top3_resources_4 = (MobileBy.XPATH,
                                 '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.ImageView[10]')

        self.top3_resources_5 = (MobileBy.XPATH,
                                 '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.ImageView[11]')

        self.top3_resources_6 = (MobileBy.XPATH,
                                 '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.ImageView[12]')

    # 点击一排资源位置第一个元素(top1:页面第一排。resources：资源内容 one：一排第一个 two就是第二个)
    def check_top1_resources_one(self):
        self.search_element(self.top1_resources_one).click()

    # 点击二排推荐app资源位的第1个元素
    def click_top2_resources_1(self):
        self.search_element(self.top2_resources_1).click()

