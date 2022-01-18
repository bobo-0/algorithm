import sys
input = sys.stdin.readline
x,y,w,h = map(int,input().split())
x_min = x
y_min = y
if w-x<x_min:
    x_min = w-x
if h-y<y_min:
    y_min = h-y
print(min(x_min,y_min))
