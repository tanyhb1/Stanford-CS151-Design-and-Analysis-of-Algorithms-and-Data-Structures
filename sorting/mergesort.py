import timer
def main():
    results = []
    with open('IntegerArray.txt', newline='') as inputfile:
        for line in inputfile:
            results.append(int(line.strip()))
    print(results)
    print(sort(results))

def sort(x):
    if len(x) == 1:
        return(x)
    else:
        middle = len(x)/2
        left = sort(x[:int(middle)])
        right = sort(x[int(middle):])
        
        return(merge(left, right))
        
def merge(left, right):
    i, j = 0, 0
    c = []

    while(len(c) < len(left) + len(right)):
        if left[i] < right[j]:
            c.append(left[i])
            i = i + 1
        else:
            c.append(right[j])
            j = j + 1
        if i == len(left) or j == len(right):
            c.extend(left[i:] or right[j:])
            break
    return(c)


    
if __name__ == '__main__':
    main()
    