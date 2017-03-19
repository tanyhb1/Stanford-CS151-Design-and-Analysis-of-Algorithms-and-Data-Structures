import sys
import threading

def main():
    
    lines = open('2sum.txt').read().splitlines()
    #lines = open('2sum-tc/test1.txt').read().splitlines()
    data = map(lambda x: int(x), lines)

    #count = 0
    #for t in range(2500, 4000+1):
    #    if(TwoSum_Naive(data, t)):
    #        count += 1
    #print('Naive:' + str(count))
    
    #count = 0
    #sorted_data = sorted(data)
    #for t in range(2500, 4000+1):
    #    if(TwoSum_BinarySearch(sorted_data, t)):
    #        count += 1
    #print('Via binary search: ' + str(count))
    
    hashTable = dict()
    
    for x in data:
        hashTable[x] = True
    print('size:' + str(len(hashTable)))
    print(hashTable)
    count = 0
    for t in range(-10000, 10000+1):
        if(TwoSum_HashTable(hashTable, data, t)):
            count += 1
    print('Via hash table: ' + str(count))
    
def TwoSum_HashTable(hashTable, lst, target):
    '''
    2-SUM algorithm via hash table.
    
    O(n) time.
    '''
    for x in lst:
        y = target-x
        if y in hashTable and x != y:
            return(True)

if __name__ == '__main__':
    main()
    
