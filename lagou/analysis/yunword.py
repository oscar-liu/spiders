
from db import  Db
from wordcloud import  WordCloud


db = Db()
#
# datas = "".join( db.getWords() )
#
# # 过滤掉一些字符
# r = ["工作内容","岗位职责","任职要求","任职资格","岗位要求","职位描述","熟悉","工作职责"]
# rs = datas.replace(r[0],"").replace(r[1],"").replace(r[2],"").replace(r[3],"").replace(r[4],"").replace(r[5],"").replace(r[6],"").replace(r[7],"")

#取数据
rs = "".join(db.getWordsFuli())

font = r'/Users/oscar/PycharmProjects/spiders/venv/lib/python3.6/site-packages/matplotlib/mpl-data/fonts/ttf/simhei.ttf'

wordcloud = WordCloud(background_color="white", font_path=font, width=1000, height=860, margin=2).generate(rs)

# %pylab inline
import matplotlib.pyplot as plt
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()