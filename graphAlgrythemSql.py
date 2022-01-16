from collections import deque
import sqlite3


class ListQueue:
    def __init__(self):
        self.item = deque([])
        self.size = 0

    def enqueue(self, data):
        self.item.append(data)
        self.size += 1

    def dequeue(self):
        self.size -= 1
        return self.item.popleft()

    def __iter__(self):
        for data in self.item:
            yield data

    def __getitem__(self, item):
        return self.item.__getitem__(item)

    def __len__(self):
        return self.item.__len__()


# DataBase Functional class
class NodeDataBase:
    def __init__(self):
        self.conn = sqlite3.connect("NODE_DATABASE")
        self.cur = self.conn.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS nodes(
                            node_num INTEGER PRIMARY KEY ,
                            color MESSAGE_TEXT ,
                            distance INTEGER ,
                            parent INTEGER
                            )""")
        self.conn.commit()

    def insert_data(self, node, color='white', distance=0, parent=0):
        self.cur.execute("INSERT INTO nodes VALUES (?, ?, ?, ?)", (node, color, distance, parent))
        self.conn.commit()

    def update_data(self, node, color, distance, parent):
        self.remove_data(node)
        self.insert_data(node, color, distance, parent)
        self.conn.commit()

    def remove_data(self, node):
        self.cur.execute("""DELETE FROM nodes
                            WHERE node_num = ?
                            """, (node,))
        self.conn.commit()
        return "Code removed successfully"

    def pop_data(self, node):
        self.cur.execute("""SELECT * FROM nodes
                            WHERE node_num = ?
                            LIMIT 1
                            """, (node,))
        node = self.cur.fetchone()
        return node

    def set_graph_list(self, list_nodes):
        for node in list_nodes:
            self.insert_data(node)

    def get_path(self, end_node):
        try:
            current_node = self.pop_data(end_node)
            while current_node:
                print(current_node[0])
                current_node = self.pop_data(current_node[3])
        finally:
            pass


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

    def set_vertices(self):
        for edges in self.edge_list_raw:
            for node in edges:
                self.vertices.add(node)

    def set_list_adjacency(self):
        for node in self.vertices:
            connected_nodes = [ver[1] for ver in list(filter(lambda v: v[0] == node, self.edge_list_raw))]
            self.list_adjacency[node] = connected_nodes

    def set_matrix_adjacency(self):
        self.matrix_adjacency = [[0 for _ in range(self.node_number)] for __ in range(self.node_number)]
        for edges in self.edge_list_raw:
            start_node = edges[0] - 1
            end_node = edges[1] - 1
            self.matrix_adjacency[start_node][end_node] = 1

    def bts(self, f_node):
        graph_db = NodeDataBase()
        graph_db.set_graph_list(self.vertices)

        start_node = graph_db.pop_data(f_node)
        graph_db.update_data(start_node[0], 'gray', start_node[2], start_node[3])

        travel_node_queue = ListQueue()
        travel_node_queue.enqueue(start_node[0])

        while len(travel_node_queue):
            parent_node = travel_node_queue.dequeue()
            for vert in self.list_adjacency[parent_node]:
                current_node = graph_db.pop_data(vert)
                if current_node[1] == 'white':
                    parent_node_dis = graph_db.pop_data(parent_node)[2]
                    graph_db.update_data(current_node[0], 'gray', parent_node_dis + 1, parent_node)
                    travel_node_queue.enqueue(current_node[0])
            parent_node_row = graph_db.pop_data(parent_node)
            graph_db.update_data(parent_node_row[0], 'black', parent_node_row[2], parent_node_row[3])
        return graph_db


if __name__ == '__main__':

    edge_file_name = open('edge_list_demo.txt', 'r')
    edges_list = list()
    for any_thing in edge_file_name:
        node_num = any_thing.split()
        edges_list.append((int(node_num[0]), int(node_num[1])))
    edges_list_raw = edges_list

    print('*****first Graph')
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
    print(first_graph.matrix_adjacency)

    print('**** Bfs ****')
    bfs_graph_list = first_graph.bts(6)
    print(bfs_graph_list.pop_data(6)[2])
    print(bfs_graph_list.pop_data(2)[2])
    print(bfs_graph_list.pop_data(7)[2])
    print(bfs_graph_list.pop_data(8)[2])
    print(bfs_graph_list.pop_data(9)[2])
    print(bfs_graph_list.pop_data(10)[2])
    print('***path***')
    print(bfs_graph_list.get_path(9))
