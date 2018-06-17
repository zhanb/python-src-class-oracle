#!/account/work/zhangbo/python/python/bin
#coding=utf-8
from sys import path
path.append('../class')
import deal_oracle 

if __name__ == "__main__":
    user=''
    passwd=''
    tns=''
    i=0
    fp=open("../data/database.cfg",'r')
    try:
        for line in fp.readlines():
            line=line.strip('\n')
            if line.split('=',1)[0] == 'user':
                user=line.split('=',1)[1]
            elif line.split('=',1)[0] == 'passwd':
                passwd=line.split('=',1)[1]
            elif line.split('=',1)[0] == 'tns':
                tns=line.split('=',1)[1]
    finally:
        fp.close()
    login=user + '/' + passwd + '@' + tns
    myOracle = deal_oracle.DealOracle(login)
    myOracle.connectdb()
    #select
    cur = myOracle.newcur()
    result = myOracle.select_sql("select serv_id from serv where serv_id in(60033017564,10002768220,60002665838)",cur)
    myOracle.closecur(cur)
    print(result)
    for i in result:
        print(i)
    #insert
    '''
    aa = []
    for i in 60033017564,10002768220,60002665838:
        aa.append((60033017564,))
        print(aa)
    cur = myOracle.newcur()
    result = myOracle.exec_sql("insert into zhangbo_serv(serv_id) values(:1)",cur,aa)
    myOracle.commit()
    myOracle.closecur(cur)
    '''
    #update
    '''
    cur = myOracle.newcur()
    result = myOracle.exec_sql("update zhangbo_serv set serv_id = 1111",cur)
    myOracle.commit()
    myOracle.closecur(cur)
    '''
    M = []
    for i in 1111,11111:
        M.append((i,))
    cur = myOracle.newcur()
    result = myOracle.exec_sql("update zhangbo_serv set serv_id = 222 where serv_id = :1",cur,M)
    myOracle.commit()
    myOracle.closecur(cur)
