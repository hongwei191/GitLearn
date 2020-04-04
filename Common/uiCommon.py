import uiautomator2 as u2
import os,sys,time,re
from Config.Const import *

def startApp(pakage):
    device.app_start(pakage)
    wait(5)

def getScreenInfo():
    screenInfo = device.device_info
    width = screenInfo["display"]["width"]
    height = screenInfo["display"]["height"]
    print("screenInfo width is: %s ;" % width)
    print("screenInfo height is: %s " % height)
    return width,height


def getActivityName():
    appinfo = device.app_current()
    activityname = appinfo.get("activity")
    pakagename = appinfo.get("package")
    print("activity name is: "+activityname)
    print("pakage name is: "+pakagename)
    return activityname

def startActivity(activity):
    appinfo = getActivityName()
    if activity == appinfo:
        print("current activity is start activity"+ appinfo)
        return True
    else:
        activity = pinganpakage + "/" + activity
        cmd = "adb shell am start -n %s" % activity
        print(cmd)
        os.system(cmd)

def clickMethod(element):
    print(element)
    try:
        if str(element).startswith("com") or str(element).startswith("android"):
            device(resourceId=element).click()
        elif re.findall("//", str(element)):
            device.xpath(element).click()
        else:
            device.d(text=element).click()
    except Exception as e:
        print("clickMethod exception print conent e")
        print(e)

def scroll_screen():
    '''
    向上滑动
    :return:
    '''
    u2.Session.swipe(device,fx=width/2,fy=height * 3 / 4,tx=0,ty=0)
    pass

def click_positonone():
    u2.Session.click(device,1260,1902)

def click_positon(device,weight,height):
    print(weight,height)
    u2.Session.click(device,weight,height)

def goHome():
    device.press("home")

def checkTextIsExist(text):
    """
    检查文本是否存在
    :param text:控件文本
    :return:文本存在返回true，不存在返回false
    """
    exist = False
    xml = device.dump_hierarchy()
    if re.findall(text,xml):
        exist = True
        print("text is exist：{}".format(text))
    else:
        print("text is no exist: {}".format(text))
    return exist

def goBack():
    device.press("back")

def checkIdIsExist(id):
    """
    检查控件id是否存在
    :param id: 控件id
    :return: 存在返回true，不存在返回false
    """
    exist = False
    xml = device.dump_hierarchy()
    if re.findall(id, xml):
        exist = True
        print("id is exist：{}".format(id))
    else:
        print("id is no exist: {}".format(id))
    return exist

def getWidgetProp():
    # device(resourceId='com.wuba:id/systemMessage')
    attribute = u2.xpath.attrib()

    print(attribute)
def getGold():
    print("领取宝箱金币.......")
    clickMethod(redid)
    if checkTextIsExist("开宝箱得金币"):
        print("点击坐标领取金币")

        click_positonone()
        time.sleep(1)
    clickMethod(homeid)

def autoGetMoney():
    clickMethod(homeid)
    for i in range(0, 10000):
        scroll_screen()
        time.sleep(25)
        # if checkTextIsExist("宝箱"):
        #     getGold()

def wait(second=1):
    time.sleep(second)

def quitApp(pakage):
    print("quit app pakage name is:" + pakage )
    device.app_stop(pakage)

def send_keys(element, sendtext):
        '''
        文本输入
        driver: 操作对象
        sendtext:输入的文案
        element:元素名称
        logtext:打印log的文案
        :return:
        '''
        device(resourceId=element).set_text(sendtext)

def sougou_serachbutton():
    if checkIdIsExist(sgsearchbtn):
        clickMethod(sgsearchbtn)
        clickMethod(sgsearchbtn)

def share_getintegral(count):
    '''
    分享任务，获取积分
    :param count:点击次数
    :return:
    '''
    wait(3)
    for i in range(0,count):
        click_positon(device,750,860)#点击微分享
        if getActivityName() != share_activity:
            goBack()
        click_positon(device, 750, 860)
        wait(2)
        click_positon(device,470,1570)#分享好友弹窗，微信好友坐标
        # if checkIdIsExist(share_friend_id):
        #     wait(1)
        #     print("111")
        #     click_positon(device, 470, 1570)
        if checkIdIsExist(wechaticonid):
            wait(1)
            click_positon(device,540,1180)
            if checkIdIsExist(wechaticonid):
                wait(1)
                click_positon(device, 540, 1180)
        else:
            wait(1)
            click_positon(device, 540, 1190)
            click_positon(device, 540, 1190)
        wait(3)
        current_winname = getActivityName()
        if current_winname == wechat_main_activity :
            goBack()
        wait(1)
        click_positon(device,770,1900)
        current_winname = getActivityName()
        print("current_winname is: "+ current_winname)
        if current_winname == wechat_main_activity :
            goBack()
        elif current_winname == error_activity:
            print("error activity page")
            goBack()
            wait(1)
        elif current_winname == share_activity:
            continue
        #     if checkIdIsExist(share_friend_id):
        #         click_positon(device, 465, 1570)
        #         if checkIdIsExist(wechaticonid):
        #             wait(2)
        #             click_positon(device, 540, 1180)
        #     else:
        #         print("current activity == share activity,but popwin no exist")
        #         return False
        # else:
        #     print("error page,please again load run")
        #     return False

def activity_assert(ext_activity):
    while(True):
        act_activity = getActivityName()
        if act_activity == ext_activity:
            return True
        else:
            continue
def tanchuan():
    click_positon(device, 540, 1180)
if __name__ == '__main__':
    # startActivity(share_activity)

    getActivityName()
    # print(checkIdIsExist("J-share-channel-list"))
    # clickMethod(searchid)
    # send_keys(inputeditid,"乐分享")
    # clickMethod(searchresult_xpath)
    # share_getintegral(1)
    # tanchuan()
    # print(self_xpth)
    # startApp(pakage)
    # autoGetMoney()
    pass