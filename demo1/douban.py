"""
1. 使用request 获取页面HTML
2. 使用lxml的etree，再使用xpath解析元素
3. 使用pandas导出csv || open
"""

import requests
from lxml import etree
import pandas
import  time

step = 20
max_pages = 10
result = []
n = 0
# for n in range(max_pages):

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
    'Accept': '*/*',
    'Host': 'movie.douban.com',
    'Referer': 'https://movie.douban.com/subject/5350027/comments?start=60&limit=20&sort=new_score&status=P&percent_type=',
}
cookie = {
    'Cookie' : 'bid=CwUwonepk4w; ll="118282"; _vwo_uuid_v2=10FD15511064BA07594881EAEC23948A|1d0aed7430e665d639c34d0aa826c59d; __utmz=30149280.1509328450.5.5.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmc=30149280; __utmc=223695111; __utmz=223695111.1515142874.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ap=1; ps=y; ue="vip_baidu@qq.com"; dbcl2="13400743:9H60Po4wRQI"; ck=f9x4; push_noty_num=0; push_doumail_num=0; _pk_id.100001.4cf6=a1c78dce8e65d1cf.1515142874.2.1515156478.1515144253.; _pk_ses.100001.4cf6=*; __utma=30149280.484554511.1498021427.1515142874.1515156478.11; __utmb=30149280.0.10.1515156478; __utma=223695111.1952103988.1515142874.1515142874.1515156478.2; __utmb=223695111.0.10.1515156478'
}





while 1:

    page = step*n
    url = 'https://movie.douban.com/subject/5350027/comments?start=%s&limit=20&sort=new_score&status=P&percent_type=' % page
    # r = requests.get(url).text
    r = requests.get(url, headers=headers ,cookies=cookie ).text


    s = etree.HTML(r)
    rs = s.xpath('//div[@class="comment-item"]')
    print('第'+str(n)+"次")
    time.sleep(1)

    if len(rs) <= 1:
        break
    else:
        n = n+1

        for x in rs :
            avatar = x.xpath('./div[@class="avatar"]/a/img/@src')
            nickname = x.xpath('./div[@class="avatar"]/a/@title')
            votes = x.xpath('.//span[@class="votes"]/text()')
            comment = x.xpath('./div[@class="comment"]/p/text()')
            tmp = {
                'avatar' : avatar[0],
                'nickname' : nickname[0],
                'votes' : votes[0],
                'comment': comment[0]
            }
            result.append(tmp)

"""
使用pandas生成csv文件
"""
excelData = pandas.DataFrame(result)
excelData.to_csv('douban.csv')


