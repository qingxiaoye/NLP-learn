# !/usr/bin/python
# -*- coding:utf-8 -*-

from gensim import models

from paragraph_vector import question_similar, answer_similar
# 1.上班时间；2.最低套餐；3.网速慢

model = models.Word2Vec.load(r"F:\yjcloud-learn\NLP-learn\c_\knowledge\qia_model\wiki_corpus00.model")
question_similar_result = question_similar(1, '营业厅，什么时候上班', model)
question_similar_result2 = question_similar(1, '上班时间是什么时候', model)

# agent_similar = answer_similar(1, '平常周一到周五时间直接去就行。', model)
