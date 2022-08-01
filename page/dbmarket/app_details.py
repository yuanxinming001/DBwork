from appium.webdriver.common.mobileby import MobileBy
from base.app_base_page import AppBasePage
from common.loging import log
import time

# app install details page app 下载详情页面
class Capp_details(AppBasePage):
    
    def __init__(self):

        #  install button 下载按钮
        self.install_button =(MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.view.View[7]')

        # advertising resources location 广告资源位
        self.advertising_resources =(MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.view.View[8]')

        # version 版本号
        self.version = (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.TextView[1]')

        # install number 下载量
        self.install_number =(MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.TextView[2]')

        # size number 大小
        self.size_number =(MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.TextView[3]')

        # update time 更新时间
        self.update_time =(MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.TextView[4]')

        # development people 开发者
        self.development_people =(MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.TextView[5]')



        # app name
        self.app_name =(MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.TextView')

        # history version 历史版本
        self.history_version =(MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.view.View[9]')

        # hot content 热门内容
        self.hot_content =(MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.TextView')

        # application information 应用信息
        self.application_information =(MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[4]/android.widget.TextView')

        # related recommended 相关推荐
        self.related_recommended =(MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[3]/android.widget.TextView')

        # application score 应用评分
        self.application_score =(MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[5]/android.widget.TextView')

    # 历史版本检查
    def check_history(self):
        rz = log()
        res = self.search_element(self.history_version)
        if res:
            rz.info('成功跳转到下载应用详情页面')
        else:
            print('error:没有发现历史版本，跳转到下载应用详情页面异常请人工检查')
        


