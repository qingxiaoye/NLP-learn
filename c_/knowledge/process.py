# -*- coding: utf-8 -*-
import logging, jieba, os, re


def get_stopwords():
    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)
    # 加载停用词表
    stopword_set = set()
    with open("stopwords.txt", 'r', encoding="utf-8") as stopwords:
        for stopword in stopwords:
            stopword_set.add(stopword.strip("\n"))
    return stopword_set


def paragraph_process(paragraph):
    # 该函数用于句子分词、去停用词
    stopwords = get_stopwords()
    paragraph_contents = []
    words = jieba.cut(paragraph, cut_all=False)
    for word in words:
        if word not in stopwords:
            paragraph_contents.append(word)
    return paragraph_contents
