import networkx as nx
import matplotlib.pyplot as plt

G = nx.path_graph(50)
G.add_edges_from([(0, 25)])
centrality = nx.eigenvector_centrality_numpy(G)
for n in centrality:
 print ("c(", n, ")=", f"{centrality[n]:.8f}")

nx.draw(G, with_labels = True)
plt.show()  # Добавлено для отображения графика
