import sys

cnt_zero = [1,0,1]
cnt_one = [0,1,1]

def fibonacci(N):
    length = len(cnt_zero)
    if N>=length:
        for i in range(length,N+1):
            cnt_zero.append(cnt_zero[i-1]+cnt_zero[i-2])
            cnt_one.append(cnt_one[i-1]+cnt_one[i-2])

    print('{} {}'.format(cnt_zero[N],cnt_one[N]))

T = int(sys.stdin.readline())    
        
for i in range(T):
    fibonacci(int(sys.stdin.readline()))
