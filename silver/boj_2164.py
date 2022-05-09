from collections import deque
n = int(input())
cards = deque([i for i in range(1,n+1)])
for _ in range(n-1):
    print(cards)
    cards.popleft()
    print(cards)
    cards.rotate(-1)
    print(cards)
print(cards[0])