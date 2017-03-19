from random import randint

def main():
    a = [24,56,1324,9837,123,345,651,3547,345,234,974,293487,321,13249]
    order_statistic = int(input())
    RSelect(a, 0, len(a)-1, order_statistic)

def RSelect(array, first, last, k):
    #where k is the kth order statistic you want to find
    if first > last or first < 0:
        return(array)
    pivot_position = PartitionArray(array, first, last)
    if pivot_position == k:
        #if position of pivot == kth order, return pivot
        print(array[pivot_position])
        
    elif pivot_position < k:
        #if position of pivot < kth order
        RSelect(array, pivot_position+1, last, k)
    elif pivot_position > k:
        RSelect(array, first, pivot_position-1, k)
def PartitionArray(array, first, last):
    
    pivot = randint(first, last)
    #swapping pivot and first element of array to make sure pivot is always the first element during partitioning
    array[first], array[pivot] = array[pivot], array[first]
    i = first+1
    for j in range(first+1, last+1):
        #if current array less than pivot
        if array[j] < array[first]:
            #swap places with the right most of the left boundary that contains the elements smaller than the pivot
            array[i], array[j] = array[j], array[i]
            #increment i since left boundary has one more element after swap
            i = i+1
    #since i is first element > pivot, i-1 is the pivot's proper position. swap pivot's current position with it's proper position.
    array[i-1], array[first] = array[first], array[i-1]
    #return pivot_position
    return(i-1)
if __name__ == "__main__":
    main()