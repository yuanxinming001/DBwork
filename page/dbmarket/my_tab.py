from appium.webdriver.common.mobileby import MobileBy
from base.app_base_page import AppBasePage
from common.loging import log
import time


# 主页面元素
class Cmy_tab(AppBasePage):
    def __init__(self):

        # 【热播影视】
        self.hotav = (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.ImageView')

        # 【热播影视】【资源详情页面】【1】(resources_1list 第一列资源列表，resources_2list )
        self.hotav_page_resources_1list = (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.HorizontalScrollView/android.widget.RelativeLayout/android.widget.TextView[1]')

        self.hotav_page_resources_2list = (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.HorizontalScrollView/android.widget.RelativeLayout/android.widget.TextView[2]')

        self.hotav_page_resources_3list = (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.HorizontalScrollView/android.widget.RelativeLayout/android.widget.TextView[3]')

        self.hotav_page_resources_4list = (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.HorizontalScrollView/android.widget.RelativeLayout/android.widget.TextView[4]')


        # 专题榜单
        self.projectlist = (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.ImageView')

        # 已安装app元素【固定app 为投屏】 （元素位置不固定，定位的是已有app的第一排最后一个。因为app个数会变化，所以需要跳转之后，页进行面的判断。检查是否跳转成功）
        self.havaapp = (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.RelativeLayout[8]/android.widget.TextView')

        # 已安装app跳转页面【需要固定app 为投屏】
        self.havaapp_openpage = (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.Button[1]')

