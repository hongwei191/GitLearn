def fortest():
    templist = ['gsmlte',(7,9,0)]
    mmldata = [["nrlte",(1,2,3)],['ltewcdma',(4,5,6)],['gsmlte',(7,9,0)]]
    temp = 'ltewcdma'
    singleinfolist = []

    #移除用户自己触发的recovery
    # for singleinfo in mmldata:
    #     if temp ==singleinfo[0]:
    #         mmldata.remove(singleinfo)

    #保存数据,空list也是可以遍历的
    for singleinfo in mmldata:
        singleinfolist.append(singleinfo[0])
    if templist[0] not in singleinfolist:
        mmldata.append(templist)

    print(mmldata)








if __name__ == '__main__':
    fortest()