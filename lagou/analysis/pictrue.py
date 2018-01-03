import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as col
import matplotlib.cm as cm




types = [u'web前端','PHP','Android','ios',u'产品总监']



class Pictrue:

    def __init__(self,years,keyword):

        plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
        plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
        mean_values = np.random.randint(50, 101, 200)
        cmap = cm.ScalarMappable(col.Normalize(min(mean_values),
                                               max(mean_values),
                                               cm.hot))


        """
        数据渲染
        """
        N = len(years[0])
        men_means = tuple(years[1])
        ind = np.arange(N)  # the x locations for the groups
        width = 0.35       # the width of the bars

        fig, ax = plt.subplots()
        rects1 = ax.bar(ind, men_means, width, color=cmap.to_rgba(mean_values))

        # ax.set_ylabel(u'web前端')
        ax.set_title(str(keyword) + u'工作年限要求')
        ax.set_xticks(ind )

        ax.set_xticklabels(tuple(years[0]))
        # ax.legend(tuple(types))

        def autolabel(rects):
            for rect in rects:
                height = rect.get_height()
                ax.text(rect.get_x() + rect.get_width()/2., 1.01*height,
                        '%d' % int(height),
                        ha='center', va='bottom')

        autolabel(rects1)
        plt.show()


if __name__ == '__main__':
    from db import Db
    db = Db()
    key = 'web前端'
    years = db.getYearTypes(key)

    key2 = 'PHP'
    years2 = db.getYearTypes(key2)

    pic = Pictrue(years,key)

    pic2 = Pictrue(years2,key2)