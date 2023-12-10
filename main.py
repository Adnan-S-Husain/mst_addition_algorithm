import dataset2 as dataset
from kruskal import KruskalMST
from algorithm import new_mst
import networkx as nx
import matplotlib.pyplot as plt



def showNN(name, data):
    print(name)
    G = nx.Graph()
    G.add_edges_from(data)
    nx.draw_networkx(G)
    plt.show()
    

def solve():
    showNN("Graph", dataset.graph)
    mst = KruskalMST(dataset.graph, dataset.n, dataset.cost)
    print("MST before adding:", mst)
    showNN("MST before adding:", mst)

    adding = dataset.adding


    mst_after_adding = new_mst(mst, adding, dataset.n, dataset.cost)
    print("MST after adding:", mst_after_adding)
    showNN("MST after adding:", mst_after_adding)
    
    
    
solve()