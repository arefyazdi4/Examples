import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, data, next_data=None, prev_data=None):
        self.data = data
        self.next = next_data
        self.prev = prev_data


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, data):
        new_dode = Node(data)
        if self.head:
            new_dode.prev = self.tail
            self.tail.next = new_dode
            self.tail = new_dode
        else:
            self.head = new_dode
            self.tail = new_dode
        self.size += 1

    def dequeue(self):
        if self.head:
            data = self.head.data
            if self.head.next:
                self.head = self.head.next
                self.head.prev = Node
            else:
                self.head = None
                self.tail = None
            self.size -= 1
            return data
        else:
            return None

    def next(self):
        node = self.head
        self.dequeue()
        self.enqueue(node.data)
        return node.data

    def __iter__(self):
        current = self.head
        for i in range(self.size):
            yield current.data
            current = current.next

    def __getitem__(self, item):
        current = self.head
        for _ in range(item):
            current = current.next
        return current.data

    def __len__(self):
        return self.size


class NodeBfs:
    def __init__(self, node_num, distance=None, predecessor=None, color='white'):
        self.node_num = node_num
        self.distance = distance
        self.predecessor: NodeBfs = predecessor
        self.color = color
        self.adj: list[NodeBfs] = list()


class GraphBfsDatabase:
    def __init__(self, raw_graph):
        self.raw_graph = raw_graph
        self.graph_list_bfs: list[NodeBfs] = list()
        self.set_graph_list()

    def set_graph_list(self):
        list_adjacency: list = self.raw_graph.list_adjacency
        for node in list_adjacency:
            new_node = NodeBfs(node[0])
            self.graph_list_bfs.append(new_node)

        for node in self.graph_list_bfs:
            node_edges = list_adjacency[node.node_num - 1][1]
            for connected_node in node_edges:
                node.adj.append(self[connected_node])

    def find_max_connected_node(self):
        max_connected_node = self.graph_list_bfs[0]
        for node in self.graph_list_bfs:
            if node.adj.__len__() > max_connected_node.adj.__len__():
                max_connected_node = node
        return max_connected_node

    def __getitem__(self, item):
        for node in self.graph_list_bfs:
            if node.node_num == item:
                return node
        return None

    @staticmethod
    def get_path(end_node: NodeBfs):
        path = list()
        current_node = end_node
        while current_node:
            path.append(current_node.node_num)
            current_node = current_node.predecessor
        path.reverse()
        return path


class GraphDirected:
    def __init__(self, edge_list_raw: list):
        self.edge_list_raw = edge_list_raw
        self.vertices = set()
        self.set_vertices()
        self.node_number = self.vertices.__len__()
        self.edge_number = self.edge_list_raw.__len__()
        self.list_adjacency = list()
        self.set_list_adjacency()
        self.matrix_adjacency = list()
        self.set_matrix_adjacency_user_interface()
        self.user_interface_graph = nx.DiGraph()  # using network
        self.set_user_interface_graph()

    def set_vertices(self):
        for edges in self.edge_list_raw:
            for node in edges:
                self.vertices.add(node)

    def set_list_adjacency(self):
        for node in self.vertices:
            connected_nodes = [ver[1] for ver in list(filter(lambda v: v[0] == node, self.edge_list_raw))]
            self.list_adjacency.append((node, connected_nodes))

    def set_user_interface_graph(self):
        for node in self.vertices:
            self.user_interface_graph.add_node(node)
        for s_node, e_node, weight in self.edge_list_raw:
            self.user_interface_graph.add_edge(s_node, e_node)

    def show_user_interface_graph(self):
        # pos = nx.spring_layout(self.user_interface_graph, seed=3113794652)  # positions for all nodes
        nx.draw(self.user_interface_graph, with_labels=True, font_weight='bold')
        # nx.draw_networkx_edges(
        #     self.user_interface_graph,
        #     pos,
        #     edgelist=[(10, 11), (10, 2)],
        #     width=8,
        #     alpha=0.5,
        #     edge_color="tab:red",
        # )
        plt.show()

    def set_matrix_adjacency_user_interface(self):
        self.matrix_adjacency = [[0 for j in range(self.node_number)] for i in range(self.node_number)]
        for edges in self.edge_list_raw:
            start_node = edges[0] - 1
            end_node = edges[1] - 1
            self.matrix_adjacency[start_node][end_node] = 1

    def show_matrix_adjacency(self):
        plt.ion()
        plt.imshow(self.matrix_adjacency, interpolation='none', origin='lower')
        plt.show()

    def bts(self, start_node, end_node):
        graph_db = GraphBfsDatabase(self)

        start_node: NodeBfs = graph_db[start_node]
        end_node: NodeBfs = graph_db[end_node]

        start_node.color = 'gray'
        start_node.distance = 0

        travel_node_queue = Queue()
        travel_node_queue.enqueue(start_node)

        while len(travel_node_queue):
            if end_node.predecessor:
                break
            parent_node: NodeBfs = travel_node_queue.dequeue()
            for current_node in parent_node.adj:
                if current_node.color == 'white':
                    current_node.color = 'gray'
                    current_node.distance = parent_node.distance + 1
                    current_node.predecessor = parent_node
                    travel_node_queue.enqueue(current_node)
            parent_node.color = 'black'
        return graph_db

    def show_bts_user_interface(self):


def read_edges_file(file_name):
    edge_file_name = open(file_name, 'r')
    edges_list = list()
    for data in edge_file_name:
        node_num = data.split()
        edges_list.append(tuple(map(int, data.split())))  # index 0 & index 1 -> tuple edge from node1 to node2
    return edges_list


if __name__ == '__main__':
    print('*****demo Graph******')
    edges_list_raw = read_edges_file('edges_list.txt')
    print(edges_list_raw)
    demo_graph_directed = GraphDirected(edges_list_raw)

    print('***** UI graph *****')
    demo_graph_directed.show_user_interface_graph()

    print('**** vertices *****')
    print(demo_graph_directed.vertices)

    print('**** node num *****')
    print(demo_graph_directed.node_number)

    print('**** edge num *****')
    print(demo_graph_directed.edge_number)

    print('**** list adj ****')
    for vertices in demo_graph_directed.list_adjacency:
        print(vertices)

    print('**** matrix adj ****')
    for vertices in demo_graph_directed.matrix_adjacency:
        print(vertices)
    demo_graph_directed.show_matrix_adjacency()

    print('**** Bfs ****')
    demo_graph_bfs_db = demo_graph_directed.bts(6, 10)
    print(6, demo_graph_bfs_db[6].distance)
    print(2, demo_graph_bfs_db[2].distance)
    print(7, demo_graph_bfs_db[7].distance)
    print(8, demo_graph_bfs_db[8].distance)
    print(9, demo_graph_bfs_db[9].distance)
    print(10, demo_graph_bfs_db[10].distance)

    print('***path***')
    print(9, GraphBfsDatabase.get_path(demo_graph_bfs_db[9]))
    print(10, GraphBfsDatabase.get_path(demo_graph_bfs_db[10]))
