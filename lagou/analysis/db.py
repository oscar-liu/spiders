# -*- coding:utf-8 -*-

import pymongo

class Db():

    def __init__(self):
        self.conn = pymongo.MongoClient('127.0.0.1')     #连接mongodb
        self.dbs  = self.conn.lagou   # 选择or创建库
        self.db = self.dbs.jobs  # 选择表
        self.types = ['web前端', 'PHP', 'Android', 'ios', '产品总监']

    def getJobs(self, sdict):

        count = self.table.find(sdict).count()
        return count

    #类目职位总数量
    def getKdCount(self):
        rs = []
        for x in self.types:
            count = self.db.find({'kd' : x }).count()
            tmp = { x : count }
            rs.append(tmp)
        return rs

    #工作年限
    def getYearNumber(self):
        rs = []
        groups = {'$group': {'_id': '$workYear', 'count': {'$sum': 1}}}

        for x in self.types:
            match = {'$match': {'kd': x }}
            pipeline = [match, groups]
            datas = self.db.aggregate(pipeline)

            datas = self.__requestData(datas)
            tmp = { x : datas }
            rs.append(tmp)
        return rs

    def getYearTypes(self,key=None):
        year = []
        count = []
        groups = {'$group': {'_id': '$workYear', 'count': {'$sum': 1}}}
        keyword = {}
        pipeline = [groups]
        if key:
            keyword = {'$match': { 'kd' : key } }
            pipeline = [keyword,groups]

        datas = self.db.aggregate(pipeline)
        datas = self.__requestData(datas)
        for x in datas:
            year.append(x['_id'])
            count.append(x['count'])
        rs = (year,count)
        return rs

    # 筛选数据
    def __requestData(self,datas):
        result = []
        for x in datas:
            result.append(x)
        return result


if __name__ == '__main__':
    db = Db()

    # rs = db.getYearTypes()
    rs2 = db.getYearTypes('web前端')
    print(rs2)
    # count = db.getKdCount()
    # print(count)

