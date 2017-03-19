def main():
    g = [0, 1, 0, 2, 1, 3, 2, 3, 2, 4, 3, 4, 3, 5, 4, 5]   
    #deciphering vertices
    vertices = []
    for x in g:
        if [x] not in vertices:
            vertices.append([x])
    #deciphering edges
    edges = [[g[x], g[x+1]] for x in range(0, len(g), 2)]
    print(DFSLoop(g, edges, vertices))   
    
def DFS(g, s, edges, topo, current_label):
    #mark s as explored)
    for edge in edges:
        #iterating over for all E(v,w), where v = s  
        if edge[0] == s and 'explored' not in edge:
            edge.append('explored')
            #recurse
            DFS(g, edge[1], edges, topo, current_label)
    #if topo is non-empty, set current label to the last item in topo minus 1
    #else if empty, topo will be n
    if len(topo) > 0:
        current_label = topo[list(topo)[len(topo)-1]]
    if s not in topo:
        #update topo with the current_label if considered element not currently in topo
        topo.update({s:current_label-1})
    return(edges)

def DFSLoop(g, edges, vertices):
    #dictionary to save the results of topological sort
    topo = {}
    current_label = len(vertices)
    #iterating over every edge to make sure none left out
    for edge in edges:
        #only consider if it has not been explored
        if 'explored' not in edge:
            DFS(g, edge[0], edges, topo, current_label)
    return(topo)
if __name__ == '__main__':
    main()