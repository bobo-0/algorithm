import sys
n = int(input())
words = [sys.stdin.readline().strip() for _ in range(n)]
words = list(set(words))
words.sort()
words.sort(key = len)
for i in words:
    print(i)
