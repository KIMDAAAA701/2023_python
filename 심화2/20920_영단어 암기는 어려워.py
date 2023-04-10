import sys
from collections import Counter

N, M = map(int, (sys.stdin.readline()).split())

dic = {}
for _ in range(N):
    word = sys.stdin.readline().rstrip()
    if len(word) >= M:
        if dic.get(word):
            dic[word][0] += 1
        else:
            dic[word] = [1, len(word), word]

s_words = sorted(dic.items(), key = lambda x : (-x[1][0], -x[1][1], x[1][2]))

for w in s_words:
    print(w[0])



