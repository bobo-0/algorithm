import sys
n = int(input())
data=[]
for i in range(0,n):
    a, b = (map(str, sys.stdin.readline().split()))
    result = ""
    for j in range(0,len(b)):
        result += b[j]*int(a)
    print(result)