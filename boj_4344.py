import sys
num = int(sys.stdin.readline())
for data in range(num):
    data = list(map(int,sys.stdin.readline().split()))
    avg = (sum(data[1:]))/data[0]
    cnt = 0
    for d in data[1:]:
        if d > avg:
            cnt+=1
    print(f'{(cnt/data[0])*100:.3f}%')
