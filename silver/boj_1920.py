"""
%시간초과 : 시간 복잡도 O(n^2)%
import sys
input = sys.stdin.readline

n = int(input().strip())
ns = input().split()
m = int(input().strip())
ms = input().split()
check = [0 for _ in range(0,m)]
for i in range(0,m):
    for j in range(0,n):
        if ms[i] in ns[j]:
            print('1')
        else:
            print('0')

from sys import stdin, stdout
n = stdin.readline()
N = set(stdin.readline().split())
m = stdin.readline()
M = stdin.readline().split()

for l in M:
    stdout.write('1\n') if l in N else stdout.write('0\n')

import sys
input = sys.stdin.readline

n = input().strip()
ns = set(input().split())
m = input().strip()
ms = input().split()
for l in ms:
    if l in ns:
        print('1')
    else:
        print('0')
"""
import sys
input = sys.stdin.readline

n = input().strip()
N = sorted(set(map(int,(input().split()))))
m = input().strip()
M = map(int,input().split())

def binary(l,N, start, end):
    if start>end:
        return 0
    m = (start+end)//2
    if l == N[m]:
        return 1
    elif l<N[m]:
        return binary(l,N,start,m-1)
    else : 
        return binary(l,N,m+1,end)

for l in M:
    start = 0
    end = len(N)-1
    print(binary(l,N,start,end))