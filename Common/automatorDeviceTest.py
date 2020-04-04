import uiautomator2 as u2
import pytest
import allure
import os
class TestReport():
    # def firstInto():
    #     print("第一次自己写入口方法")
    #
    # def deviceInfoConnect():
    #     d = u2.connect_usb("SLYGK17814000005")
    #     return d

    @allure.feature("test_add")
    def test_add(self):
        """
        加法运算
       """
        assert 0==0

    # @allure.feature("test_subtraction")
    # def test_subtraction(a=1,b=3):
    #     '''
    #     减法运算
    #     :param a: 减数
    #     :param b: 被减数
    #     :return: 差
    #     '''
    #     assert a-b == 5
    #
    # @allure.feature("test_multiplication")
    # def test_multiplication(a=1,b=3):
    #     '''
    #     乘法运算
    #     :param a: 乘数
    #     :param b: 被乘数
    #     :return: 积
    #     '''
    #     assert a*b == 3
    #
    # @allure.feature("test_division")
    # def test_division(a=1,b=3):
    #     '''
    #     除法运算
    #     :param a: 除数
    #     :param b: 被除数
    #     :return: 商
    #     '''
    #     assert a/b == 2

    # def generatorReport():
    #     pass

if __name__ == '__main__':
    # firstInto()
    # test_add(a,b)
    # test_subtraction(a,b)
    # test_multiplication(a,b)
    # test_division(a,b)
    pytest.main(['-s', '-q', 'automatorDeviceTest.py', '--alluredir', './report/xml'])
    os.system("allure generate report/xml -o report/html")
    # generatorReport()
    pass