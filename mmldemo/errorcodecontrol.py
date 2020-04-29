'''
1,压测无法区分60/70LTE及GSM
2,同频异频可以根据keyword结尾关键字区分，然后找到对应IP的所有cellname数据，然后区分
3,mml命令是否区分60/70/80，
'''
def forloopcontrol(keyword_list):
    for index in range(len(keyword_list)):
        print(keyword_list[index])
        if "2" not in keyword_list[index]:
            src_rat_assign(keyword_list[index][0])
            target_rat = "NA"
        else:
            src_rat_assign(keyword_list[index][0])
            tager_rat_assign(keyword_list[index][2])
        #调用锁定mml接口->调用修改mml参数接口->setmml，将返回结果保存即可
        #继续下一个keyword处理

def  tager_rat_assign(flag_mark):
    if "N" in flag_mark:
        target_rat = "NR"
        target_cellname = "NR1"
    elif "L" in flag_mark:
        target_rat = "LTE"
        target_cellname = "LTE4"
    elif "W" in flag_mark:
        target_rat = "WCDMA"
        target_cellname = "WCDMA13"
    elif "T" in flag_mark:
        target_rat = "TDSCDMA"
        target_cellname = "TDSCDMA8"
    elif "G" in flag_mark:
        target_rat = "GSM"
        target_cellname = "GSM8"
    return target_rat,target_cellname

def src_rat_assign(flag_mark):
    if "N" in flag_mark:
        src_rat = "NR"
        src_cellname = "NR1"
    elif "L" in flag_mark:
        src_rat = "LTE"
        src_cellname = "LTE4"
    elif "W" in flag_mark:
        src_rat = "WCDMA"
        src_cellname = "WCDMA13"
    elif "T" in flag_mark:
        src_rat = "TDSCDMA"
        src_cellname = "TDSCDMA8"
    elif "G" in flag_mark:
        src_rat = "GSM"
        src_cellname = "GSM8"
    return src_rat,src_cellname

def loopfor():
    for i in range(3):
        print(i)
        flag = False
        print("1cen")
        for j in range(3):
            print(j)
            print("2cen")
            for index in range(3):
                print(index)
                flag=True
                if flag:
                    break
            if flag:
                break
def controlerrorcode(mml):
    if 'nRETCODE' in mml:
        location= mml.find('nRETCODE')#出现的位置
        start = mml[location:]#出出现位置截取到字符串末尾
        end = str(start).find(" ")#错误码后的第一个空格出现的位置
        code = start[0:end]#错误码
        print(code)
        #直接判断错误码是否在返回字符串内，如果在就直接返回处理结果
        if 'nRETCODE=939589976' in mml:
            print('此错误码可以忽略')
        return True


def dictdatamade():
    nRETCODE=['939589976','12345','75641']
    result = {}
    if '12345' in nRETCODE:
        print("code {0} in error code".format(12345) )
        print("222321")
    for i in range(3):
        result.setdefault(i,nRETCODE[i])
    return result

def dictadddata(tupledata):
    result = dictdatamade()
    print(result)

if __name__ == '__main__':
    src_cell = ["LTE", 'WCDMA', 'GSM']
    target_cell = ['NA', 'NR', 'LTE']
    keyword_list = ['LTETIMER', 'GSMTIMER', 'W2G', 'NRTIMER']
    mml1 = 'ADD NREXTERNALCELL:MCC="460",Mnc="60",GnodebId=1211,cellId =0,Dlarfcn=630720,PhyCellId=2000,' \
           'Tac=1;nRETCODE=939589976 Parameter not found'
    mml2 = 'ADD NREXTERNALCELLPLMN:Mcc="460",SharedMnc="60",GnodebId=1211,CellId=0,SharedMcc="460",SharedMnc="60",' \
           'nRETCODE=1967128770 Each of the multiple operators share the same external cell must have a unique ' \
           'combination of MCC and MNC'
    # print(mml1)
    # print(mml2)
    # forloopcontrol(keyword_list)
    # controlerrorcode(mml1)
    # loopfor()
    dictadddata(tupledata=None)
    pass