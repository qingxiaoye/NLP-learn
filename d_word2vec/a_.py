# !/usr/bin/python
# -*- coding:utf-8 -*-
from gensim import models

from paragraph_vector import question_similar, answer_similar

# 1.上班时间；2.最低套餐；3.网速慢

sentences = [['first', 'sentence'], ['second', 'sentence']]
sentences2 = [['今天天气不错啊'], ['你们公司几点上班']]

# train word2vec on the two sentences
model = models.Word2Vec(sentences2, min_count=1)
print(model.wv.index2word)
print()
