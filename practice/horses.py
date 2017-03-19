#n horses on stable, skill of horse i is s[i]]
#pick 2 horses x,y whereby difference d[x,y] in horses s[x], s[y] would be minimum
from quicksort3 import *
def main():
        test_cases = int(input())
        total_horses = int(input())
        skill_array = input().split()
        array = []
        for a in skill_array:
            array.append(int(a))
        QuickSort(array, 0, len(array)-1)
        
    
if __name__ == "__main__":
    main()