def main(): 
    A = []
    with open('2sum.txt') as data:
        for line in data:
            A.append(int(line.strip()))
    A = sorted(A)
    counter = 0
    for T in range(-10000, 10001): 
        print(counter)
        for i in range(0, len(A)):
            if(two_sum(A, T, i)):
                counter = counter + 1
    print(counter)
def two_sum(A, T, index):
    first = 0
    last = len(A)-1
    while(first<last):
        middle = (first+last)//2
        #x+y < T, search right side
        if A[middle] < T-A[index]:
            first = middle+1
        #x+y > T, search left side
        elif A[middle] > T-A[index]:
            last = middle-1
        else:
            if(A[middle] != A[index]):
                return(True)
if __name__ == '__main__':
    main()