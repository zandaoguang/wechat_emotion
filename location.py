"""
author:zandaoguang
微信公众号：视学算法
date：2018/10/26
"""
import csv
import itchat
import matplotlib.pyplot as plt
from collections import Counter
import re
import jieba
import os

import numpy as np
from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator
from scipy.misc import imread



def analyseLocation(friends):
    headers = ['NickName','Province','City']
    with open('D:/wx/Python_new/wechat/location.csv','w',encoding="utf-8",newline='') as csvFile:
        writer = csv.DictWriter(csvFile, headers)
        writer.writeheader()
        for friend in friends[1:]:
           row = {}
           row['NickName'] = friend['NickName']
           row['Province'] = friend['Province']
           row['City'] = friend['City']
           print(row)
           writer.writerow(row)

# 登陆微信
itchat.auto_login(hotReload=True)

# 获取自己的好友列表
friends = itchat.get_friends(update=True)


# 好友总数, 第一个是自己
total = len(friends[1:])
print ('好友总数:', total)
analyseLocation(friends)
