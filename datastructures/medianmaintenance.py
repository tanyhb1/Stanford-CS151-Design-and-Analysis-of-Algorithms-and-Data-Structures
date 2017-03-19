import heapq

def main():
    High = []
    Low = []
    medians = 0
    with open('test.txt') as data:
        for line in data:
            x = int(line.strip())            
            if len(High) + len(Low) == 0:
                heapq.heappush(Low, x)
            else:
                if x < heapq.nlargest(1, Low)[0]:
                    heapq.heappush(Low, x)
                elif x > heapq.nlargest(1, Low)[0]:
                    heapq.heappush(High, x)
            if len(High) > len(Low)+1:
                y = heapq.heappop(High)
                heapq.heappush(Low, y)        
            elif len(Low) > len(High)+1:
                y = heapq.nlargest(1, Low)[0]
                heapq.heappush(High, y)
                Low.remove(y)
            if len(Low) > len(High):
                a = heapq.nlargest(1, Low)[0]
                medians = medians + heapq.nlargest(1, Low)[0]
            elif len(High) >= len(Low):
                a = heapq.nsmallest(1, High)[0]
                medians = medians + heapq.nsmallest(1, High)[0]
            print(a)
    print(medians%10000)
if __name__ == '__main__':
    main()