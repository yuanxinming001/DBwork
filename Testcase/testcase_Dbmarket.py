import os
import sys
import allure
object_path = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
sys.path.append(object_path)
from common.driver_tool import DriverTool
from base.app_base_page import AppBasePage
from common.loging import log
from page.dbmarket.find_tab import Cfind_tab
from page.dbmarket.movement_details import Cmovement_details
from page.dbmarket.search_tab import Csearch_tab
from page.dbmarket.home_page import Chomepage
from page.dbmarket.my_tab import Cmy_tab
from common.board import remotecontrol
from page.dbmarket.app_details import Capp_details


@allure.epic('当贝市场项目')
class Test_dbmarket(AppBasePage):

    def setup(self):
        homepage = Chomepage()
        self.app_driver = DriverTool.get_app_driver("com.dangbeimarket", ".activity.WelcomeActivity")
        homepage.judge_agree_button()

    def teardown(self):
        DriverTool.kill_app_driver()

    @allure.title('检查 当贝市场app可以成功打开')
    def test01(self, rz=log()):
        homepage = Chomepage()
        res_findtab = homepage.search_element(homepage.findtab)
        if res_findtab:
            rz.info('当贝市场app可以成功打开')
        else:
            rz.info('error:当贝市场打开异常，请手工检查')

    @allure.title('检查我的tab页面热播影视模块和专题榜单模块展示正常')
    def test02(self, rz=log()):
        homepage = Chomepage()
        homepage.goto_my_tab()
        mytab = Cmy_tab()
        res_hotav = mytab.search_element(mytab.hotav)
        res_projectlist = mytab.search_element(mytab.projectlist)
        if res_hotav and res_projectlist:
            rz.info('我的tab页面热播影视模块和专题榜单模块展示正常')
        else:
            rz.info('error:我的tab页面热播影视模块和专题榜单模块展示异常，请手工检查')

    @allure.title('检查热播影视资源模块，点击后可以跳转对应页面')
    def test03(self, rz=log()):
        homepage = Chomepage()
        homepage.goto_my_tab()
        my_tab = Cmy_tab()
        my_tab.click_hotavlist()
        res_list1 = my_tab.search_element(my_tab.hotav_page_resources_1list)
        res_list2 = my_tab.search_element(my_tab.hotav_page_resources_2list)
        if res_list1 and res_list2:
            rz.info('热播影视资源模块，点击后可以跳转对应页面')
        else:
            rz.info('error:请人工检查热播影视资源模块，点击后跳转页面异常')

    @allure.title('检查专题榜单源模块，点击后可以跳转对应页面')
    def test04(self, rz=log()):
        homepage = Chomepage()
        homepage.goto_my_tab()
        my_tab = Cmy_tab()
        my_tab.click_projectlist()
        res_top_title = my_tab.search_element(my_tab.top_title)
        if res_top_title:
            rz.info('点击专题榜单源模块，可以跳转对应页面')
        else:
            rz.info('error:点击专题榜单资源模块，跳转页面异常，请人工检查')

    @allure.title('检查播影视模块资源页面，点击更多电影tab，跳转页面正确')
    def test05(self):
        homepage = Chomepage()
        homepage.goto_my_tab()
        my_tab = Cmy_tab()
        my_tab.click_hotavlist()
        remotecontrol(send='right')
        my_tab.click_more_mv()
        app_details = Capp_details()
        app_details.check_history()

    @allure.title('检查榜单资源内容，点击后跳转页面正确')
    def test06(self):
        homepage = Chomepage()
        homepage.goto_my_tab()
        my_tab = Cmy_tab()
        my_tab.click_hotavlist()
        remotecontrol(send='right')
        my_tab.check_hotmvlist_jump_ok()

    @allure.title('检查热播影视模块资源页面：本周电影热播、本周电视剧热播模块展示正确')
    def test07(self):
        homepage = Chomepage()
        my_tab = Cmy_tab()
        homepage.goto_my_tab()
        my_tab.click_hotavlist()
        my_tab.check_hotmvlist_title()

    @allure.title('检查发现页面推荐app的资源内容，点击可以跳转下载app页面')
    def test08(self):
        homepage = Chomepage()
        homepage.goto_find_tab()
        app_details = Capp_details()
        find_tab = Cfind_tab()
        find_tab.check_top1_resources_one()
        app_details.check_history()

    @allure.title('检查发现页面二排推荐app显示正确，点击可以跳转正确页面')
    def test09(self):
        homepage = Chomepage()
        homepage.goto_find_tab()
        app_details = Capp_details()
        find_tab = Cfind_tab()
        find_tab.click_top2_resources_1()
        app_details.check_history()

    @allure.title('检查第三排 搜索功能模块显示正确，点击可以跳转正确页面')
    def test10(self, rz=log()):
        homepage = Chomepage()
        homepage.goto_find_tab()
        find_tab = Cfind_tab()
        find_tab.click_top3_resources_1()
        searcher_tab = Csearch_tab()
        res = searcher_tab.search_element(searcher_tab.hot_application_title)
        if res:
            rz.info('搜索页面热门应用列表title存在，跳转页面正确')
        else:
            rz.info('error: 没有找到热门应用列表title，跳转页面异常请人工检查')

    @allure.title('检查最后一排 装机必备功能模块显示正确，点击可以跳转正确页面')
    def test11(self):
        homepage = Chomepage()
        homepage.goto_find_tab()
        find_tab = Cfind_tab()
        find_tab.click_top3_resources_2()

    @allure.title('检查最后一排 运动健康功能模块显示正确，点击可以跳转正确页面')
    def test12(self):
        homepage = Chomepage()
        homepage.goto_find_tab()
        find_tab = Cfind_tab()
        find_tab.click_top3_resources_3()
        movement_details = Cmovement_details()
        movement_details.get_The_default()

    @allure.title('检查最后一排 音乐娱乐功能模块显示正确，点击可以跳转正确页面')
    def test13(self, rz=log()):
        homepage = Chomepage()
        homepage.goto_find_tab()
        find_tab = Cfind_tab()
        find_tab.click_top3_resources_4()
        movement_details = Cmovement_details()
        movement_details.get_The_default()

    @allure.title('检查最后一排 热门游戏功能模块显示正确，点击可以跳转正确页面')
    def test14(self):
        homepage = Chomepage()
        homepage.goto_find_tab()
        find_tab = Cfind_tab()
        find_tab.click_top3_resources_5()
        movement_details = Cmovement_details()
        movement_details.get_The_default()

    @allure.title('检查最后一排 实用工具功能模块显示正确，点击可以跳转正确页面')
    def test15(self):
        homepage = Chomepage()
        homepage.goto_find_tab()
        find_tab = Cfind_tab()
        find_tab.click_top3_resources_6()
        movement_details = Cmovement_details()
        movement_details.get_The_default()

    @allure.title('检查发现tab底部装机必备模块功能显示正确')
    def test16(self):
        homepage = Chomepage()
        homepage.goto_find_tab()
        find_tab = Cfind_tab()
        find_tab.findtab_downtitle()

    @allure.title('检查发现tab页面最底部精选专题模块显示正确')
    def test17(self):
        homepage = Chomepage()
        homepage.goto_find_tab()
        find_tab = Cfind_tab()
        find_tab.findtab_downone()

    @allure.title('检查发现tab页面最底部常用工具专题模块显示正确')
    def test18(self):
        homepage = Chomepage()
        homepage.goto_find_tab()
        find_tab = Cfind_tab()
        find_tab.findtab_downtwo()

    @allure.title('检查发现tab页面最底部更多精品应用显示正确')
    def test19(self):
        homepage = Chomepage()
        homepage.goto_find_tab()
        find_tab = Cfind_tab()
        find_tab.findtab_downthree()










