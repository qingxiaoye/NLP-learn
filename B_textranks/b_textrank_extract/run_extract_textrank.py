# !/usr/bin/python
# -*- coding:utf-8 -*-

import sys
from operator import itemgetter
from collections import defaultdict
import jieba.posseg

text_type = str
string_types = (str,)
xrange = range

iterkeys = lambda d: iter(d.keys())
itervalues = lambda d: iter(d.values())
iteritems = lambda d: iter(d.items())
class UndirectWeightedGraph:
    d = 0.85

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, start, end, weight):
        # use a tuple (start, end, weight) instead of a Edge object
        self.graph[start].append((start, end, weight))
        self.graph[end].append((end, start, weight))

    def rank(self):
        ws = defaultdict(float)
        outSum = defaultdict(float)

        wsdef = 1.0 / (len(self.graph) or 1.0)
        for n, out in self.graph.items():
            ws[n] = wsdef
            outSum[n] = sum((e[2] for e in out), 0.0)

        # this line for build stable iteration
        sorted_keys = sorted(self.graph.keys())
        for x in xrange(10):  # 10 iters
            for n in sorted_keys:
                s = 0
                for e in self.graph[n]:
                    s += e[2] / outSum[e[1]] * ws[e[1]]
                ws[n] = (1 - self.d) + self.d * s

        (min_rank, max_rank) = (sys.float_info[0], sys.float_info[3])

        for w in itervalues(ws):
            if w < min_rank:
                min_rank = w
            if w > max_rank:
                max_rank = w

        for n, w in ws.items():
            # to unify the weights, don't *100.
            ws[n] = (w - min_rank / 10.0) / (max_rank - min_rank / 10.0)

        return ws


def textrank(self, sentence, topK=20, withWeight=False, allowPOS=('ns', 'n', 'vn', 'v'), withFlag=False):
    """
    Extract keywords from sentence using TextRank algorithm.
    Parameter:
        - topK: return how many top keywords. `None` for all possible words.
        - withWeight: if True, return a list of (word, weight);
                      if False, return a list of words.
        - allowPOS: the allowed POS list eg. ['ns', 'n', 'vn', 'v'].
                    if the POS of w is not in this list, it will be filtered.
        - withFlag: if True, return a list of pair(word, weight) like posseg.cut
                    if False, return a list of words
    """
    self.pos_filt = frozenset(allowPOS)
    g = UndirectWeightedGraph()
    cm = defaultdict(int)
    words = tuple(self.tokenizer.cut(sentence))
    for i, wp in enumerate(words):
        if self.pairfilter(wp):
            for j in xrange(i + 1, i + self.span):
                if j >= len(words):
                    break
                if not self.pairfilter(words[j]):
                    continue
                if allowPOS and withFlag:
                    cm[(wp, words[j])] += 1
                else:
                    cm[(wp.word, words[j].word)] += 1

    for terms, w in cm.items():
        g.addEdge(terms[0], terms[1], w)
    nodes_rank = g.rank()
    if withWeight:
        tags = sorted(nodes_rank.items(), key=itemgetter(1), reverse=True)
    else:
        tags = sorted(nodes_rank, key=nodes_rank.__getitem__, reverse=True)

    if topK:
        return tags[:topK]
    else:
        return tags
if __name__ == '__main__':

    sentence = '全国港澳研究会会长徐泽在会上发言指出，学习系列重要讲话要深刻领会 主席关于香港回归后的宪制基础和宪制秩序的论述，这是过去20年特别是中共十八大以来"一国两制"在香港实践取得成功的根本经验。首先，要在夯实 香港的宪制基础、巩固香港的宪制秩序上着力。只有牢牢确立起"一国两制"的宪制秩序，才能保证"一国两制"实践不走样 、不变形。其次，要在完善基本法实施的制度和机制上用功。中央直接行使的权力和特区高度自治权的结合是特区宪制秩 序不可或缺的两个方面，同时必须切实建立以行政长官为核心的行政主导体制。第三，要切实加强香港社会特别是针对公 职人员和青少年的宪法、基本法宣传，牢固树立"一国"意识，坚守"一国"原则。第四，要努力在全社会形成聚焦发展、抵 制泛政治化的氛围和势能，全面准确理解和落实基本法有关经济事务的规定，使香港继续在国家发展中发挥独特作用并由 此让最广大民众获得更实在的利益。'

    keywords =  textrank(sentence, topK=20, withWeight=True, allowPOS=('n', 'nr', 'ns'))

    # print(type(keywords))
    # <class 'list'>

    for item in keywords:
        print(item[0], item[1])
