def solution(s):
    words = s.split(" ")
    for i in range(0,len(words)):
        words[i] = words[i].capitalize()
    return (" ").join(words)