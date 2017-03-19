import sys
import threading
def main():
    A = dict()
    with open('2sum.txt') as data:
        for line in data:
            A[int(line.strip())] = True
    counter = 0
    for T in range(-10000,10000+1):
        print(counter, T)
        for x in A:
            y = T-x
            if y in A and x != y:
                counter = counter + 1
    print(counter)
if __name__ == '__main__':
    threading.stack_size(67108864) # 64MB stack
    sys.setrecursionlimit(2 ** 20)  # approx 1 million recursions
    thread = threading.Thread(target = main) # instantiate thread object
    thread.start() # run program at target)