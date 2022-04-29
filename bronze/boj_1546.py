import sys
n = int(input())
s = list(map(int,sys.stdin.readline().split()))
high = max(s)
for sc in range(0,n):
    s[sc] = (s[sc]/high)*100
print(sum(s)/n)
