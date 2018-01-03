import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as col
import matplotlib.cm as cm

from db import  Db





db = Db()

categorys = db.getKdCount()
# print(categorys)
typesCount = []
types = [u'web前端','PHP','Android','ios',u'产品总监']
for x in range(len(categorys) ):
    tmp = categorys[x][types[x]]
    typesCount.append( tmp )



plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
mean_values = np.random.randint(1, 101, 100)
cmap = cm.ScalarMappable(col.Normalize(min(mean_values),
                                       max(mean_values),
                                       cm.hot))

N = 5
men_means = tuple(typesCount) #各分类数据
men_std = (2, 3, 4, 1, 2)

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, men_means, width, color=cmap.to_rgba(mean_values), yerr=men_std)

ax.set_ylabel(u'职位统计')
ax.set_title(u'招聘职位数据热度统计')
ax.set_xticks(ind )

ax.set_xticklabels(tuple(types))


def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.01*height,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(rects1)

plt.show()