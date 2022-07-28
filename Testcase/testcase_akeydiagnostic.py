import os
import sys
object_path = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
sys.path.append(object_path)
from common.driver_tool import DriverTool
from common.loging import log
from base.app_base_page import AppBasePage
from page.akeydiagnostic.Network import CNetwork
from page.akeydiagnostic.logget import Clogget
from page.akeydiagnostic.Network_details import CNetwork_details


class Test_akeydiagnostic(AppBasePage):

    def setup(self):
        self.app_driver = DriverTool.get_app_driver("com.dangbei.lerad.leradwatcher", ".ui.main.MainActivity")

    def teardown(self):
        DriverTool.kill_app_driver()

    # 检查可以打开一键诊断app
    def test01(self):
        network = CNetwork()
        network.getNetwork_button()

    # 检查网络诊断功能正常
    def test02(self):
        network = CNetwork()
        network.goto_Network_detauls()
        details = CNetwork_details()
        details.findback()

    # # 检查点击日志收集button 跳转页面正确
    def test03(self):
        network = CNetwork()
        clogget = Clogget()
        network.go_to_logreport()
        clogget.check_logget_page_element()

    # 检查网络诊断页面显示正确
    def test04(self):
        network = CNetwork()
        cNetwork_details = CNetwork_details()
        network.goto_Network_detauls()
        cNetwork_details.check_networkdetails_title()

    # 检查日志上报页面显示正确
    def test05(self):
        network = CNetwork()
        clogget = Clogget()
        network.go_to_logreport()
        clogget.check_logget_page_element()

    # 检查日志可以上报成功
    def test06(self):
        rz = log()
        network = CNetwork()
        clogget = Clogget()
        network.go_to_logreport()
        clogget.To_obtain()
        clogget.logup()
        get_Qr_code = network.search_element(network.Qr_code)
        if get_Qr_code:
            rz.info('日志可以上报成功')
        else:
            rz.info('error：日志上报失败，请手工检查')
