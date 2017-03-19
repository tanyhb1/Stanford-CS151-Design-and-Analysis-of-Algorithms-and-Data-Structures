import sys

sys.setrecursionlimit(0x100000)

import threading
import sys
def main():
    edges = []
    #edges_copy is a copy of edges
    rev_edges = []
    with open('SCC') as data:
        for line in data:
            info = line.strip().split()
            info = list(map(int, info))
            edges.append([info[0], info[1]])
            rev_edges.append([info[1], info[0]])
    #run DFS loop twice, 1st time on rev_edges, 2nd time on edges
    #1st time we find the finishing time of each call.
    #store the ftime returned by 1st call
    print('yo')
    ftime = DFSLoop(rev_edges)
    print('a')
    n = 875714
    ldr = {}
    total = []
    print('ah')
    for x in range(n, 2, -1):
        for edge in edges:    
            if 'explored' not in edge and edge[0] == ftime[x]:
                storage = DFS(ftime[x], edges, ldr, ftime)
                if len(total) != 0:
                    for _ in total:   
                        storage = storage - _
                total.append(storage)
    print(total)
def DFS(s, edges, ldr, ftime,):
    #mark s as explored)
    global l
    global t
    if s not in ldr:
        ldr.update({s:l})
    for edge in edges:
        #iterating over for all E(v,w), where v = s  
        if edge[0] == s and 'explored' not in edge:
            edge.append('explored')
            DFS(edge[1], edges, ldr, ftime)
    if s not in ftime.values():
        t = t + 1
        ftime.update({t:s})
    return(len(ldr))
    

def DFSLoop(edges):
    #storage for leader and finishing times during the 2 passes.
    ldr = {}
    ftime = {}
    #global variables for ldr and ftime
    global l
    global t
    l = 0
    t = 0

    #starting from the end
    for edge in reversed(edges):            
        if 'explored' not in edge:
            #set leader to edge[0] which is the largest vertex since we're starting from the back
            l = edge[0]
            DFS(edge[0], edges, ldr, ftime)
            
    
    return(ftime)
class Counter(object):
    count = 0
    def counter(self):
        self.count = self.count + 1
if __name__ == '__main__':
    threading.stack_size(67108864) # 64MB stack
    sys.setrecursionlimit(2 ** 20)  # approx 1 million recursions
    thread = threading.Thread(target = main) # instantiate thread object
    thread.start() # run program at target)