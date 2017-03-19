
from heap import heap_insert, heap_delete
import heapq
def main():
    edges = []
    vertices = []
    heap = []
    with open('dijkstraData.txt') as data:
        for line in data:
            a = line.strip().split()
            for _ in range(1, len(a), 1):
                placeholder = [int(a[_].split(',')[1]), int(a[_].split(',')[0]), int(a[_].split(',')[1])]
                edges.append(placeholder)
                if int(a[0]) not in vertices:
                    vertices.append(int(a[0]))
    print(edges)
    print(vertices)
    for x in range(len(edges)):
        heap_insert(heap, edges[x])
        
    print(heap)
    #X = set of vertices processed, A = dictionary of shortest path distances for vertex V, B = dictionary of the computed shortest path for V
    X = [1]
    A = {1:0}
    B = {1:None}

if __name__ == '__main__':
    main()