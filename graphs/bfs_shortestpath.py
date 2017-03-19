
def main():
    graph = [0, 1, 0, 2, 1, 3, 2, 3, 2, 4, 3, 4, 3, 5, 4, 5, 5, 6]
    #deciphering the graph's edges and vertices
    BFS(graph, graph[0])     
#takes in graph g and start vertex s
def BFS(g, s):
    #assume entire graph unexplored initially, marking if explored by appending 'explored'
    #Q = queue data structure initialised with s
    Q = [s]
    #initialise distance dictionary with distance(s=0)=0
    distance = {0:0}
    #deciphering the graph's edges
    edges = [[g[x], g[x+1]] for x in range(0, len(g), 2)]
    print(edges)
    while(Q):
        #removing the first node of the queue data structure and storing it to v
        v = Q.pop(0)
        for edge in edges:
            if edge[0] == v and 'explored' not in edge:
                #v = edge[0], w = edge[1], check to see if w exists in dictionary already to prevent unnecessary overwriting of data from further calls
                if edge[1] not in distance:
                    #update distance dictionary with key w = dist(v)+1, where edge[1] = w and edge[0] = v
                    distance.update({edge[1]:distance[edge[0]]+1})
                edge.append('explored')                    
                Q.append(edge[1])
                
    print(distance)

if __name__ == '__main__':
    main()