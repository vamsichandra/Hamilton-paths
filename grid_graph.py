
from graphillion import GraphSet
import matplotlib.pyplot as plt
import networkx as nx
import helper as hl
# import graphillion.tutorial as hl
import sys

class GridGraph:

    def __init__(self, m):
        """
        Initialize the object.
        """

        self.m = m
        self.nodes = []
        self.edges = []
        self.G = None
        self.num_nodes = (m + 1) * (m + 1)
        self.num_edges = 2 * m * (m - 1)

        self.init()

    def init(self):
        """
        Initialize the variables.
        """

        self.G = nx.grid_2d_graph(self.m, self.m)

        self.nodes = list(self.G.nodes())
        self.edges = list(self.G.edges())

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

        return self.edges

    def get_nodes(self):

        return self.nodes

    def generate_graph(self):
        """
        Generates the NetworkX graph.
        """

        return self.G

    def get_graph(self):

        return self.generate_graph()

    def plot(self, options={}):

        graph = self.get_graph()

        pos = {(x, y):(y, -x) for x,y in graph.nodes()}

        if len(options) == 0:

            options = {
                "edgecolors": "#333",
                "node_size": 2000,
                "node_color": "#FC5647",
                "linewidths": 2,
                "width": 2,
                "edge_color": "#333",
                "font_color": "white",
                "font_size": "14"
            }

        nx.draw(graph, pos=pos, with_labels=True, **options)
        # plt.show()

    def plot_from_edges(g, options={}):

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
                "font_size": "14"
            }

        nx.draw(g, pos, **options)

    def get_paths(self, s, t, is_hamilton=True):

        universe = hl.grid(self.m, self.m)
        GraphSet.set_universe(universe)

        paths = GraphSet.paths(s, t, is_hamilton=is_hamilton)

        return paths

    def count_hamiltonian_paths(self, s, t):
        """
        Counts the No. of hamitonian paths from s to t.
        """

        return len(self.get_paths(s, t))

    def show_path(self, path):

        options = {
            "edgecolors": "#333",
            "node_size": 500,
            "node_color": "#FC5647",
            "linewidths": 2,
            "width": 2,
            "edge_color": "#333",
            "font_color": "white",
            "font_size": "9",
            "with_labels": True
        }

        hl.draw(path, options)

def get_name(num):

    return str(num) + 'x' + str(num) + '.png'

if __name__ == '__main__':

    arguments = sys.argv

    if len(arguments) == 1:

        print('Please provide the Grid size.')
        print('For Example:')
        print('    python grid_graph.py 5')
        exit(0)

    num = 4
    try:
        num = int(arguments[1])
    except:
        print('Please provide the grid size as an integer.')
        exit(0)

    gg = GridGraph(num)

    start = 1

    end = end = gg.get_num_nodes()

    if num % 2 == 1:
        end = gg.get_num_nodes() - 1

    paths = gg.get_paths(start, end)

    fname = get_name(num)

    print('=======================')
    print('Grid Graph: %d x %d' % (num, num))
    print('=======================')
    print('The number of hamitonian paths from', start, ' to', end, ' are:', len(paths))
    print('Drawing a path from', start, ' to', end, 'and saving in', fname)

    # Pass the random path.
    gg.show_path(paths.choice())

    plt.savefig(fname, format='png', dpi=600)
