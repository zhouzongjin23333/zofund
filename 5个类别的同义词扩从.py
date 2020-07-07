import pandas as pd
import re
import jieba.posseg as psg
import jieba
import gensim
import numpy as np

text = pd.read_csv('word_split.txt',encoding='utf-8')
texts = [line.split(' ') for line in open('word_split.txt',encoding='utf-8')]

print('开始下载模型')
model = gensim.models.Word2Vec.load(r'model.bin')
print('下载完毕')

# 行业景气
industry_list = ['景气','回暖','复苏','量价其升','行业']

# 涨价
price_list = ['涨价','提价']

# 超预期
expecting_list = ['高于','预期','超']

# 转型
changing_list = ['转型','外延','新业务']

# 份额提升
market_share_list = ['份额','扩张','规模','替代','放量','拓展','并购','集中度']

def expect(list):
    all_list = set()
    for word in list:
        word_list = set()
        for i in texts[0:100]:
            for k in i:
                try:
                    c = model[k]
                    score = model.similarity(word, k)
                    if score >= 0.5:
                        print(k)
                        word_list.add(k)
                except KeyError:
                    # print("not in vocabulary")
                    c = 0
        all_list = all_list | word_list
    print(all_list)
    return all_list


industry_list = expect(industry_list)
price_list = expect(price_list)
expecting_list = expect(expecting_list)
changing_list = expect(changing_list)
market_share_list = expect(market_share_list)





