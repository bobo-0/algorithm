word = input()
alpha = [-1 for _ in range(0,26)]
for i in range(len(word)):
    if alpha[ord(word[i])-97] == -1:
        alpha[ord(word[i])-97] = i
for j in alpha:
 print(j, end=" ")
