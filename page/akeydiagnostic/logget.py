from appium.webdriver.common.mobileby import MobileBy
from base.app_base_page import AppBasePage
from common.loging import log
import time


# 日志收集页面元素
class Clogget(AppBasePage):
    def __init__(self):

        # logget_button 日志获取
        self.logget_button = (MobileBy.XPATH,
                              '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[2]/android.widget.TextView')

        # 日志收集 title
        self.logget_title = (MobileBy.XPATH,
                             '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.TextView')

        # 日志收集步骤检查 【1】【2】【3】
        self.logget_one = (MobileBy.XPATH,
                           '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.TextView[1]')

        self.logget_two = (
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.TextView[2]')

        self.logget_three = (MobileBy.XPATH,
                             '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.TextView[3]')

        # 日志收集开始button
        self.logget_start_button = (MobileBy.XPATH,
                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.TextView')

        #  log time 收集日志时间
        self.log_time = (MobileBy.XPATH,
                         '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.TextView[1]')

        # cancel button取消按钮
        self.cancel_button = (MobileBy.XPATH,
                              '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[2]/android.widget.TextView')

        # log upload日志上报
        self.log_upload = (MobileBy.XPATH,
                           '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.TextView')

    # 日志收集页面元素操作--------------------------------------------------------------------------------------------------------------------------

    # 1、开始收集日志 To_obtain
    def To_obtain(self):
        self.search_element(self.logget_start_button).click()

    # 2、拿到获取时间  get  log time
    def get_log_time(self):
        rz = log()
        time.sleep(50)
        restime = self.search_element(self.log_time)
        if restime:
            rz.info('收集中')
        else:
            rz.info('没有正常收集')

    # 3、日志上报
    def logup(self):
        time.sleep(40)
        self.search_element(self.log_upload).click()


    # 4、检查日志收集页面元素 check page element
    def check_logget_page_element(self):
        rz = log()
        gettitle = self.search_element(self.logget_title)
        rz.info('检查：日志收集 页面titl 展示正确')
        get_logone = self.search_element(self.logget_one)
        rz.info('检查：点按【日志收集】请确保收集时间不少于30，提示展示正确')
        #get_logtwo = self.search_element(self.logget_two)
        #rz.info('检查：将您遇到的问题重新操作一遍，返回本页，提示展示正确')
        #get_logthree = self.search_element(self.logget_three)
        #rz.info('检查：点按【日志上报，提示展示正确')
        if get_logone and gettitle:
            rz.info('日志收集页面元素检查完毕，全部展示正确')
        else:
            rz.info('erro:请检查哪个元素展示异常')

