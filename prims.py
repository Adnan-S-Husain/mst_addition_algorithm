def prim(N, G):
    INF = 9999999
    N = 7
    G = G[:]
    G.pop(0)
    for row in G:
        row.pop(0)

    selected_node = [0 for _ in range(N)]

    no_edge = 0

    selected_node[0] = True
    ans = []
    while (no_edge < N - 1):
        minimum = INF
        a = 0
        b = 0
        for m in range(N):
            if selected_node[m]:
                for n in range(N):
                    if ((not selected_node[n]) and G[m][n]):
                        if minimum > G[m][n]:
                            minimum = G[m][n]
                            a = m
                            b = n
        ans.append((min(a+1, b+1), max(a+1, b+1)))
        selected_node[b] = True
        no_edge += 1
    return ans
prim()