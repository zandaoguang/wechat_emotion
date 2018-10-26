#!/usr/bin/python
# -*- coding:utf-8 -*-
# **************************
# * Author      :  baiyyang
# * Email       :  baiyyang@163.com
# * Description :  
# * create time :  2018/1/20上午11:47
# * file name   :  mywechat.py

import itchat
import matplotlib.pyplot as plt
from collections import Counter
import re
import jieba
from wordcloud import WordCloud, ImageColorGenerator
from scipy.misc import imread
plt.rcParams['font.sans-serif'] = ['SimHei']




# 登陆微信
itchat.auto_login(hotReload=True)

# 获取自己的好友列表
friends = itchat.get_friends(update=True)


# 好友总数, 第一个是自己
total = len(friends[1:])
print ('好友总数:', total)

# 查看好友男友比例
male = female = other = 0
for friend in friends[1:]:
    sex = friend['Sex']
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        other += 1

sexes = list()
sexes.append(float(male) * 100 / total)
sexes.append(float(female) * 100 / total)
sexes.append(float(other) * 100 / total)

print ('男性好友: %-.2f%%' % sexes[0])
print ('女性好友: %-.2f%%' % sexes[1])
print ('不明身份好友: %-.2f%%' % sexes[2])

#draw(sexes, ['male', 'female', 'other'], 'Gender', 'Proportion', "Gender's proportion of my friends", type=0)

signatures = list()
provinces = list()
cities = list()

# 过滤掉签名中的冗余字符
pattern = re.compile('<[^>]+>')

for friend in friends:
    if friend['Signature']:
        signature = pattern.sub('', friend['Signature']).strip().replace('&amp;', '')
        signatures.append(signature)
    provinces.append(friend['Province'] if friend['City'] else 'NULL')
    cities.append(friend['City'] if friend['City'] else 'NULL')


# 绘制好友省份柱状图
pro = sorted(Counter(provinces).most_common(10), key=lambda d: -d[1])
label, num = zip(*pro)
#draw(num, label, 'Provinces', 'nums', 'Province distribute of my friends')

# 绘制好友城市柱状图
cit = sorted(Counter(cities).most_common(10), key=lambda d: -d[1])
label, num = zip(*cit)
#draw(num, label, 'Cities', 'nums', 'City distribute of my friends')

# 根据好友个性签名生成词云
text = ''.join(signatures)
# 使用全模式，尽可能多的切分
wordlist = jieba.cut(text, cut_all=True)

bg_pic = imread('heart.jpg')
wordcloud = WordCloud(mask=bg_pic, font_path='D:/wx/Python_new/wechat/itchat.pkl', background_color='white',
                      max_words=2000, max_font_size=100, min_font_size=10, scale=1.5).generate(' '.join(wordlist))

# 从图片背景生成颜色值
image_colors = ImageColorGenerator(bg_pic)

plt.imshow(wordcloud.recolor(color_func=image_colors))
plt.imshow(wordcloud)
plt.axis('off')
plt.show()







