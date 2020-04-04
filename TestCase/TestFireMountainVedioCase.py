import unittest
from Common import uiCommon
from Config.Const import *

class TestFireMountainVedio(unittest.TestCase):

    def setUp(self):
        print("fire mountain vedio set up")
        uiCommon.startApp(vocanalpakage)
        win_name = uiCommon.getActivityName()
        if win_name !="":
            print("current win name is: " + win_name[0])

    def testStep(self):
        print("test step into")
        uiCommon.autoGetMoney()

    def tearDown(self):
        uiCommon.quitApp(vocanalpakage)
        pass


if __name__ == '__main__':
    unittest.main()
    pass

