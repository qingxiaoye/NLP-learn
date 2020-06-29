# !/usr/bin/python
# -*- coding:utf-8 -*-
import networkx as nx

# 二，图的顶点
g = nx.Graph()  # 创建空的无向图
# g = nx.DiGraph()  # 创建空的有向图
# 1，向图中增加顶点
g.add_node(1)
g.add_nodes_from([2, 3, 4])
print(g.nodes(data=True))

# 2 增加其他属性
g.add_node(1, name='n1', weight=1)
# data为true，那么返回的是NodeDataView对象，该对象不仅包含每个顶点的ID属性，还包括顶点的其他属性
print(g.nodes(data=True))

# 3，删除顶点
g.remove_node(1)
print(g.nodes(data=True))

# 4，更新顶点
g._node[2].update({'name': 'n1 new'})
g._node[3]['name'] = 'n1 new'
print(g.nodes(data=True))

# 5，删除顶点的属性
del g.nodes[2]['name']

# 6，检查是否存在顶点
print(g.has_node(1))

# 三，图的边
# 1，向图中增加边 边是由对应顶点的名称构成的
# 一个边
g.add_edge(2, 3)
# 多个边
g.add_edges_from([(1, 2), (1, 3)])
print(g.edges())  # EdgeView([(1, 2), (1, 3), (2, 3)])
# 前两个字段是顶点的ID属性，用于标识一个边，第三个字段是边的权重
g.add_edge(1, 2, weight=4.7, relationship='renew')
g.add_weighted_edges_from([[1, 2, 0.125], (1, 3, 0.75), (2, 4, 1.2), (3, 4, 0.375)])
# 为边增加属性
g.add_edges_from([(1, 2, {'color': 'blue'}), (2, 3, {'weight': 8})])
print(g.edges(data=True))

# 2，查看边的属性
# 查看特定的边的信息有两种方式：
print(g[1][2])
print(g.get_edge_data(1, 2))

# 3，删除边
# g.remove_edge(2, 3)
# g.remove_edges_from([(1, 2), (1, 3)])
print(g.edges(data=True))
# 4，更新边的属性
g[2][4]['weight'] = 4.7
g.edges[2, 4]['weight'] = 4

g[3][4].update({"weight": 4.7})
g.edges[2, 4].update({"weight": 4.7})
print(g.edges(data=True))
# 5，删除边的属性
del g[3][4]['weight']

# 6，检查边是否存在
print(g.has_edge(1, 2))

# 四，图的属性
# 图的属性主要是指相邻数据，节点和边。

# 1，adj
# ajd返回的是一个AdjacencyView视图，该视图是顶点的相邻的顶点和顶点的属性，
print(g.adj[2][4])
# {'weight': 0.125, 'relationship': 'renew', 'color': 'blue'}
print(g.adj[1])
# AtlasView({2: {'weight': 0.125, 'relationship': 'renew', 'color': 'blue'}, 3: {'weight': 0.75}})


# 4，degree

# 对于无向图，顶点的度是指跟顶点相连的边的数量；对于有向图，顶点的图分为入度和出度，朝向顶点的边称作入度；背向顶点的边称作出度。
print(g.edges())
print(g.degree)

# 五，图的遍历
# 图的遍历是指按照图中各顶点之间的边，从图中的任一顶点出发，对图中的所有顶点访问一次且只访问一次。
# 图的遍历按照优先顺序的不同，通常分为深度优先搜索（DFS）和广度优先搜索（BFS）两种方式。

# 1，查看顶点的相邻顶点
# 查看顶点的相邻顶点，有多种方式，例如，以下代码都用于返回顶点1的相邻顶点，g[n]
# 表示图g中，与顶点n相邻的所有顶点：
# g[n]
# g.adj[n]
# g.neighbors(n)
# 其中，g.neighbors(n)
# 是g.adj[n]
# 的迭代器版本。
#
# 2，查看图的相邻
#
# 该函数返回顶点n和相邻的节点信息：
#
# >> > for n, nbrs in g.adjacency():
#     ...
#     print(n)
# ...
# print(nbrs)
# 3，图的遍历
#
# 深度优先遍历的算法：
#
# 首先以一个未被访问过的顶点作为起始顶点，沿当前顶点的边走到未访问过的相邻顶点；
# 当当前顶点没有未访问过的相邻顶点时，则回到上一个顶点，继续试探别的相邻顶点，直到所有的顶点都被访问过。
# 深度优先遍历算法的思想是：从一个顶点出发，一条路走到底；如果此路走不通，就返回上一个顶点，继续走其他路。
#
# 广度优先遍历的算法：
#
# 从顶点v出发，依次访问v的各个未访问过的相邻顶点；
# 分别从这些相邻顶点出发依次访问它们的相邻顶点；
# 广度优先遍历算法的思想是：以v为起点，按照路径的长度，由近至远，依次访问和v有路径相通且路径长度为1, 2...，n的顶点。
#
# 在进行图遍历时，需要访问顶点的相邻顶点，这需要用到adjacency()
# 函数，例如，g是一个无向图，n是顶点，nbrs是顶点n的相邻顶点，是一个字典结构
#
# for n, nbrs in g.adjacency():
#     print(n, nbrs)
#     for nbr, attr in nbrs.items():
#         # nbr表示跟n连接的顶点，attr表示这两个点连边的属性集合
#         print(nbr, attr）

# 六，绘制Graph
# 使用networkx模块draw()函数构造graph，使用matplotlib把图显示出来：


from matplotlib import pyplot as plt
import networkx as nx

g = nx.Graph()
# g.add_nodes_from([1,2,3])
g.add_edges_from([(1, 2, {'color': 'blue'}), (1, 3), (1, 5)])
nx.draw_networkx(g)
plt.show()

# 七，计算每个顶点的PageRank值
# 每个顶点的PageRank（简称PR）值，是访问顶点的概率，可以通过networkx.pagerank()函数来计算，
# 该函数根据顶点的入边和边的权重来计算顶点的PR值，
# 也就是说，PR值跟顶点的入边有关，跟入边的weight（权重）属性有关：

# pagerank(g, alpha=0.85, personalization=None, max_iter=100, tol=1e-06, nstart=None, weight='weight', dangling=None)

# g：无向图会被转换为有向图，一条无向边转换为两条有向边；
# alpha：阻尼参数，默认值是0.85，取值范围为 0 到 1, 代表从图中某一特定点指向其他任意点的概率；
# weight：默认值是weight，表示使用edge的weight属性作为权重，如果没有指定，那么把edge的权重设置为1；

# 例如，创建一个有向图，由三个顶点（A、B和C），两条边（A指向B，A指向C），边的权重都是0.5

g = nx.DiGraph()
g.add_weighted_edges_from([('A', 'B', 0.5), ('A', 'C', 0.5)])
print(nx.pagerank(g))
# {'A': 0.259740259292235, 'C': 0.3701298703538825, 'B': 0.3701298703538825}
# 修改边的权重，并查看顶点的PR值：

g['A']['C']['weight'] = 1
print(nx.pagerank(g))
# {'A': 0.259740259292235, 'C': 0.40692640737443164, 'B': 0.3333333333333333}
# 2，查看各个顶点的PR值

# 根据图来创建PageRank，并查看各个顶点的PageRank值

pr = nx.pagerank(g)
# page_rank_value=pr[node]
for node, pageRankValue in pr.items():
    print("%s,%.4f" % (node, pageRankValue))
