from appium.webdriver.common.mobileby import MobileBy
from base.app_base_page import AppBasePage
from common.loging import log
import time


# 主页面元素
class Cwelfare_association(AppBasePage):
    def __init__(self):
        # Welfare association 福利社tab
        self.Welfare_association = (MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.HorizontalScrollView/android.widget.RelativeLayout/android.widget.ImageView[9]')

        # -------------------------------------------------------------------------------

        #  Head portrait  页面左上角用户头像
        self.Head_portrait = (MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.HorizontalScrollView/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.ImageView[1]')

        # user id
        self.user_id = (MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.HorizontalScrollView/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.TextView[1]')

        # The current integral 当前积分不包含值
        self.The_current_integral = (MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.HorizontalScrollView/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.TextView[3]')

        # integral  积分值
        self.integral = (MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.HorizontalScrollView/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.TextView[4]')

        # -------------------------------------------------------------------------------

        # top resources left  顶部左资源位
        self.top_resources_left = (MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.HorizontalScrollView/android.widget.RelativeLayout/android.widget.ImageView[2]')

        self.top_resources_roght = (MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.HorizontalScrollView/android.widget.RelativeLayout/android.widget.ImageView[3]')

        # today reward title 今日奖励title
        self.today_reward_title = (MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.HorizontalScrollView/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.TextView[1]')

        # -------------------------------------------------------------------------------

        # 任务奖励推荐资源 Quest_rewards_resources_one  left - right 1、2、3、4、5
        self.Quest_rewards_resources_one = (MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.HorizontalScrollView/android.widget.RelativeLayout/android.widget.RelativeLayout[3]/android.widget.ImageView')

        self.Quest_rewards_resources_two = (MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.HorizontalScrollView/android.widget.RelativeLayout/android.widget.RelativeLayout[4]/android.widget.ImageView')

        self.Quest_rewards_resources_three = (MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.HorizontalScrollView/android.widget.RelativeLayout/android.widget.RelativeLayout[5]/android.widget.ImageView')

        # -------------------------------------------------------------------------------

        # Integral_rules 积分规则  Integral_rules_details_title

        self.Integral_rules  = (MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.HorizontalScrollView/android.widget.RelativeLayout/android.widget.ImageView[4]')

        self.Integral_rules_details_title = (MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]')

        self.Integral_rules_details_Q = (MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]')



    # 1、开始收集日志 To_obtain
    def To_obtain(self):
        self.search_element(self.logget_start_button).click()