from math import floor
def main():
    heap_storage = []



        
def heap_insert(heap, key):
    #add new key to very end of heap
    heap.append(key)
    key_index = len(heap)
    while(True):
        #finding the index of parent which is based on whether key_index is even or odd
        if key_index>1:
            if key_index%2 == 0:
                parent_key_index = (key_index//2)
                parent_key = heap[parent_key_index-1]
            else:
                parent_key_index = floor(key_index//2)
                parent_key = heap[parent_key_index-1]
        else:
            break       
        
        #if invariant not kept,
        if parent_key > key:
            #bubble up till it is restored.
            heap[parent_key_index-1], heap[key_index-1] = heap[key_index-1], heap[parent_key_index-1]
            #set new key_index to be the new position index
            key_index = parent_key_index
        else:
            break
    
def extract_min(heap):
    #since formula for children = 2*i, 2*i+1 will cause index to go out of range for cases where len(heap) <3,
    #insert bottleneck here
    if len(heap) < 3:
        if len(heap) == 0:
            return('heap is empty bruh')
        minimum = min(heap)
        heap.remove(minimum)
        return(minimum)
    #swap tail with root before deleting the new tail. simpler way to delete root.
    heap[len(heap)-1], heap[0] =  heap[0], heap[len(heap)-1]
    #saving the root before deleting.
    minimum = heap.pop()
    root_index = 1 
    while(root_index*2+1 <= len(heap)):
        #finding children index
        children_index_1, children_index_2 = root_index*2, root_index*2 + 1 
        #finding keys
        root_key, children_key_1, children_key_2 = heap[root_index-1], heap[children_index_1-1], heap[children_index_2-1]
        
        #finding minimum of the children
        if children_key_1 < children_key_2:
            children_index = children_index_1
        else:
            children_index = children_index_2   
        children_key = heap[children_index-1]
        
        #if invariant isnt kept, bubble down until it is restored
        if root_key > children_key:
            heap[root_index-1], heap[children_index-1] = heap[children_index-1], heap[root_index-1]
            #set new key_index to be the new position index
            root_index = children_index
        else:
            break
    #return previously found minimum
    return(minimum)

def heap_delete(heap, key):
    key_index = heap.index(key)+1
    heap[key_index-1], heap[len(heap)-1] = heap[len(heap)-1], heap[key_index-1]
    x = heap.pop()
    while(key_index*2+1 <= len(heap)):
        #finding children index
        children_index_1, children_index_2 = key_index*2, key_index*2 + 1 
        #finding keys
        key, children_key_1, children_key_2 = heap[key_index-1], heap[children_index_1-1], heap[children_index_2-1]
        
        #finding minimum of the children
        if children_key_1 < children_key_2:
            children_index = children_index_1
        else:
            children_index = children_index_2   
            
        children_key = heap[children_index-1]
        
        if key_index%2 == 0:
            parent_key_index = (key_index//2)
            parent_key = heap[parent_key_index-1]
        else:
            parent_key_index = floor(key_index//2)
            
            parent_key = heap[parent_key_index-1]

        #if invariant isnt kept, bubble down until it is restored
        if key > children_key:
            heap[key_index-1], heap[children_index-1] = heap[children_index-1], heap[key_index-1]
            #set new key_index to be the new position index
            key_index = children_index
        elif key < parent_key:
            #bubble up till it is restored.
                heap[parent_key_index-1], heap[key_index-1] = heap[key_index-1], heap[parent_key_index-1]
            #set new key_index to be the new position index
                key_index = parent_key_index
        else:
            break
    #return previously found minimum
if __name__ == '__main__':
    main()