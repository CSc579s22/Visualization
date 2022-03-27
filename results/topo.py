import networkx as nx
from matplotlib import pyplot as plt

G = nx.Graph()
G.add_edge("server", "sw_origin")
G.add_edge("sw_origin", "sw1")
G.add_edge("sw_origin", "sw2")
G.add_edge("sw1", "cache1", weight=1)
G.add_edge("sw2", "cache2", weight=10)
for i in range(4):
    G.add_edge("sw1", "sw1c{}".format(i + 1), weight=(i + 1) * 2 / 10)
for i in range(2):
    G.add_edge("sw2", "sw2c{}".format(i + 1), weight=1)

fixed_positions = {"server": (0, 0), "sw_origin": (0, -1), "sw1": (-2, -1.5), "sw2": (2, -1.5),
                   "cache1": (-0.5, -1.5), "cache2": (0.5, -1.5)}
fixed_nodes = fixed_positions.keys()
pos = nx.spring_layout(G, pos=fixed_positions, fixed=fixed_nodes, seed=2)
nx.draw_networkx(G, pos)
labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.savefig("topo.png")
plt.show()

