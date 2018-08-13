def from_bin_to_int(bin_str):
    sum_bin = 0
    deg = 0
    bin_str = bin_str[::-1]
    for x in bin_str:
        if x == '1':
            sum_bin += (2 ** deg)
        deg += 1
    return sum_bin


def graph6_format(adj_matrix):
    n = len(adj_matrix)
    r = ""
    for j in range(n):
        for i in range(n):
            if i == j:
                break
            if adj_matrix[i][j] == 0:
                r += '0'
            else:
                r += '1'
    len_r = len(r)
    graph6 = ""
    graph6 += chr(n + 63)
    for i in range(0, len_r, 6):
        if len_r - i >= 6:
            sub_r = r[i:(i + 6)]
        else:
            sub_r = r[i:len_r]
            while len(sub_r) < 6:
                sub_r += '0'
        sum_bin = from_bin_to_int(sub_r)
        graph6 += chr(sum_bin + 63)
    return graph6


def construct_adjacency_matrix(graph):
    n = len(graph)
    adj_matrix = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(len(graph[i])):
            u = i
            v = graph[i][j]
            adj_matrix[u][v] = 1
            adj_matrix[v][u] = 1
    return adj_matrix


def layoff(d):
    n = len(d)
    d_graph = []
    for i in range(n):
        d_graph.append([d[i], i])
    graph = [[] for i in range(n)]
    flag = True
    while True:
        d_graph.sort(key=lambda x: x[0])
        d_graph.reverse()
        if d_graph[0][0] == 0:
            break
        for i in range(1, n):
            if d_graph[i][0] > 0 and d_graph[0][0] > 0:
                d_graph[i][0] -= 1
                d_graph[0][0] -= 1
                graph[d_graph[0][1]].append(d_graph[i][1])
                graph[d_graph[i][1]].append(d_graph[0][1])
        if d_graph[0][0] != 0:
            flag = False
            break
    if not flag:
        print("\nThe vector d = {} isn't a graphic".format(tuple(d)))
    else:
        adj_matrix = construct_adjacency_matrix(graph)
        graph6 = graph6_format(adj_matrix)
        print("\nGraph in graph6 format: {}".format(graph6))


if __name__ == "__main__":
    print("Vector of degrees d: ", end="")
    d = list(map(int, input().split()))
    layoff(d)