from appium.webdriver.common.mobileby import MobileBy
from base.app_base_page import AppBasePage
from common.loging import log
from common.board import remotecontrol
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
        # 【热播影视】【资源详情页面】【1】【资源】one resources
        self.hotav_page_resources_1list_oneresources = (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.HorizontalScrollView/android.widget.RelativeLayout/android.widget.RelativeLayout[16]/android.widget.TextView')

        # 【热播影视】【资源详情页面】【2】【资源】two resources
        self.hotav_page_resources_2list_tworesources = (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.HorizontalScrollView/android.widget.RelativeLayout/android.widget.RelativeLayout[17]/android.widget.TextView')

        # resources play 播放器选择
        self.play_resources = (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.TextView')

        # 【热播影视】【资源详情页面】【1】（ 更多电影按钮)more mv
        self.more_mv = (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.HorizontalScrollView/android.widget.RelativeLayout/android.widget.RelativeLayout[25]/android.widget.TextView')

        # 专题榜单
        self.projectlist = (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.ImageView')

        # 专题榜单详情页面顶部标题 top title
        self.top_title = (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.TextView')


        # 已安装app元素【固定app 为投屏】 （元素位置不固定，定位的是已有app的第一排最后一个。因为app个数会变化，所以需要跳转之后，页进行面的判断。检查是否跳转成功）
        self.havaapp = (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.RelativeLayout[8]/android.widget.TextView')

        # 已安装app跳转页面【需要固定app 为投屏】
        self.havaapp_openpage = (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.Button[1]')


    # 点击热播影视
    def click_hotavlist(self):
        self.search_element(self.hotav).click()

    # 点击专题榜单
    def click_projectlist(self):
        self.search_element(self.projectlist).click()

    # 点击 【热播影视】【资源详情页面】【1】（ 更多电影按钮)more mv
    def click_more_mv(self):
        self.search_element(self.more_mv).click()

    # 检查电影热播列表资源点击跳转正确
    def check_hotmvlist_jump_ok(self):
        rz = log()
        self.search_element(self.hotav_page_resources_1list_oneresources).click()
        res_play_resources1 = self.search_element(self.play_resources)
        remotecontrol(send='back')
        self.search_element(self.hotav_page_resources_2list_tworesources).click()
        res_play_resources2 = self.search_element(self.play_resources)
        remotecontrol(send='back')
        if res_play_resources1 and res_play_resources2:
            rz.info('点击资源播放跳转正确')
        else:
            rz.info('error: 点击资源播放跳转错误，请人工检查')

    # 检查：热播影视模块资源页面：本周电影热播、本周电视剧热播、本周综艺热播、本周动漫热播模块展示正确
    def check_hotmvlist_title(self):
        rz = log()
        res_hotav_list1 = self.search_element(self.hotav_page_resources_1list)
        res_hote_list2 = self.search_element(self.hotav_page_resources_2list)
        remotecontrol(send='right4')
        res_hotav_list3 = self.search_element(self.hotav_page_resources_3list)
        res_hotav_list4 = self.search_element(self.hotav_page_resources_4list)
        if res_hote_list2 and res_hotav_list1 and res_hotav_list3 and res_hotav_list4:
            rz.info('热播影视模块资源页面：本周电影热播、本周电视剧热播模块展示正确')
        else:
            rz.info('error:热播影视模块资源页面：本周电影热播、本周电视剧热播、模块展示异常，请人工检查')




