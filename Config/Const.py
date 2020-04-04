import uiautomator2 as u2

#公共配置信息
sn = "SLYGK17814000005"
device = u2.connect_usb(sn)
ue = u2.Device
screenInfo = device.device_info
width = screenInfo["display"]["width"]
height = screenInfo["display"]["height"]

#58配置信息
pakage = "com.wuba"
home_win_name = "com.wuba/com.wuba.home.activity.HomeActivity"

#火山小视频配置信息
vocanalpakage = "com.ss.android.ugc.livelite"
mian_activity = "com.ss.android.ugc.livelite/com.ss.android.ugc.live.main.MainActivity"
homeid = "com.ss.android.ugc.livelite:id/wa" #首页
recommondid = "com.ss.android.ugc.livelite:id/wc" #推荐
redid = "com.ss.android.ugc.livelite:id/wf" #红包
mineid = "com.ss.android.ugc.livelite:id/wi" #我的

#微信配置信息
wepakage = "com.tencent.mm"
wechat_main_activity = "com.tencent.mm.ui.transmit.SelectConversationUI"
#//*[@resource-id="com.tencent.mm:id/dai"]/android.widget.LinearLayout[1]
norule = "resource-id="+'"'+wepakage+":id/dai"+'"'
self_xpth = "//*[@"+norule+"]/android.widget.LinearLayout[1]"#//*[@resource-id=com.tencent.mm:id/dcf]/android.widget.LinearLayout[1]
xpth_text = "【全新车】侣行汽车 雪佛兰科沃兹"
detail_xpath = "com.tencent.mm:id/atp"
read_xpath = "com.tencent.mm:id/aij"

#平安银行配置信息
main_activity = "com.pingan.launcher.activity.LauncherActivity"
share_activity = "com.pingan.componet.hybrid.webUrl.WebUrlActivity"
error_activity = "com.pingan.core.base.PocketWebViewActivity"
password = "jiangzhihong191"
pinganpakage = "com.pingan.paces.ccms"
searchid = "com.pingan.paces.ccms:id/base_header_view_middle_rl"
inputeditid = "com.pingan.paces.ccms:id/launcher_header_search_edit"
sgsearchbtn = "com.sohu.inputmethod.sogou:id/imeview_keyboard"
sr_pin = "main"
searchresult_xpath = "//*[@resource-id="+'"'+sr_pin + '"'+"]/android.view.View[1]/android.view.View[1]/android.view.View[2]"
wightid = "android:id/content"
weihaibao_xpath = "//*[@resource-id="+'"'+wightid+'"'+"]/android.widget.FrameLayout[1]/android.widget.LinearLayout[2]"
wechaticonid = "com.huawei.android.internal.app:id/icon"
share_friend_id = "J-share-channel-list"
