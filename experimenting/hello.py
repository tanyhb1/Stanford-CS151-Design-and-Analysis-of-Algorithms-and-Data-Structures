#make four if conditions, based on previous move 
#for each (a,b) pair, there are only 2x2=4 possible moves
#they are (a,b),(-a,b),(a,-b)(-a,-b)
#we can remove one of the possible moves because it simply backtracks, leaving to 3 possible moves.
#bruteforce would take estimated n^2 time
#start from (n,n), work towards (0,0)
#answers organised (1,1), (1,2), (1,3), ..., (1,n-1)
#                  (2,1), ...,               (2,n-1)
#                   ...
#                  (n-1,1), ...,            (n-1,n-1)
#if impossible to reach (0,0) from (n-1,n-1), print -1 instead.
import operator
def main():
    n = int(input().strip())
    for a in range(1, n+1):
        for b in range(1, n+1):
            #tuple(map(operator.sub, A, move))
            position = (n-1, n-1)
            minimum = 0
            while(True):
                steps = 0
                steps_array = []
                wrong_array = []
                steps = Checker(position, a, b, steps, n, steps_array, wrong_array)

                print(min(steps), 'a', a,b)
                break
            
                #if no. of steps less than current min, and a solution exists (implying that steps > 0), set min to steps
                if steps<minimum and steps >0:
                    minimum = steps
                #if current minimum is 0, and steps == -1, set minimum to -1, and break loop
                elif minimum == 0 and steps == -1 :
                    solvable = -1                 
                
def Checker(position, a, b, steps, n, steps_array, wrong_array):
    move = a,b
    check = 0
    position = tuple(map(operator.sub, position, move))
    
    
    steps = steps + 1
    
    if position == (0,0):
        #once position is (0,0), add # of steps into array and break
        steps_array.append(steps)

    elif position[0] < 0 or position[1] < 0 or position[0] > n or position[1] > n:
        wrong_array.append(-1)
        check = -1
    print(steps_array, wrong_array)
    if check == -1:
        if len(steps_array) > 0:
            print('asdfsad')
            position = tuple(map(operator.add, position, move))
            return(wrong_array)
        else:
            
            return(wrong_array)
        
    if check == 0:
        if move[0] > 0 and move[1] > 0:
            Checker(position, -a, b, steps, n, steps_array, wrong_array)
            Checker(position, a, b, steps, n, steps_array, wrong_array)
            Checker(position, a, -b, steps, n, steps_array, wrong_array)
        elif move[0] < 0 and move[1] > 0:
            Checker(position, a, b, steps, n, steps_array, wrong_array)
            Checker(position, -a, b, steps, n, steps_array, wrong_array)
            Checker(position, -a, -b, steps, n, steps_array, wrong_array)
        elif move[0] > 0 and move[1] < 0:
            
            Checker(position, -a, -b, steps, n, steps_array, wrong_array)
            Checker(position, a, -b, steps, n, steps_array, wrong_array)
            Checker(position, a, b, steps, n, steps_array, wrong_array)
        else:
            Checker(position, a, -b, steps, n, steps_array, wrong_array)
            Checker(position, -a, -b, steps, n, steps_array, wrong_array)
            Checker(position, -a, b, steps, n, steps_array, wrong_array)
        check = 1
    if check == 1:    
    #if length of steps_array and wrong_array == length of position choices then break
        if len(steps_array) == 0:
            return(wrong_array)
        else:
            return(steps_array)
if __name__ == "__main__":
    main()