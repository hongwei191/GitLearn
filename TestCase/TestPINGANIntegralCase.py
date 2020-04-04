from Common import uiCommon
from Config.Const import *
import unittest

class TestPINGANIntegralCase(unittest.TestCase):

    def setUp(self):
        pass
        uiCommon.startApp(pinganpakage)

    def test_step(self):
        #分享任务自动化
        # uiCommon.wait(3)
        # uiCommon.classlickMethod(searchid)
        # uiCommon.send_keys(inputeditid,"乐分享")
        # uiCommon.wait(2)
        # uiCommon.clickMethod(searchresult_xpath)
        # uiCommon.activity_assert(share_activity)
        # uiCommon.wait(2)
        # uiCommon.share_getintegral(20)

        #阅读任务自动化
        uiCommon.wait(2)
        uiCommon.startApp(wepakage)
        print("into self detail page")
        uiCommon.clickMethod(self_xpth)

        print("click share page")
        for i in range(0,40):
            # uiCommon.clickMethod(detail_xpath)
            uiCommon.clickMethod(read_xpath)
            uiCommon.wait(3)
            uiCommon.goBack()

    def tearDown(self):
        print("wechat teardown into")
        # uiCommon.quitApp(wepakage)


if __name__ == '__main__':
    unittest.main()
    pass
