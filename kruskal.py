def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, rank, x, y):
    if rank[x] < rank[y]:
        parent[x] = y
    elif rank[x] > rank[y]:
        parent[y] = x
    else:
        parent[y] = x
        rank[x] += 1

def KruskalMST(graph, n, cost):
    V = n
    result = []
    i = 0
    e = 0
    graph.sort(key=lambda item: cost[item[0]][item[1]])
    parent = [i for i in range(V + 1)]
    rank = [0] * (V + 1)

    while e < V - 1:
        u, v = graph[i]
        w = cost[u][v]
        i = i + 1
        x = find(parent, u)
        y = find(parent, v)
        if x != y:
            e = e + 1
            result.append((u, v))
            union(parent, rank, x, y)

    minimumCost = 0
    print("Edges in the constructed MST")
    for u, v in result:
        weight = cost[u][v]
        minimumCost += weight
        print("%d -- %d == %d" % (u, v, weight))
    print("Cost of Minimum Spanning Tree:", minimumCost)
    return result

if __name__ == "__main__":
    # KruskalMST(graph, n, cost)
    pass