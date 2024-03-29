# -*- coding: utf-8 -*-
"""network visualization

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IoL8Tfg3L5d31wc_dUcOK3vKmj-nv9FN
"""

pip install networkx

import networkx as nx
import matplotlib.pyplot as plt

G= nx.Graph()

G.add_nodes_from([1,2,3,4,5])

G.add_edges_from([(1,2),(1,3),(2,3),(3,4),(5,1)])

pos=nx.spring_layout(G)
nx.draw(G,pos,with_labels=True,node_color='skyblue',node_size=1400,edge_color='black',linewidths=1,font_size=15)
plt.show()