
from graphillion import GraphSet
import networkx as nx
import matplotlib.pyplot as plt
import sys

class BipartiteGraph:

    def __init__(self, m, n):
        """
        Initialize the object.
        """

        self.m = m
        self.n = n
        self.m_nodes = []
        self.n_nodes = []
        self.num_nodes = m + n
        self.num_edges = m * n

        self.init()

    def init(self):
        """
        Initialize the variables.
        """

        for node_id in range(1, self.get_num_nodes() + 1):

            if node_id <= self.m:
                self.m_nodes.append(node_id)
            else:
                self.n_nodes.append(node_id)


    def get_num_nodes(self):
        """
        Returns the total number of nodes in the graph.
        """

        return self.num_nodes

    def get_num_edges(self):
        """
        Returns the total number of edges in the graph.
        """

        return self.num_edges

    def get_edges(self):

        edges = []

        for i in range(self.m):
            for j in range(self.n):
                edges.append((self.m_nodes[i], self.n_nodes[j]))

        return edges

    def get_nodes(self):

        return self.m_nodes + self.n_nodes

    def generate_graph(self):
        """
        Generates the NetworkX graph.
        """

        graph = nx.Graph()
        graph.add_nodes_from(self.m_nodes, bipartite=0)
        graph.add_nodes_from(self.n_nodes, bipartite=1)

        edges = self.get_edges()

        graph.add_edges_from(edges)

        return graph

    def get_graph(self):

        return self.generate_graph()

    def plot(self, options={}):

        graph = self.get_graph()

        l, r = nx.bipartite.sets(graph)

        pos = {}

        pos.update((node, (1, index)) for index, node in enumerate(l))
        pos.update((node, (2, index)) for index, node in enumerate(r))

        if len(options) == 0:

            options = {
                "edgecolors": "#333",
                "node_size": 1500,
                "node_color": "#FC5647",
                "linewidths": 2,
                "width": 2,
                "edge_color": "#333",
                "font_color": "white",
                "font_size": "14"
            }

        nx.draw(graph, pos=pos, with_labels=True, **options)
        # plt.show()

    def get_paths(self, s, t, edges, is_hamilton=True):

        GraphSet.set_universe(edges)

        return GraphSet.paths(s, t, is_hamilton=is_hamilton)

    def count_hamiltonian_paths(self, s, t, edges):
        """
        Counts the No. of hamitonian paths from s to t.
        """

        return len(self.get_paths(s, t, edges))

    def count_hamiltonian_paths_with_edge_removed(self, s, t, edge, edges):
        """
        Counts the Hamiltonian paths with an edge removed in the graph.
        """

        edges = list(edges)
        edges.remove(edge)

        return self.count_hamiltonian_paths(s, t, edges)

def get_name(num):

    return 'bipartite-' + str(num) + '.png'

if __name__ == '__main__':


    arguments = sys.argv

    if len(arguments) == 1:

        print('Please provide the bipartite size.')
        print('For Example:')
        print('    python bipartite_graph.py 5')
        exit(0)

    num = 4
    try:
        num = int(arguments[1])
    except:
        print('Please provide the bipartite graph size as an integer.')
        exit(0)

    bg = BipartiteGraph(num, num)

    edges = bg.get_edges()

    start = 1
    end = (bg.get_num_nodes() // 2) + 1

    # print(start, end)
    # print(bg.count_hamiltonian_paths(start, end, edges))
    # print(bg.count_hamiltonian_paths_with_edge_removed(start, end, (start, end), edges))
    # print(bg.count_hamiltonian_paths_with_edge_removed(start, end, (start, end + 1), edges))

    fname = get_name(num)

    print('=======================')
    print('Bipartite Graph: %d x %d' % (num, num))
    print('=======================')
    print('The number of hamitonian paths from', start, ' to', end, ' are:', bg.count_hamiltonian_paths(start, end, edges))
    print('The number of hamitonian paths from', start, ' to', end, ' by removing start and end edge are:', bg.count_hamiltonian_paths_with_edge_removed(start, end, (start, end), edges))
    print('The number of hamitonian paths from', start, ' to', end, ' by removing', start, 'and ', end+1,' edge are:', bg.count_hamiltonian_paths_with_edge_removed(start, end, (start, end + 1), edges))
    print('Saving bipartite graph in', fname)

    bg.plot()
    plt.savefig(fname, format='png', dpi=600)
