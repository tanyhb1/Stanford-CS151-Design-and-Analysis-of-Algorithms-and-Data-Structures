def main():
    edges = []
    vertices = []
    with open('dijkstraData.txt') as data:
        for line in data:
            a = line.strip().split()
            for _ in range(1, len(a), 1):
                placeholder = [int(a[0]), int(a[_].split(',')[0]), int(a[_].split(',')[1])]
                edges.append(placeholder)
                if int(a[0]) not in vertices:
                    vertices.append(int(a[0]))
    print(edges)
    print(vertices)
    #X = set of vertices processed, A = dictionary of shortest path distances for vertex V, B = dictionary of the computed shortest path for V
    X = [1]
    A = {1:0}
    B = {1:None}
    
    #while x!=V
    #for all crossing edges E(v, w) with v in X and W in (X-V), pick edge that minimises (A[v] + length of vw).
    #label the edge E(v*, w*)
    #set A[w*] = A[v*] + lv*w*
    #set B[w*] = B[v*] link with (v*,w*)
    while (len(X) < len(vertices)):
        #setting minimum to be arbitrary large number to act as comparison
        minimum = 99999
        storage = []
        for edge in edges:
            #edge[0] = v, edge[1] = w; if v in X and W not in X (crossing edges between X and W)
            if edge[0] in X and edge[1] not in X:
                #set distance to current known distance of v + lvw
                distance = A[edge[0]] + edge[2]
                #finding the minimum distance for all edge in edges
                if distance < minimum:
                    minimum = distance
                    #storing the edge that has the minimum distance
                    storage = edge
        #storage = (v*,w*), the edge that satisfies Dijkstra's greedy criterion.
        #store w* in A with value of distance b/w s to w
        A[storage[1]] = minimum
        #adding w* to X
        X.append(storage[1])
        B[storage[1]] = B[storage[0]], storage[1]
   
    #simple function to find distance of a key, breaks when 0 entered        
    while(True):
        vertex = int(input())
        if vertex == 0:
            break
        elif vertex > 200:
            print('Please enter a vertex within the range.')
        else:
            print(A[vertex], B[vertex])
if __name__ == '__main__':
    main()