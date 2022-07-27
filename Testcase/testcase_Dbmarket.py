from base.app_base_page import AppBasePage
from common.driver_tool import DriverTool
from common.loging import log
from page.dbmarket.home_page import Chomepage
from page.dbmarket.my_tab import Cmy_tab



class Test_dbmarket(AppBasePage):
    def setup(self):
        homepage = Chomepage()
        self.app_driver = DriverTool.get_app_driver("com.dangbeimarket", ".activity.WelcomeActivity")
        homepage.judge_agree_button()
    def teardown(self):
        DriverTool.kill_app_driver()


    # 检查 当贝市场app可以成功打开
    def test01(self, rz = log()):
        homepage = Chomepage()
        res_findtab = homepage.search_element(homepage.findtab)
        if res_findtab:
            rz.info('当贝市场app可以成功打开')
        else:
            rz.info('error:当贝市场打开异常，请手工检查')

    # 检查我的tab页面热播影视模块和专题榜单模块展示正常
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

    # 检查热播影视资源模块，点击后可以跳转对应页面
    # 检查专题榜单源模块，点击后可以跳转对应页面







