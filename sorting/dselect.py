def main():
    
def DSelect(array, first, last):
    if first > last or last < 0:
        return(array)
    pivot = ChoosePivot(array)
    PartitionArray(array, first, last)
def PartitionArray(array, first, last):
    
def ChoosePivot(array):
    copy_array = []
    median_array = []
    start = 0
    end = start + 5
    for i in range(0, len(array)):
        if i%5 == 0 and i != 0:
            #for every five elements, sort each group and find median, copying median to new array A
            for j in range(start, end):
                #simple sorting
                minimum = copy_array[j]
                for k in range(start, end):
                    if copy_array[k] < minimum:
                        minimum = copy_array[k]
                        copy_array[j], copy_array[k] = copy_array[k], copy_array[j]
            #find median
            median = copy_array[start+2]
            #copy median to A
            median_array.append(median)
            
            #remembering to append every 5th element
            copy_array.append(array[i])
            
            #increase start and end boundaries by 5
            start = start + 5
            end = start + 5

        else:
            copy_array.append(array[i])
    #find median of array A using recursion
    if len(median_array) > 4:
        ChoosePivot(median_array)
    else:
        #sort and return median
        return(median_array[2])
if __name__ == "__main__":
    main()