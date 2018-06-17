#!/usr/bin/env python
#coding=utf-8
import cx_Oracle as Oracle

class DealOracle:
    def __init__(self,oracle_login):
        self.oracle_login = oracle_login
        self.con = None
    def connectdb(self):
        if self.con == None:
            self.con = Oracle.connect(self.oracle_login)
        if self.con != None:
            return True
        else:
            return False
    def closedb(self):
        if self.con:
            self.conn. close()
            self.conn = None
    def newcur(self):
        cur = self.con.cursor()
        if cur:
            return cur
        else:
            print ("#Error# Get New Cursor Failed.")
            return None
    def closecur(self,cur):
        if cur:
            cur.close()
    def commit(self):
        self.con.commit()
    def rollback(self):
        self.con.rollback()
    def select_sql(self,sql,cur):
        c = cur.execute(sql)
        result = c.fetchall()
        return result
    def exec_sql(self,sql,cur,parm_list = None):
        if parm_list:
            cur.prepare(sql)
            result = cur.executemany(None,parm_list)
        else:
            result = cur.execute(sql)
        return result
