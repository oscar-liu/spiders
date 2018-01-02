# -*- coding:utf-8 -*-

import requests
import time
from lxml import etree
from db import Db

searchKeywors = ['web前端','PHP','Android','ios','产品总监']


cookie = {
    'Cookie'  : 'JSESSIONID=ABAAABAACBHABBI3A647C0349919858E41C2A8C3AD1A7E3; _ga=GA1.2.83764640.1514512345; user_trace_token=20171229095224-ea9c22b6-ec3a-11e7-b68c-525400f775ce; LGRID=20171229102054-e5bc70b4-ec3e-11e7-b691-525400f775ce; LGUID=20171229095224-ea9c254b-ec3a-11e7-b68c-525400f775ce; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1514512345; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1514514054; index_location_city=%E6%B7%B1%E5%9C%B3; _gid=GA1.2.1037774580.1514512349; TG-TRACK-CODE=search_code; SEARCH_ID=e1736980439a4a58843e94913853b2cb; X_HTTP_TOKEN=dae277108342154722aa3afeff82178a'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:57.0) Gecko/20100101 Firefox/57.0',
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'Host':'www.lagou.com',
    'Origin':'https://www.lagou.com',
    'Referer':'https://www.lagou.com/jobs/list_web%E5%89%8D%E7%AB%AF?city=%E6%B7%B1%E5%9C%B3&cl=false&fromSearch=true&labelWords=&suginput=',
}

data = {
    'first': False,
    'pn':1,
    'kd': 'Android',
}

detail_cookies = {
    'Cookie' : 'JSESSIONID=ABAAABAACBHABBI3A647C0349919858E41C2A8C3AD1A7E3; _ga=GA1.2.83764640.1514512345; user_trace_token=20171229095224-ea9c22b6-ec3a-11e7-b68c-525400f775ce; LGSID=20171229095224-ea9c23b1-ec3a-11e7-b68c-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; LGRID=20171229102042-dee51a95-ec3e-11e7-b691-525400f775ce; LGUID=20171229095224-ea9c254b-ec3a-11e7-b68c-525400f775ce; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1514512345; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1514514043; index_location_city=%E6%B7%B1%E5%9C%B3; _gid=GA1.2.1037774580.1514512349; TG-TRACK-CODE=search_code; SEARCH_ID=f1a55bd8c2074125ae5bd8dc7e2813a6; X_HTTP_TOKEN=dae277108342154722aa3afeff82178a'
}



def get_job(data):
    # url = 'https://www.lagou.com/jobs/positionAjax.json?city=深圳&needAddtionalResult=false&isSchoolJob=0'
    url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E6%B7%B1%E5%9C%B3&needAddtionalResult=false&isSchoolJob=0'
    page = requests.post(url=url, cookies=cookie, headers=headers, data=data)
    page.encoding = 'utf-8'
    result = page.json()

    if result['success'] == False:
        print(result['msg'])
        print("等待10分钟后继续爬取")
        time.sleep(10)

    # 实例化DB类
    db = Db()
    # print(result)
    jobs = result['content']['positionResult']['result']


    for job in jobs:
        positionId = job['positionId']  # 主页ID

        detail_url = 'https://www.lagou.com/jobs/{}.html'.format(positionId)
        response = requests.get(url=detail_url, headers=headers, cookies=detail_cookies)
        response.encoding = 'utf-8'
        tree = etree.HTML(response.text)
        desc = tree.xpath('//*[@id="job_detail"]/dd[2]/div/p/text()')
        job['desc'] = desc
        job['kd'] = data['kd']
        # for des in desc:
        #     print(des)
        db.insertJobs(job)  # 入库


def url(data):

    for x in range(1,32):
        data['pn'] = x
        get_job(data)
        time.sleep(120) #60秒请求一次
        print('第'+str(x)+"次请求")

if __name__ == '__main__':
    url(data)



