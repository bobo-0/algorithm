i = input()
word = i.upper()
char = [0 for i in range(0,26)]
for i in range(len(word)):
    char[ord(word[i])%65] += 1

max_val = max(char)
check = 0
for i in char:
    if i == max_val:
        check += 1

if check >1 : 
    print("?")
else:
    print(chr(char.index(max(char))+65))
