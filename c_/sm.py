# !/usr/bin/python
# -*- coding:utf-8 -*-
import numpy as np


# 余弦距离
def distEclud(vecA, vecB):
    diseclud = np.sqrt(np.sum(np.power((vecA - vecB[0]), 2)))
    return diseclud


def distCos(vecA, vecB):
    cos_distance = float(np.sum(np.array(vecA) * np.array(vecB))) / (distEclud(vecA,np.mat(np.zeros(len(vecA)))[0]) * distEclud(vecB,np.mat(np.zeros(len(vecB)))[0]))
    return cos_distance


def paragraph_vector(sentence, model):
    paragraph_1 = []
    for word in sentence:
        if word in model.wv.index2word:
            vec = model[word]
            paragraph_1.append(vec)
        else:
            print(word + '\t\t\t——不在词汇表里' + '\n\n')
    a = np.array(paragraph_1)
    paragraph_vec = np.mean(a, axis=0)
    return paragraph_vec


def sentence_distance(sentence_1, sentence_2):
    # sentence_1 = ['营业厅', '时间', '上班']
    paragraph_vec_1 = paragraph_vector(sentence_1)
    paragraph_vec_2 = paragraph_vector(sentence_2)
    result = distCos(paragraph_vec_1, paragraph_vec_2)
    print(result)
    return result


if __name__ == "__main__":
    sentence_1 = ['营业厅', '时间', '上班']
    sentence_2 = ['营业厅', '几点', '上班']
    sentence_distance(sentence_1, sentence_2)