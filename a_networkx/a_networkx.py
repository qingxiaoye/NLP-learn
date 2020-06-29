# !/usr/bin/python
# -*- coding:utf-8 -*-
import numpy
import networkx as nx

A = numpy.matrix([[1, 1], [2, 1]])
G = nx.from_numpy_matrix(A)
print(G.edges(data=True))

import numpy

dt = [('weight', float), ('cost', int)]
A = numpy.matrix([[(1.0, 2)]], dtype=dt)
print(A)
G = nx.from_numpy_matrix(A)
print(G.edges(data=True))
