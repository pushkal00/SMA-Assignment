#!/usr/bin/env python
# coding: utf-8

# In[1]:


import networkx as nx
from networkx.algorithms.community.modularity_max import greedy_modularity_communities
import matplotlib.pyplot as plt
import time


# In[2]:


def modularity_clustering(G):
    def plot_clusters(clusters):
        val_map = {}
        idx = 0
        for cluster in clusters:
            for node in cluster:
                val_map[node] = idx
            idx += 1
        values = [val_map.get(node) for node in G.nodes()]
        nx.draw(G, cmap=plt.get_cmap('viridis'), node_color=values, with_labels=True, font_color='white')
        plt.show()

    old = time.time()
    communities = tuple(greedy_modularity_communities(G))
    new = time.time()
    print("running time:", new-old)
    print("num clusters:", len(communities))
    print("Modularity: " + str(nx.algorithms.community.modularity(G, communities)))
    plot_clusters(communities)
    return communities


# In[3]:


dolphins_graph = nx.read_gml("dolphins.gml")
clusters = modularity_clustering(dolphins_graph)
for cluster in clusters:
    print(cluster)


# In[8]:


karate_graph = nx.read_gml("karate.gml", label="id")
clusters = modularity_clustering(karate_graph)
for cluster in clusters:
    print(cluster)


# In[5]:


jazz_graph = nx.read_gml("jazz.gml")
clusters = modularity_clustering(jazz_graph)
for cluster in clusters:
    print(cluster)

