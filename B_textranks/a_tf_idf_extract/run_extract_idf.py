# !/usr/bin/python
# -*- coding:utf-8 -*-


from operator import itemgetter
import jieba
from jieba import posseg as psg
from idf_load import idf_loader


def extract_tags(sentence, topK=20, withWeight=False, allowPOS=(), withFlag=False):
    """
    Extract keywords from sentence using TF-IDF algorithm.
    Parameter:
        - topK: return how many top keywords. `None` for all possible words.
        - withWeight: if True, return a list of (word, weight);
                      if False, return a list of words.
        - allowPOS: the allowed POS list eg. ['ns', 'n', 'vn', 'v','nr'].
                    if the POS of w is not in this list,it will be filtered.
        - withFlag: only work with allowPOS is not empty.
                    if True, return a list of pair(word, weight) like posseg.cut
                    if False, return a list of words
    """
    if allowPOS:
        allowPOS = frozenset(allowPOS)
        words = psg.cut(sentence)
    else:
        words = jieba.cut(sentence)
    freq = {}
    for w in words:
        if allowPOS:
            if w.flag not in allowPOS:
                continue
            elif not withFlag:
                w = w.word
        wc = w.word if allowPOS and withFlag else w
        # if len(wc.strip()) < 2 or wc.lower() in self.stop_words:
        #     continue
        if len(wc.strip()) < 2:
            continue
        freq[w] = freq.get(w, 0.0) + 1.0
    total = sum(freq.values())
    for k in freq:
        kw = k.word if allowPOS and withFlag else k
        idf1 = idf_loader(r'F:\yjcloud-learn\NLP-learn\B_textranks\a_tf_idf_extract\idf1.txt')

        # 如果idf里没有词语，则用median_idf作为作为idf的取值
        idf_freq, median_idf = idf1.get_idf()
        freq[k] *= idf_freq.get(kw, median_idf) / total
    # todo
    # 不太懂
    print(freq)

    if withWeight:
        tags = sorted(freq.items(), key=itemgetter(1), reverse=True)
    else:
        tags = sorted(freq, key=freq.__getitem__, reverse=True)
    if topK:
        return tags[:topK]
    else:
        return tags


if __name__ == '__main__':
    text = "线程是程序执行时的最小单位，它是进程的一个执行流，\
            是CPU调度和分派的基本单位，一个进程可以由很多个线程组成，\
            线程间共享进程的所有资源，每个线程有自己的堆栈和局部变量。\
            线程由CPU独立调度执行，在多CPU环境下就允许多个线程同时运行。\
            同样多线程也可以实现并发操作，每个请求分配一个线程来处理。"

    # 基于TF-IDF算法进行关键词抽取
    keywords = extract_tags(text, topK=5, withWeight=True, allowPOS=['ns', 'n', 'vn', 'v', 'nr'])
    print(keywords)
