def main():
    a = []
    x = Counter()
    with open('*.txt') as data:
        for line in data:
            a.append(int(line.strip()))
    QuickSort(a, 0, len(a)-1, x)
    print(a)
    print(x.count)
def QuickSort(array, left, right, x):
    if right is None:
        right = len(array)-1
    if left>=right or left<0:
        return(array)
    x.count = x.count + right - left -1
    


                                                                        #makes pivot the first element in the array
    CurrentPosition = PartitionArray(array, left, right)                                     #Current position of pivot
    QuickSort(array, left, CurrentPosition-1, x)                                #try, confused if array will split if i slice an array
    QuickSort(array, CurrentPosition+1, right, x)
def PartitionArray(array, left, right):
    pivot = array[right]
    i = right-1
    for j in range(right-1, left-1, -1):
        if array[j] > pivot:
            array[j], array[i] = array[i], array[j]
            i = i-1
        
    array[right], array[i+1] = array[i+1], array[right]
    return(i+1)


def ChoosePivot(array, length):
    return(0)
    #to be implemented according to pset specs
    
class Counter(object):
    count = 0
    def counter(self):
        self.count = self.count + 1

    
if __name__ == "__main__":
    main()