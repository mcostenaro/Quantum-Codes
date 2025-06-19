import rustworkx as rx
from rustworkx.visualization import mpl_draw as draw_graph
import numpy as np
import matplotlib.pyplot as plt


#gerando o grafo
n = 5
 
g = rx.PyGraph()
g.add_nodes_from(np.arange(0, n, 1))
edge_list = [(0, 1, 1.0), (0, 2, 1.0), (0, 4, 1.0), (1, 2, 1.0), (2, 3, 1.0), (3, 4, 1.0)]
g.add_edges_from(edge_list)
draw_graph(g, node_size=600, with_labels=True)
plt.show()


