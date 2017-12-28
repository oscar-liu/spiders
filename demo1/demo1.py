"""
1. 使用request 获取页面HTML
2. 使用lxml的etree，再使用xpath解析元素
3. 使用pandas导出csv
"""

import requests
from lxml import etree
import pandas

url = 'https://movie.douban.com/subject/5350027/comments?status=P'
r = requests.get(url).text

s = etree.HTML(r)
rs = s.xpath('//div[@class="comment-item"]')
result = []
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

excelData = pandas.DataFrame(result)
excelData.to_csv('comment.csv')