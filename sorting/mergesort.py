def main():
    results = []
    with open('IntegerArray.txt', newline='') as inputfile:
        for line in inputfile:
            results.append(int(line.strip()))
    print(results)
    print(sort(results))


    
if __name__ == '__main__':
    main()
    
