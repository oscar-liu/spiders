# -*- coding:utf-8 -*-

import pymongo

class Db():

    def __init__(self):
        self.conn = pymongo.MongoClient('127.0.0.1')     #连接mongodb
        self.dbs  = self.conn.lagou   # 选择or创建库

    #职位列表
    def insertJobs(self,datas):
        self.table = self.dbs.jobs  # 选择or创建表
        # 入库
        if type(datas) is dict:
            self.table.insert(datas)
        elif type(datas) is list:
            for x in datas:
                self.table.insert(x)

    def insertJobDetail(self,info):
        self.detail = self.dbs.jobsdetail
        self.detail.insert(info)


# if __name__ == '__main__':
#     db = Db()
#     data = {'name': 'litchi2'}
#     datas = [{'name': 'litchi3'},{'name': 'litchi4'},{'name': 'litchi5'}]
#     db.insertJobs(datas)

