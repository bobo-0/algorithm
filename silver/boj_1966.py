import sys
input = sys.stdin.readline
case = int(input().strip())

for _ in range(case):
    n,m = list(map(int,input().split()))
    importance = list(map(int,input().split()))
    indexes = list(range(n))
    indexes[m] = 'target'

    print_time = 0

    while True:
        if importance[0] == max(importance):
            print_time+=1
            
            if indexes[0] == 'target':
                print(print_time)
                break
            else :
                importance.pop(0)
                indexes.pop(0)
        else:
            importance.append(importance.pop(0))
            indexes.append(indexes.pop(0))
