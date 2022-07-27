from appium.webdriver.common.mobileby import MobileBy
from base.app_base_page import AppBasePage
from common.loging import log
import time


# 网络诊断页面元素
class CNetwork(AppBasePage):
    def __init__(self):
        # 网络诊断button
        self.Network_inthe_diagnosis_of_button = (MobileBy.XPATH,
                                                  '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.TextView')

        #  Qr_code 二维码图片
        self.Qr_code = (MobileBy.XPATH,
                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.ImageView')

        # 网络诊断页面的title展示
        self.Network_inthe_diagnosis_of_title = (MobileBy.XPATH,
                                                 '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.TextView[1]')

        # logget_button 日志收集
        self.logget_button = (MobileBy.XPATH,
                              '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[2]/android.widget.TextView')

    # 网络诊断页面元素操作--------------------------------------------------------------------------------------------------------------------------

    # 获取网络诊断button 二维码图片
    def getNetwork_button(self):
        rz = log()
        get_Network_inthe_diagnosis_of_button = self.search_element(self.Network_inthe_diagnosis_of_button)
        get_Qr_code = self.search_element(self.Qr_code)
        if get_Qr_code and get_Network_inthe_diagnosis_of_button:
            rz.info('进入一键诊断页面正确')
        else:
            rz.info('error:进入一键诊断页面错误')


    # 点击网络诊断button Network_inthe_diagnosis_of_button
    def goto_Network_detauls(self):
        self.search_element(self.Network_inthe_diagnosis_of_button).click()

    # 去日志收集页面
    def go_to_logreport(self):
        self.search_element(self.logget_button).click()

