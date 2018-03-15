#！ /usr/bin/env python 3.5.2
#coding = utf-8
#author = yexiaozhu

import os, time, unittest
from appium import webdriver
from selenium.webdriver.common.by import By

PATH = lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__), p))

class SimpleAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'  # 设备系统
        desired_caps['platformVersion'] = '5.1.1'  # 设备系统版本
        desired_caps['deviceName'] = 'cc1ad23e'  #  设备名称
        # desired_caps['deviceName'] = 'MDG4C15B21005668'  #  设备名称

        desired_caps['app'] = PATH(r"D:\工作\teacher_v2.1.2.293-release.apk")
        # desired_caps['app'] = "com.lebaoedu.teacher.test" # 测试包名
        # desired_caps['app'] = "com.lebaoedu.teacher" # 正式包名
        # desired_caps['unicodeKeyboard'] = True
        # desired_caps['resetKeyboard'] = True
        # desired_caps['app'] = PATH(r"D:\工作\ApiDemos-debug.apk")
        # desired_caps['appPackage'] = 'com.lebaoedu.teacher'
        # desired_caps['appActivity'] = 'com.lebaoedu.teacher.activity.HomeActivity'

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        time.sleep(5)
        el = self.driver.find_element_by_id('com.lebaoedu.teacher:id/tv_pass')
        # el = self.driver.find_element_by_id('tv_pass')
        # print('type:',type(el))
        el.click()
        # time.sleep(5)
        # 输入手机号码
        self.driver.find_element_by_id('com.lebaoedu.teacher:id/et_content').send_keys('18202532873')
        date = time.strftime("%Y%m%d")
        code = date + str(2873)
        print(int(code))
        # 输入短信验证码
        self.driver.find_element_by_id('com.lebaoedu.teacher:id/et_telcode').send_keys(int(code))
        # 点击登录
        login = self.driver.find_element_by_id('com.lebaoedu.teacher:id/tv_login')
        login.click()
        time.sleep(5)
        # try:
        #     iv_close = self.driver.find_element(By.ID,"com.lebaoedu.teacher:id/iv_close")
        #     print('iv_close=',iv_close)
        #     iv_close.click()
        #     self.driver.implicitly_wait(1)
        # except:
        #     pass

    def tearDown(self):
        self.driver.quit()

    def test_help(self):
        # 帮助
        img_help = self.driver.find_element_by_id('com.lebaoedu.teacher:id/img_help')
        print('img_help=', img_help)
        img_help.click()
        # text = self.driver.find_elements(By.ID, "com.lebaoedu.teacher:id/tv_title")[0].text
        text = self.driver.find_element_by_id("com.lebaoedu.teacher:id/tv_title").text
        self.assertTrue(u"帮助" == text)
        # cons = self.driver.contexts
        # print(cons)
        # webview = cons[-1]
        # self.driver._switch_to.context(webview)
        # Qa = self.driver.we
        # print('Qa=', Qa)
        # Qa.click()
        img_back = self.driver.find_element_by_id('com.lebaoedu.teacher:id/img_back')
        print('img_back=', img_back)
        img_back.click()

    # def test_add_class(self):
    #     # 添加班级
    #     img_add_class = self.driver.find_element_by_id('com.lebaoedu.teacher:id/img_add_class')
    #     img_add_class.click()
    #     add_class_text = self.driver.find_element_by_id('com.lebaoedu.teacher:id/tv_title').text
    #     self.assertTrue(u"添加班级" == add_class_text)
    #     tv_create_class = self.driver.find_element_by_id('com.lebaoedu.teacher:id/tv_create_class')
    #     tv_create_class.click()
    #     create_class_text = self.driver.find_element_by_id('com.lebaoedu.teacher:id/tv_title').text
    #     self.assertTrue(u"创建班级" == create_class_text)
    #     # 输入学校名称
    #     ed_list = self.driver.find_elements_by_class_name('android.widget.EditText')
    #     ed_kindergrader = ed_list[0]
    #     ed_kindergrader.send_keys('18202532873')
    #     self.driver.deactivate_ime_engine()
    #     # 输入班级名称
    #     ed_class_name = ed_list[1]
    #     ed_class_name.send_keys('18202532873')
    #     self.driver.deactivate_ime_engine()
    #     # 点击完成创建
    #     create = self.driver.find_element_by_name(u'完成创建')
    #     create.click()
    #
    #
    # # def test_tv_to_bind_box(self):
    # #     # 绑定盒子
    # #     tv_to_bind_box = self.driver.find_element_by_id('com.lebaoedu.teacher:id/tv_to_bind_box')
    # #
    def test_tv_chang_class(self):
        # 切换班级
        tv_change_class = self.driver.find_element_by_id('com.lebaoedu.teacher:id/tv_change_class')
        tv_change_class.click()
        # 获取教师班级列表
        # class_lists = self.driver.find_elements_by_id('com.lebaoedu.teacher:id/tv_class_name')
        class_lists = self.driver.find_elements_by_class_name('android.widget.RelativeLayout')
        # 获取班级总数
        class_lists_number = len(class_lists) - 1
        print("class_lists_number", class_lists_number)
        class_lists[4].click()
        time.sleep(5)

    def test_class_dyn(self):
        # 班级动态
        try:
            class_dyn = self.driver.find_element_by_id('com.lebaoedu.teacher:id/layout_class_dyn')
            class_dyn.click()
            title = self.driver.find_element_by_id('com.lebaoedu.teacher:id/tv_title')
            self.assertTrue(title == u'班级动态')
            dyn_lists = self.driver.find_elements_by_id('com.lebaoedu.teacher:id/layout_container')
            print('dyn_lists=',dyn_lists)
            call_back = self.driver.find_element_by_id('com.lebaoedu.teacher:id/img_back')
            call_back.click()
        except:
            print('暂无班级动态')
            time.sleep(5)

    # # def test_banner(self):
    # #     # 切换banner
    # #     return
    # #
    # #
    # # def test_lay_class_manage(self):
    # #     # 班级管理
    # #     lay_class_manage = self.driver.find_element_by_id('com.lebaoedu.teacher:id/layout_class_manage')



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleAndroidTests)
    # unittest.TextTestRunner(verbosity=2).run(suite)