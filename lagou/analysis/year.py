
from db import  Db
from pictrue import Pictrue



db = Db()

types = [u'web前端','PHP','Android','ios',u'产品总监']


for x in types:
    datas = db.getYearTypes(x)
    pic = Pictrue(datas, x)

# datas = db.getYearTypes('')
# pic = Pictrue(datas,"互联网热门职位")