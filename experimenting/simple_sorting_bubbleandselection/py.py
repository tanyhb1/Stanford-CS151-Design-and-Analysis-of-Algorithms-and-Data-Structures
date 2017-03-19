c = [0,2,5,1,7,8,6,4,3,9]    
start = 0
end = len(c)  
for j in range(start, end):
#simple sorting
    minimum = c[j]
    for k in range(start, end):
        print(c)
        if c[k] > minimum:
            minimum = c[k]
            c[j], c[k] = c[k], c[j]
print(c)