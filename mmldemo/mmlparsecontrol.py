import os,sys,toml
from functools import lru_cache
from cachetools import cached

@cached(cache={})
def tomlparse(path):
    result = toml.load(path)
    print(result)
    return result

def mmlassignvalue(env_config):
    mml = '''ADD ONE:MCC ={0},MNC={2},CELL={4};ADD TWO: MNC={1},MCC={0};ADD THREE:ID={0},CELL={1},MNC={2},MCC={3};
    ADD FOUR:MCC ={0},MNC={2},CELL={4};ADD FIVE: MNC={1},MCC={0};ADD SIX:ID={0},CELL={1},MNC={2},MCC={3};'''
    # mml = "ADD ONE:MCC ={0},MNC={2},CELL={4};"
    if mml.endswith(";"):#去掉命令行末尾分号，否者拆分后为实际命令条数+1（空串）
        mml = mml[:-1]
    mml = mml.split(";")
    print("first mml: ",mml)
    command = ''#赋值后拼接后KV
    basicmml = ''#命令关键字
    paramstr = ''#参数串
    singlemml = ""#多条命令拆分，参数赋值后拼接成的单条命令
    executemml = ""#多条命令拆分，参数赋值后并拼接最终发送的mml
    for i in range(len(mml)):
        endmml = mml[i].split(":")
        basicmml=endmml[0]
        paramstr=endmml[1]
        print(basicmml)
        print(paramstr)
        kv_list = paramstr.split(",")
        paramstr = ''
        for j in range(len(kv_list)):
            print("第 %s 次kv遍历" % str(j))
            key_value_list = kv_list[j].split("=")
            key = key_value_list[0].strip()
            value = key_value_list[1]
            mark = value[1:len(value)-1]
            if int(mark) % 2 == 0:
                    value =env_config["C3"][key]#C3为逻辑小区标识
                    print("assign after value1: "+str(value))
            else:
                    value = env_config["C4"][key]
                    print("assign after value2: " +str(value))
            command = key+"="+str(value)+","
            paramstr = paramstr+command
        print(command)
        print(paramstr)
        singlemml = basicmml+":"+paramstr[:-1]+";"
        print(singlemml)
        executemml = executemml+singlemml
    print("成功再次一举了： "+executemml)
    print("str control mothod")
    print("12345{}".format(789))
    print("------------------------")


if __name__ == '__main__':
   ROOTPATH = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
   env_config_path = os.path.join(ROOTPATH,"resource\env_config_toml.toml")
   env_iot_path = os.path.join(ROOTPATH,"resource\env_iot_toml.toml")
   print(ROOTPATH,env_config_path,env_iot_path)
   env_config = tomlparse(env_config_path)
   print("********************************************************")
   mmlassignvalue(env_config)