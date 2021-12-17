#!/usr/bin/env python
# coding: utf-8

# In[1]:


import networkx as nx
import matplotlib.pyplot as plt
import time


# In[2]:


def betweenness_clustering(G, K):
    """
    Computes K clusters in G using girvan newman method
    """
    def edges_to_remove(G):
        centralities = nx.edge_betweenness_centrality(G)
        max_centrality = max(centralities.values())
        edges = [edge for edge in centralities if centralities[edge] == max_centrality]
        return edges
    
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
    
    g = G.copy()
    old = time.time()
    connected_components = list(nx.connected_components(g))
    num_connected_components = len(connected_components)
    while (num_connected_components < K):
        edges = edges_to_remove(g)
        for edge in edges:
            g.remove_edge(edge[0], edge[1])
        connected_components = list(nx.connected_components(g))
        num_connected_components = len(connected_components)
    new = time.time()
    print("time taken:", (new - old))
    modularity = nx.algorithms.community.quality.modularity(G, connected_components)
    print("modularity score:", modularity)
    plot_clusters(connected_components)
    return connected_components
        


# In[3]:


dolphins_graph = nx.read_gml("dolphins.gml")
k = 4
clusters = betweenness_clustering(dolphins_graph, k)
for cluster in clusters:
    print(cluster)


# In[4]:


karate_graph = nx.read_gml("karate.gml", label="id")
k = 2
clusters = betweenness_clustering(karate_graph, k)
for cluster in clusters:
    print(cluster)


# In[5]:


jazz_graph = nx.read_gml("jazz.gml")
k = 4
clusters = betweenness_clustering(jazz_graph, k)
for cluster in clusters:
    print(cluster)


# In[ ]:




