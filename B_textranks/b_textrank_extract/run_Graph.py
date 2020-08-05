# !/usr/bin/python
# -*- coding:utf-8 -*-
import sys
from collections import defaultdict

xrange = range
iterkeys = lambda d: iter(d.keys())
itervalues = lambda d: iter(d.values())
iteritems = lambda d: iter(d.items())


class UndirectWeightedGraph:
    d = 0.85

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, start, end, weight):
        # 共现的次数作为边的权重
        # use a tuple (start, end, weight) instead of a Edge object
        self.graph[start].append((start, end, weight))
        self.graph[end].append((end, start, weight))

    def rank(self):
        ws = defaultdict(float)
        outSum = defaultdict(float)
        # 初始权重
        wsdef = 1.0 / (len(self.graph) or 1.0)
        for n, out in self.graph.items():
            ws[n] = wsdef
            outSum[n] = sum((e[2] for e in out), 0.0)

        # this line for build stable iteration
        sorted_keys = sorted(self.graph.keys())
        # 为什么是10次迭代
        for x in xrange(10):  # 10 iters
            for n in sorted_keys:
                s = 0
                for e in self.graph[n]:
                    s += e[2] / outSum[e[1]] * ws[e[1]]
                ws[n] = (1 - self.d) + self.d * s
        print(ws)
        (min_rank, max_rank) = (sys.float_info[0], sys.float_info[3])
        # 找最大最小值
        for w in itervalues(ws):
            if w < min_rank:
                min_rank = w
            if w > max_rank:
                max_rank = w
        print(ws)

        for n, w in ws.items():
            # to unify the weights, don't *100.
            ws[n] = (w - min_rank / 10.0) / (max_rank - min_rank / 10.0)
        print(ws)
        return ws


if __name__ == '__main__':
    cm = {('全国', '研究会'): 2, ('全国', '会长'): 2, ('全国', '徐泽'): 2, ('研究会', '会长'): 2, ('研究会', '徐泽'): 2, ('会长', '徐泽'): 2}
    g = UndirectWeightedGraph()
    for terms, w in cm.items():
        g.addEdge(terms[0], terms[1], w)
    nodes_rank = g.rank()
