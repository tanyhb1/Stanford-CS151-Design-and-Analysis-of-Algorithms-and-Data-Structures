def main():
    global counter
    counter = 0
    graph = [0, 1, 0, 2, 1, 3, 2, 3, 2, 4, 3, 4, 3, 5, 4, 5]
    edges = [[graph[x], graph[x+1]] for x in range(0, len(graph), 2)]
    vertices = []
    for x in graph:
        if [x] not in vertices:
            vertices.append([x])
    print(edges)
    print(DFS(graph, graph[0], edges))
    print(counter)
    
def DFS(g, s, edges):
    #mark s as explored)
    global counter
    counter = counter + 1
    for edge in edges:
        #iterating over for all E(v,w), where v = s  
        if edge[0] == s and 'explored' not in edge:
            edge.append('explored')
            DFS(g, edge[1], edges)
    return(edges)
if __name__ == '__main__':
    main()
