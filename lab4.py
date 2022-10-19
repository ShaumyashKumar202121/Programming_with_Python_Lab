def AdjacencyMatrix(nd):
    ad_Mtx = [[0 for i in range(nd)] for j in range(nd)]

    for i in range(nd):
        u, v, w = map(int, input("Enter the vertices and weight: ").split(','))

        ad_Mtx[u][v] = w
        ad_Mtx[v][u] = w
    
    return ad_Mtx


node = int(input("Enter the number of vertices: "))
print(AdjacencyMatrix(node))