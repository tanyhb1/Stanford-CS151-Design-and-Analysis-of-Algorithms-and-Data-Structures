def main():
    a,b = input().split()
    a = int(a)
    b = int(b)
    diff = str(a-b)
    length = len(diff)
    x = ''
    for i in range(length):
        if i == length-1:
            if int(diff[i]) >= 0:
                a = int(diff[i])+1
                x = x + str(a)
            if int(diff[i]) == 9:
                a = int(diff[i])-1
                x = x + str(a)
        else:
            x = x + diff[i]
            
    print(x)
if __name__ == "__main__":
    main()