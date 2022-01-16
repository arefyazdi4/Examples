class Graphs:
    def __init__(self, edge_list_raw: list):
        self.edge_list_raw = edge_list_raw
        self.vertices = set()
        self.set_vertices()
        self.node_number = self.vertices.__len__()
        self.edge_number = self.edge_list_raw.__len__()
        self.list_adjacency = dict()
        self.set_list_adjacency()
        self.matrix_adjacency = list()
        self.set_matrix_adjacency()
        self.color = {node: 'white' for node in self.vertices}
        self.distance = {node: None for node in self.vertices}
        self.predecessor = {node: None for node in self.vertices}

    def set_vertices(self):
        for edges in self.edge_list_raw:
            for node in edges:
                self.vertices.add(node)

    def set_list_adjacency(self):
        for node in self.vertices:
            connected_nodes = [ver[1] for ver in list(filter(lambda v: v[0] == node, self.edge_list_raw))]
            self.list_adjacency[node] = connected_nodes

    def set_matrix_adjacency(self):
        self.matrix_adjacency = [[0 for j in range(self.node_number)] for i in range(self.node_number)]
        for edges in self.edge_list_raw:
            start_node = edges[0] - 1
            end_node = edges[1] - 1
            self.matrix_adjacency[start_node][end_node] = 1

    def bts(self, start_node):

        self.color[start_node] = 'gray'
        self.distance[start_node] = 0

        travel_node_queue = list()
        travel_node_queue.append(start_node)

        while len(travel_node_queue):
            parent_nodes = travel_node_queue.pop(0)
            for current_node in self.list_adjacency[parent_nodes]:
                if self.color[current_node] == 'white':
                    self.color[current_node] = 'gray'
                    self.distance[current_node] = self.distance[parent_nodes] + 1
                    self.predecessor[current_node] = parent_nodes
                    travel_node_queue.append(current_node)
            self.color[parent_nodes] = 'black'

    def path(self, end_point):
        node = end_point
        while node:
            print(node)
            node = self.predecessor[node]


def read_edges_file(file_name):
    edge_file_name = open(file_name, 'r')
    edges_list = list()
    for data in edge_file_name:
        node_num = data.split()
        edges_list.append((int(node_num[0]), int(node_num[1])))  # index 0 & index 1 -> tuple edge from node1 to node2
    return edges_list


if __name__ == '__main__':
    print('*****first Graph')
    edges_list_raw = read_edges_file('edge_list_demo.txt')
    first_graph = Graphs(edges_list_raw)

    print('**** vertices *****')
    print(first_graph.vertices)

    print('**** node num *****')
    print(first_graph.node_number)

    print('**** edge num *****')
    print(first_graph.edge_number)

    print('**** list adj ****')
    print(first_graph.list_adjacency)

    print('**** matrix adj ****')
    for vertices in first_graph.matrix_adjacency:
        print(vertices)

    print('**** Bfs ****')
    first_graph.bts(6)
    print(first_graph.distance[6])
    print(first_graph.distance[9])
    print(first_graph.distance[10])
    print(first_graph.distance[3])

    print('path')
    first_graph.path(9)
