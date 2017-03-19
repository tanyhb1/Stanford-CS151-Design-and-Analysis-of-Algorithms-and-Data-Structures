def main():
    graph = ['a', 'b', 'a','c','c','d','d','e','d','f','e','f']
    DFS(graph, graph[0])
def DFS(g, s):
    #S = stack data structure initialised with s
    S = [s]
    edges = [[g[x], g[x+1]] for x in range(0, len(g), 2)]
    while(S):
        #removing last node of S priority queue
        v = S.pop(len(S)-1)
        for edge in edges:
            if edge[0] == v and 'explored' not in edge:
                edge.append('explored')
                S.append(edge[1])
                print(edge)
    print(edges)            
    
if __name__ == '__main__':
    main()