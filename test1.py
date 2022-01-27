# pass by value or reference
# def func1(b):
#     b.append(4)
#
#
# if __name__ == '__main__':
#     a:list = [1, 2, 3]
#     print(a)
#     func1(a)
#     print(a)

# test str methods
# s1 = "burger"
# s2 = "gay"
#
# # s3=s1.join(["rf","psyco",s2])
# # print(s3)
# a = s1.find("g" , 0 , -1)
# print(a)

# map
# def myfunc(a):
#   return len(a)
#
# x = map(myfunc, ('apple', 'banana', 'cherry'))
#
# print("\n\n",x)
#
# #convert the map into a list, for readability:
# print(list(x))
#
# print("****************1**************")
# #################
# list1 = [1 , 2 , 3]
#
# for item in map(myfunc, ('apple', 'banana', 'cherry')): print(item)
#
# print("****************2**************")
# for item in x: print(item)
#
# for item in map(lambda n : n**2 , list1): print(item)
# for item in map(lambda n : n**2 , [1 , 2 , 3]): print(item)
#
# print("****************3**************")
#
# x2 = filter(myfunc, ('apple', 'banana', 'cherry'))
# print(x2)
# print(list(x2))
#
# for item in filter(myfunc, ('apple', 'banana', 'cherry')): print(item)
# for item in filter(lambda n : n<3 , list1): print(item)

# test print
# print("hi","hello" ,end = '   *')
# print("End line")


# if __name__ == '__main__':
#     listB = [7, 2, 3, 4, 0]
#
#
#     def findminmax(listA=[]):
#         listA.sort()
#         print(listA[0])
#         print(listA[-1])
#
#
#     def findDupl(listB):
#         setA = {i for i in listB}
#         if setA.__len__() == listB.__len__():
#             print("yes")
#         else:
#             print("no")
#
#
#     findminmax(listB)
#     findDupl(listB)


# a = [1, 2, 3, 4]
# print(a[:2])
# b = {3, 4, 2, 7, 1}
# print(b)
# c = {'c', 'a', 'd', 'b'}
# print(c)
# print(a.pop(0))
# d = {i: None for i in a}
# print(d)
# print(d[2])

# if __name__ == '__main__':
#     v = [float('inf')] * 5
#     print(v)
import networkx as nx
import matplotlib.pyplot as plt

# if __name__ == '__main__':
    # G=nx.DiGraph()
    # G.add_node(0),G.add_node(1),G.add_node(2),G.add_node(3),G.add_node(4)
    # G.add_edge(0, 1),G.add_edge(1, 2),G.add_edge(0, 2),G.add_edge(1, 4),G.add_edge(1, 3),G.add_edge(3, 2),G.add_edge(3,1),G.add_edge(4,3)
    # nx.draw(G, with_labels=True, font_weight='bold')
    # plt.show()



    # G = nx.cubical_graph()
    # pos = nx.spring_layout(G, seed=3113794652)  # positions for all nodes
    #
    # # nodes
    # options = {"edgecolors": "tab:gray", "node_size": 800, "alpha": 0.9}
    # nx.draw_networkx_nodes(G, pos, nodelist=[0, 1, 2, 3], node_color="tab:red", **options)
    # nx.draw_networkx_nodes(G, pos, nodelist=[4, 5, 6, 7], node_color="tab:blue", **options)
    #
    # # edges
    # nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)
    # nx.draw_networkx_edges(
    #     G,
    #     pos,
    #     edgelist=[(0, 1), (1, 2), (2, 3), (3, 0)],
    #     width=8,
    #     alpha=0.5,
    #     edge_color="tab:red",
    # )
    # nx.draw_networkx_edges(
    #     G,
    #     pos,
    #     edgelist=[(4, 5), (5, 6), (6, 7), (7, 4)],
    #     width=8,
    #     alpha=0.5,
    #     edge_color="tab:blue",
    # )
    #
    # # some math labels
    # labels = {}
    # labels[0] = r"$a$"
    # labels[1] = r"$b$"
    # labels[2] = r"$c$"
    # labels[3] = r"$d$"
    # labels[4] = r"$\alpha$"
    # labels[5] = r"$\beta$"
    # labels[6] = r"$\gamma$"
    # labels[7] = r"$\delta$"
    # nx.draw_networkx_labels(G, pos, labels, font_size=22, font_color="whitesmoke")
    #
    # plt.tight_layout()
    # plt.axis("off")
    # plt.show()



# import numpy as np
# import matplotlib.pylab as pl
#
# if __name__ == '__main__':
#
#     nx = 4
#     ny = 5
#     data = np.random.randint(0,10,size=(ny,nx))
#
#     pl.figure()
#     tb = pl.table(cellText=data, loc=(0,0), cellLoc='center')
#
#     tc = tb.properties()['child_artists']
#     for cell in tc:
#         cell.set_height(1/ny)
#         cell.set_width(1/nx)
#
#     ax = pl.gca()
#     ax.set_xticks([])
#     ax.set_yticks([])
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':

    a = [[0 for i in range(100)] for _ in range(100)]
    a[2][2]=1
    # a = np.random.randint(-1, 2, (5, 5))
    plt.ion()
    plt.imshow(a, interpolation='none')
    plt.show()