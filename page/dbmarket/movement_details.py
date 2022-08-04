from appium.webdriver.common.mobileby import MobileBy
from base.app_base_page import AppBasePage
from common.loging import log
from common.board import remotecontrol
import time


# 运动健康详情页面
class Cmovement_details(AppBasePage):
    def __init__(self):

        # 全部应用 all application
        self.all_application = (MobileBy.XPATH, '')

        # 健身塑形 fitness
        self.fitness = (MobileBy.XPATH,
                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.GridView[1]/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.TextView')

        # 瑜伽舞蹈 dance
        self.dance = (MobileBy.XPATH,
                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.GridView[1]/android.widget.RelativeLayout[3]/android.widget.RelativeLayout/android.widget.TextView')

        # 健康咨询 consulting
        self.consulting = (MobileBy.XPATH,
                           '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.GridView[1]/android.widget.RelativeLayout[4]/android.widget.RelativeLayout/android.widget.TextView')

        # 默认 The default
        self.The_default = (MobileBy.XPATH,
                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.RelativeLayout[1]/android.widget.TextView')

        # 更新 update
        self.update = (MobileBy.XPATH,
                       '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.RelativeLayout[2]/android.widget.TextView   ')

        # 评分 score
        self.score = (MobileBy.XPATH,
                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.RelativeLayout[3]/android.widget.TextView')

        # 热度 The heat
        self.The_heat = (MobileBy.XPATH,
                         '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.RelativeLayout[4]/android.widget.TextView')

        # 中间顶部资源 【1、2、3】 top middle 1
        self.top_middle_1 = (MobileBy.XPATH,
                             '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.GridView[2]/android.widget.RelativeLayout[1]/android.widget.ImageView')

        # 中间下面资源 【1、2、3.......】 dwom middle 1
        self.dwom_middle_1 = (MobileBy.XPATH,
                              '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.GridView[2]/android.widget.RelativeLayout[4]/android.widget.ImageView[2]')

    # 获取默认tab元素 get The_default
    def get_The_default(self, rz=log()):
        res_The_default = self.search_element(self.The_default)
        if res_The_default:
            rz.info('点击功能模块后，跳转页面正确')
        else:
            rz.info('error: 点击点击功能模块后块，跳转页面显示异常，请人工检查')
