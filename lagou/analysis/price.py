
from db import  Db
from pictrue import Pictrue



db = Db()


priceList = [u'2k-5k',u'5k-10k',u'10k-15k',u'15k-25k',u'25k-50k']
types = [u'web前端','PHP','Android','ios',u'产品总监']

datas = db.getPrices()
for d in datas:
    data = d
    key = tuple(d.keys())
    price_count = []
    for a in d[key[0]]:
        count = len(a)
        price_count.append(count)

    _tuple = ( priceList,price_count )

    pic = Pictrue( _tuple , key[0])
    # pic = Pictrue(datas, x)

# datas = db.getYearTypes('')
# pic = Pictrue(datas,"互联网热门职位")