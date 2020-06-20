"""
接口功能测试应用：http://www.weather.com.cn/data/cityinfo/
接口功能：获得对应城市的天气预报
源码：Python
功能包：HttpClient
请求方法：Get
自动化测试框架：pytest
运行架构：pytest
开发工具：PyCharm
源码位置：
"""
import pytest

from test_jenkins.weather.library.httpclient import HttpClient


class TestWeather:
    """Weather api test cases"""

    def setup(self):
        """"""
        self.host = 'http://www.weather.com.cn'
        self.api = '/data/cityinfo'
        self.client = HttpClient()  # 实例化工具类HttpClient类

    @pytest.mark.parametrize('city_code, exp_city', [("101280601", "深圳1"), ("101040100", "重庆"), ("101010100", "北京"), ("101020100", "上海")])
    def test_weather(self, city_code, exp_city):
        url = f'{self.host}{self.api}/{city_code}.html'  # 拼接url
        response = self.client.Get(url=url)  # 发起get请求
        act_city = response.json()['weatherinfo']['city']  # 取出字典中的city值作为实际城市
        print(f'Expect city = {exp_city}, while actual city = {act_city}')  # 打印期望城市，实际城市
        assert exp_city == act_city
