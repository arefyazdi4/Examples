class Graphs:
    def __init__(self, edge_list_raw: list):
        self.edge_list_raw = edge_list_raw
        self.vertices = set()
        self.set_vertices()
        self.node_number = self.vertices.__len__()
        self.edge_number = self.edge_list_raw.__len__()
        self.list_adjacency = list()
        self.set_list_adjacency()
        self.matrix_adjacency = list()
        self.set_matrix_adjacency()

    def set_vertices(self):
        for edges in self.edge_list_raw:
            for node in edges:
                self.vertices.add(node)

    def set_list_adjacency(self):
        for node in self.vertices:
            connected_nodes = [ver[1] for ver in list(filter(lambda v: v[0] == node, self.edge_list_raw))]
            self.list_adjacency.append((node, connected_nodes))

    def set_matrix_adjacency(self):
        self.matrix_adjacency = [[0 for j in range(self.node_number)] for i in range(self.node_number)]
        for edges in self.edge_list_raw:
            start_node = edges[0] - 1
            end_node = edges[1] - 1
            self.matrix_adjacency[start_node][end_node] = 1


def read_edges_file(file_name):
    edge_file_name = open(file_name, 'r')
    edges_list = list()
    for data in edge_file_name:
        node_num = data.split()
        edges_list.append((int(node_num[0]), int(node_num[1])))  # index 0 & index 1 -> tuple edge from node1 to node2
    return edges_list


if __name__ == '__main__':
    print('*****first Graph')
    edges_list_raw = read_edges_file('edges_list.txt')
    first_graph = Graphs(edges_list_raw)

    # print('**** vertic *****')
    # print(first_graph.vertices)
    # print('**** node num *****')
    # print(first_graph.node_number)
    # print('**** edge num *****')
    # print(first_graph.edge_number)
    # print('**** list adj ****')
    # print(first_graph.list_adjacency)
    print('**** matrix adj ****')
    print(first_graph.matrix_adjacency)
