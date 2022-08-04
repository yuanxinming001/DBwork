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

        # 装机必备详情页面 影音 av title 换按钮
        self.top3_resources_2_avtitle = (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[14]/android.widget.TextView')


        # 页面最底部装机必备 标题 down title
        self.down_title = (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.TextView')

        # 页面最底部装机必备：精选专题 down one
        self.down_one =  (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.ImageView[7]')

        # 页面最底部装机必备：常用工具 down two
        self.down_two = (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.ImageView[8]')

        # 页面最底部装机必备：更多精品应用 down three
        self.down_three = (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.ImageView[9]')



    # 点击一排资源位置第一个元素(top1:页面第一排。resources：资源内容 one：一排第一个 two就是第二个)
    def check_top1_resources_one(self):
        self.search_element(self.top1_resources_one).click()

    # 点击二排推荐app资源位的第1个元素
    def click_top2_resources_1(self):
        self.search_element(self.top2_resources_1).click()

    # 检查第三排搜索模块点击跳转页面正确 click_top3_resources_1
    def click_top3_resources_1(self):
        self.search_element(self.top3_resources_1).click()

    # 检查第三排装机必备模块点击跳转页面正确 click_top3_resources_2
    def click_top3_resources_2(self, rz = log()):
        self.search_element(self.top3_resources_2).click()
        res_avtitle = self.search_element(self.top3_resources_2_avtitle)
        if res_avtitle:
            rz.info('点击第三排装机必备模块点击跳转页面正确')
        else:
            rz.info('error: 点击第三排装机必备模块点击跳转页面异常，请人工检查')

    # 检查第三排运动健康模块点击跳转页面正确 click_top3_resources_3
    def click_top3_resources_3(self, rz = log()):
        self.search_element(self.top3_resources_3).click()

    # 检查最后一排 音乐娱乐功能模块显示正确，点击可以跳转正确页面 click_top3_resources_4
    def click_top3_resources_4(self, rz = log()):
        self.search_element(self.top3_resources_4).click()

    # 检查最后一排 热门游戏功能模块显示正确，点击可以跳转正确页面 click_top3_resources_5
    def click_top3_resources_5(self, rz = log()):
        self.search_element(self.top3_resources_5).click()

    # 检查最后一排 实用工具功能模块显示正确，点击可以跳转正确页面 click_top3_resources_6
    def click_top3_resources_6(self, rz = log()):
        self.search_element(self.top3_resources_6).click()

    # 滑动到最底部，找到装机必备模块
    def findtab_downtitle(self, rz=log()):
        remotecontrol(send='down10')
        remotecontrol(send='down10')
        res_down_title = self.search_element(self.down_title)
        if res_down_title:
            rz.info('findtab底部装机必备模块显示正确')
        else:
            rz.info('error ：findtab底部没有找到装机必备模块')

    # 滑动到最底部，检查精选专题模块显示正确
    def findtab_downone(self, rz=log()):
        remotecontrol(send='down10')
        remotecontrol(send='down10')
        res_down_one = self.search_element(self.down_one)
        if res_down_one:
            rz.info('findtab底部装精选专题模块显示正确')
        else:
            rz.info('error ：findtab底部没有找到精选专题模块')

    # 滑动到最底部，检查常用工具专题模块显示正确
    def findtab_downtwo(self, rz=log()):
        remotecontrol(send='down10')
        remotecontrol(send='down10')
        res_down_two = self.search_element(self.down_two)
        if res_down_two:
            rz.info('findtab底部常用工具专题模块显示正确 ')
        else:
            rz.info('error ：findtab底部没有找到常用工具专题模块')

    # 滑动到最底部，检查更多精品应用显示正确
    def findtab_downthree(self, rz=log()):
        remotecontrol(send='down10')
        remotecontrol(send='down10')
        res_down_three = self.search_element(self.down_three)
        if res_down_three:
            rz.info('findtab底部更多精品应用显示正确')
        else:
            rz.info('error ：findtab底部没有找到更多精品应用')














