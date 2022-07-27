from appium.webdriver.common.mobileby import MobileBy
from base.app_base_page import AppBasePage
from common.loging import log


# 网络诊断详情页面元素
class CNetwork_details(AppBasePage):

    def __init__(self):
        # back 返回按钮

        self.back_button = (MobileBy.XPATH,
                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[5]/android.widget.TextView')
        # 网络正常服务

        self.Normal_Network_Service = (MobileBy.XPATH,
                                       '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.TextView[1]')

        # 检查项title 【1】【2】【3】【4】
        self.Network_Service_one = (MobileBy.XPATH,
                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.TextView[1]')

        self.Network_Service_two = (MobileBy.XPATH,
                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.TextView[1]')

        self.Network_Service_three = (MobileBy.XPATH,
                                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[3]/android.widget.TextView[1]')

        self.Network_Service_fore = (MobileBy.XPATH,
                                     '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[4]/android.widget.TextView[1]')

    # 网络诊断详情页面元素操作--------------------------------------------------------------------------------------------------------------------------

    # 查找返回按钮
    def findback(self):
        rz = log()
        getback = self.search_element(self.back_button)
        if getback:
            rz.info('可以正常诊断设备网络')
        else:
            rz.info('errpr:网络诊断异常，请检查！')

    # 检查网络诊断项 1、2、3、4
    def check_networkdetails_title(self):
        rz = log()
        checkone_title = self.search_element(self.Network_Service_one)
        rz.info('网络基础配置检查完毕')
        checktow_title = self.search_element(self.Network_Service_two)
        rz.info('IP地址配置检查完毕')
        checkthree_title = self.search_element(self.Network_Service_three)
        rz.info('设备能否上网检查完毕')
        checkfore_title = self.search_element(self.Network_Service_fore)
        rz.info('网页连接测试检查完毕')
        if checkone_title and checktow_title and checkthree_title and checkfore_title:
            rz.info('网络服务4项检查均正确')
        else:
            rz.info('error:网络服务4项检查展示有问题')


