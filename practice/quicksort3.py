import timer
def main():
    a = []
    x = Counter()
    with open('QuickSort.txt') as data:
        for line in data:
            a.append(int(line.strip()))
    QuickSort(a, 0, len(a)-1, x)
    print(a)
    print(x.count)
def QuickSort(array, first, last, x):
    
    if first>=last or first<0:
        return(array)
    pivot = PartitionArray(array, first, last, x)
    QuickSort(array, pivot+1, last, x)
    QuickSort(array, first, pivot-1, x)

    
def PartitionArray(array, first, last, x):
    
    #median position between the first and last elements
    length = last+first 
    if length%2 == 0:
        mid = (length//2)
    else:
        mid = ((length+1)//2)-1
        
    array[mid], array[first] = array[first], array[mid]
    pivot = array[first]
    i = first+1
    for j in range(first+1, last+1):
        if (array[j] < pivot):
            array[i], array[j] = array[j], array[i]
            i = i+1
    array[i-1], array[first] = array[first], array[i-1]
    x.count = x.count + last - first - 1
    return(i-1)
    
class Counter(object):
    count = 0
    def counter(self):
        self.count = self.count + 1
if __name__ == "__main__":
    main()