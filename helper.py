
from builtins import range
from graphillion import GraphSet
from random import seed, shuffle

def grid(m, n=None, prob_to_remove_edge=0.0):
    import networkx as nx
    # critical edge probability is 0.5 in the percolation theory
    assert 0 <= prob_to_remove_edge and prob_to_remove_edge < 0.4
    seed(1)
    m += 1
    if n is None:
        n = m
    else:
        n += 1
    edges = []
    for v in range(1, m * n + 1):
        if v % n != 0:
            edges.append((v, v + 1))
        if v <= (m - 1) * n:
            edges.append((v, v + n))
    g = nx.Graph(edges)
    while prob_to_remove_edge > 0:
        g = nx.Graph(edges)
        edges_removed = edges[:]
        shuffle(edges_removed)
        g.remove_edges_from(edges_removed[:int(len(edges)*prob_to_remove_edge)])
        if nx.is_connected(g) and len(g[1]) == 2:
            break
    return g.edges()

def draw(g, options={}, universe=None):
    import networkx as nx
    import matplotlib.pyplot as plt
    if not isinstance(g, nx.Graph):
        g = nx.Graph(list(g))
    if universe is None:
        universe = GraphSet.universe()
    if not isinstance(universe, nx.Graph):
        universe = nx.Graph(list(universe))
    n = sorted(universe[1].keys())[1] - 1
    m = universe.number_of_nodes() // n
    g.add_nodes_from(universe.nodes())
    pos = {}
    for v in range(1, m * n + 1):
        pos[v] = ((v - 1) % n, (m * n - v) // n)


    if len(options) == 0:
        options = {
            "edgecolors": "#333",
            "node_size": 2000,
            "node_color": "#FC5647",
            "linewidths": 2,
            "width": 2,
            "edge_color": "#333",
            "font_color": "white",
            "font_size": "14",
            "with_labels": True
        }

    nx.draw(g, pos, **options)
    # plt.show()

def how_many_turns(path):
    path = set(path)
    turns = 0
    pos = 1
    direction = 1
    while (True):
        edges = [e for e in path if e[0] == pos or e[1] == pos]
        if not edges: break
        edge = edges[0]
        path -= set([edge])
        next_direction = abs(edge[1] - edge[0])
        if direction != next_direction:
            turns +=1
        pos = edge[1] if edge[0] == pos else edge[0]
        direction = next_direction
    return turns

def hist(data):
    import matplotlib.pyplot as plt
    plt.hist(data)
    plt.show()
