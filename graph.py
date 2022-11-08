
import networkx as nx
import matplotlib.pyplot as plt

G = nx.grid_2d_graph(5, 5)

print(G.nodes())
pos = {(x,y):(y,-x) for x,y in G.nodes()}

options = {
    'font_size': 11,
    'font_color': '#fff'
}

nx.draw(G, node_size=2000, node_color='#212a35', pos=pos, with_labels=True, **options)
plt.show()
