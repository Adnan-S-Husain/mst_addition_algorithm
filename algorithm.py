def check_edge(edge, mst):
    a = min(edge[0], edge[1])
    b = max(edge[0], edge[1])
    edge = (a, b)
    for e in mst:
        if e == edge:
            return True
    return False

def check_edge_deletable(edge, adding):
    a = min(edge[0], edge[1])
    b = max(edge[0], edge[1])
    e = (a, b)
    if e in adding:
        return False
    return True

def check_edge_in_path(edge, path):
    a = min(edge[0], edge[1])
    b = max(edge[0], edge[1])
    e = (a, b)
    if e in path:
        return True
    return False


def dfs(root, visited, path, end, cost, mst, adding):
    visited[root] = True
    # print("root:", root)
    if root == end:
        return 0, None
    for edge in mst:
        if edge[0] != root and edge[1] != root:
            continue
        if edge[0] == root:
            dest = edge[1]
        else:
            dest = edge[0]
        if check_edge_in_path((root, dest), path):
            continue
        c = cost[root][dest]
        # print("dfs:", (root, dest), c)
        if visited[dest] == True:
            if not check_edge_deletable((root, dest), adding):
                return 0, None
            return c, (min(root, dest), max(root, dest))
        t, e = dfs(dest, visited, path + [(min(root, dest), max(root, dest))], end, cost, mst, adding)
        if t != -1:
            if not check_edge_deletable((root, dest), adding):
                return t, e
            if (t > c):
                return t, e
            else:
                return c, (min(root, dest), max(root, dest))
    return -1, None

def new_mst(mst, adding, n, cost):
    mst = mst[:]
    for edge in adding:
        if check_edge(edge, mst):
            continue
        visited = [False for _ in range(n+1)]
        c, rm = dfs(edge[0], visited, [], edge[1], cost, mst, adding)
        # print(edge, c, rm)
        if rm:
            mst.remove(rm)
            mst.append(edge)
    
    return mst