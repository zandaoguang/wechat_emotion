"""
author:zandaoguang
微信公众号：视学算法
date：2018/10/26
"""
import itchat
import matplotlib.pyplot as plt
from collections import Counter
import re
import jieba
from wordcloud import WordCloud, ImageColorGenerator
from scipy.misc import imread

# itchat.auto_login(hotReload=True)
# friends = itchat.get_friends(update=True)

def analyseSex(firends):
    sexs = list(map(lambda x:x['Sex'],friends[1:]))
    counts = list(map(lambda x:x[1],Counter(sexs).items()))
    labels = ['Unknow','Male','Female']
    colors = ['red','yellowgreen','lightskyblue']
    plt.figure(figsize=(8,5), dpi=80)
    plt.axes(aspect=1)
    plt.pie(counts, #性别统计结果
            labels=labels, #性别展示标签
            colors=colors, #饼图区域配色
            labeldistance = 1.1, #标签距离圆点距离
            autopct = '%3.1f%%', #饼图区域文本格式
            shadow = False, #饼图是否显示阴影
            startangle = 90, #饼图起始角度
            pctdistance = 0.6 #饼图区域文本距离圆点距离
    )
    plt.legend(loc='upper right',)
    plt.title(u'%s' % friends[0]['NickName'])
    plt.show()

# 登陆微信
itchat.auto_login(hotReload=True)

# 获取自己的好友列表
friends = itchat.get_friends(update=True)


# 好友总数, 第一个是自己
total = len(friends[1:])
print ('好友总数:', total)
analyseSex(friends)