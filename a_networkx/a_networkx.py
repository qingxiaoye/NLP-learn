# !/usr/bin/python
# -*- coding:utf-8 -*-
import networkx as nx

g=nx.Graph()#创建空的无向图
g=nx.DiGraph()#创建空的有向图
g.add_node(1)
g.add_nodes_from([2,3,4])
print(g.nodes())