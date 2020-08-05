# !/usr/bin/python
# -*- coding:utf-8 -*-
import os
from gensim import models


class MySentences(object):
    def __init__(self, dirname):
        self.dirname = dirname

    def __iter__(self):
        for fname in os.listdir(self.dirname):
            for line in open(os.path.join(self.dirname, fname)):
                yield line.split()


sentences = MySentences(r'F:\yjcloud-learn\NLP-learn\d_word2vec\doc')  # a memory-friendly iterator
model = models.Word2Vec(sentences)
print(print(model.wv.index2word))
