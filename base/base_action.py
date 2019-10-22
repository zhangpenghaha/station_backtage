import allure
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, feature, timeout=10, poll=1.0):
        try:
            by = feature[0]
            value = feature[1]
            return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(by, value))
        except :
            return None

    def find_elements(self, feature, timeout=10, poll=1.0):
        try:
            by = feature[0]
            value = feature[1]
            return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(by, value))
        except :
            return None


    # 点击
    def click(self, feature):
        self.find_element(feature).click()

    # 输入
    def input(self, feature, text):
        allure.attach("输入" + text, text, allure.attach_type.TEXT)
        self.find_element(feature).clear()
        self.find_element(feature).send_keys(text)

    # 获取元素文本
    def get_text(self, feature):
        return self.find_element(feature).text

    # 获取多元素文本
    def get_texts(self, feature):
        text_list = []
        a = self.find_elements(feature)
        print(a)
        for i in a:
            l = i.text
            text_list.append(l)
        return text_list


    # 获取elert弹框文本
    def get_alert_text(self):
        return self.driver.switch_to.alert().text


    # 通过P标签文本找元素
    def find_by_text_p(self, text):
        ele =  By.XPATH, '//p[text()="{}"]'.format(text)
        return self.find_element(ele).text

    # 通过span标签找文本
    def find_by_text_span(self, text):
        ele =  By.XPATH, '//span[text()="{}"]'.format(text)
        return self.find_element(ele).text

    # 通过div标签找文本
    def find_by_text_div( self, text ):
        ele = By.XPATH, '//div[text()="{}"]'.format(text)
        return self.find_element(ele).text

    # 点击span文本
    def click_span_text(self, text):
        allure.attach("点击" + text, text, allure.attach_type.TEXT)
        ele = By.XPATH, '//span[text()="{}"]'.format(text)
        return self.click(ele).text

    # 点击div文本
    def click_div_text( self, text ):
        allure.attach("点击"+ text, text, allure.attach_type.TEXT)
        ele = By.XPATH, '//div[text()="{}"]'.format(text)
        return self.click(ele)

    # 点击link_text文本
    def click_link_text( self, text ):
        allure.attach("点击" + text, text, allure.attach_type.TEXT)
        ele = By.LINK_TEXT, '{}'.format(text)
        return self.click(ele)

    # 向下滑动
    def scroll_dwon(self, num, lenth):
        """
        :param num: 滑动之后再滑动多少次,每次+1000
        :param lenth: 第一次滑动的位置
        :return:
        """
        for i in range(num):
            js = 'window.scrollTo(0, {})'.format(lenth)
            self.driver.execute_script(js)
            lenth += 1000
            time.sleep(5)