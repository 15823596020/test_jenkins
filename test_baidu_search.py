"""
selenium自动化代码的介绍
用例业务内容：测试百度网首页搜索关键词之后，跳转页面标题的正确性
python 代码实现
Web UI 测试框架 Selenium（WebDriver）
自动化测试框架 pytest
运行框架 pytest
开发工具 PyCharm
"""
import os
import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from loguru import logger  # logger是为了让打印出来的日志更好看一下


class TestBaidu:

    def setup_class(self):
        try:
            headless = os.getenv("headless")  # 获取环境变量headless，可随意取名，如果获取到了就复制给headless
        except Exception:
            headless = None  # 如果没有获取到，就设置headless为None
        chrome_options = Options()
        if headless == "true":  # 如果headless取值为true
            logger.info("设置了headless变量并且设置为true，将会无界面运行测试")  # 打印，用print也可以，但是logger.info打印出来的日志更好看
            chrome_options.add_argument("--headless")  # 添加一个参数headless，采用无界面的运行方式
        else:
            logger.info("系统未设置headless为true，将会有界面运行测试")  # 打印
        self.driver = webdriver.Chrome(options=chrome_options)  # 那么就采用有界面的运行方式
        self.driver.set_window_size("1360", "768")  # 设置尺寸，防止无界面运行时，找不到元素
        self.driver.implicitly_wait(10)  # 隐式等待
        logger.info("请求百度www.baidu.com")  # 打印
        self.driver.get('http://www.baidu.com')  # 访问网址

    def teardown_class(self):
        self.driver.quit()  # 退出

    @pytest.mark.parametrize("keys", ("霍格沃兹", "测试开发"))
    def test_baidu(self, keys):
        el = self.driver.find_element(By.ID, "kw")  # 定位输入框
        logger.info("清除输入框的内容")  # 打印
        el.clear()  # 清空输入框（因为这里测试使用了一次初始化，第一次搜索的结果可能还存在，所以需要清空输入框）
        logger.info(f"填写关键字{keys}到输入框")  # 打印
        el.send_keys(keys)  # 输入搜索词
        logger.info(f"提交，进行符合{keys}的结果查找")  # 打印
        self.driver.find_element(By.ID, "su").click()  # 定位百度一下按钮
        sleep(5)
        assert keys in self.driver.title  # 断言搜索词在获取的标题中

if __name__ == '__main__':
    pytest.main(["-s", "-v"])