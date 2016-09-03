# coding=utf8
import json

json_arr = json.loads(
    '{ "status":true,"total":701,"tngou":[{"count":8689,"description":"材料芹菜叶，黑木耳，白芝麻（熟），盐，花椒油，香油做法1、芹菜叶洗净，放入加了盐的沸水里轻焯一下，捞出攥干水分，弄成小段；2、将泡发好的黑木耳剔除根部，用清水反复冲洗干净，然后过沸水焯熟，过凉水后沥干水分，切成细丝；3、将上述材料与白芝麻一起放入调理盆，加入适量的盐、花椒油和香油，混合均匀，渍上片刻，即可盛盘食用了","fcount":0,"food":"芹菜叶,黑木耳,白芝麻,花椒油,香油","id":164,"images":"","img":"/cook/150802/fc43c4736144faf2c52aed1965aa5a19.jpg","keywords":"黑木耳 菜叶 花椒油 白芝麻 水分 ","name":"芹菜叶拌木耳","rcount":0}]}')
print(json_arr["tngou"][0]['description'])
