from appium.webdriver.common.mobileby import MobileBy
from base.app_base_page import AppBasePage
from common.board import remotecontrol
from common.loging import log
import time


# 主页面元素
class Chomepage(AppBasePage):

    def __init__(self):



        # 跳过 jump button
        self.jump_button = (MobileBy.XPATH,
                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.HorizontalScrollView/android.widget.RelativeLayout/android.widget.ImageView[9]')

        # 同意按钮 agree button
        self.agree_button = (MobileBy.XPATH,
                             '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.TextView[1]')

        # 不同意按钮 ont agree button
        self.not_agree_button = (MobileBy.XPATH,
                                 '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.TextView[2]')

        # 下一步next step
        self.next_step = (MobileBy.XPATH,
                          '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.TextView[3]')
        # 我的tab元素
        self.mytab = (MobileBy.XPATH,
                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.HorizontalScrollView/android.widget.RelativeLayout/android.widget.ImageView[1]')

        # 发现tab元素
        self.findtab = (MobileBy.XPATH,
                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.HorizontalScrollView/android.widget.RelativeLayout/android.widget.ImageView[2]')

        # 精品tab元素
        self.Thehighqualitygoods = (MobileBy.XPATH,
                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.HorizontalScrollView/android.widget.RelativeLayout/android.widget.ImageView[3]')

        # 影音tab元素
        self.avtab = (MobileBy.XPATH,
                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.HorizontalScrollView/android.widget.RelativeLayout/android.widget.ImageView[4]')

        # 教育tab元素
        self.educationtab = (MobileBy.XPATH,
                             '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.HorizontalScrollView/android.widget.RelativeLayout/android.widget.ImageView[6]')

        # 游戏tab元素
        self.gametab = (MobileBy.XPATH,
                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.HorizontalScrollView/android.widget.RelativeLayout/android.widget.ImageView[7]')

        # 应用tab 元素
        self.applicationtab = (MobileBy.XPATH,
                               '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.HorizontalScrollView/android.widget.RelativeLayout/android.widget.ImageView[8]')

        # 管理tab元素
        self.managementtab = (MobileBy.XPATH,
                              '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.HorizontalScrollView/android.widget.RelativeLayout/android.widget.ImageView[9]')

        # 福利社tab
        self.welfaretab = (MobileBy.XPATH,
                           '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.HorizontalScrollView/android.widget.RelativeLayout/android.widget.ImageView[10]')

    # 判断冷启动：跳过弹窗、下载弹窗、同意协议弹窗方法
    def judge_agree_button(self):
        print('123')
        get_agree_button = self.search_element(self.agree_button)
        if get_agree_button:
            self.search_element(self.agree_button).click()
            time.sleep(6)
            remotecontrol(send='back')
            remotecontrol(send='back')
        else:
            pass

        get_jump_button = self.search_element(self.jump_button)
        if get_jump_button:
            self.search_element(self.jump_button).click()
        else:
            pass

    # 跳转我的页面 goto my tab
    def goto_my_tab(self):
        self.search_element(self.mytab).click()

    # 跳转发现页面 goto find tab
    def goto_find_tab(self):
        self.search_element(self.findtab).click()
        remotecontrol(send='back')
