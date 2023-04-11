import sys
from collections import deque

test_case = int(sys.stdin.readline().rstrip())

for _ in range(test_case):
    doc_num, find = list(map(int, sys.stdin.readline().rstrip().split()))


    imp = list(map(int, sys.stdin.readline().rstrip().strip().split()))
    idx = list(range(doc_num))

    cnt = 0
    while True:
        if imp[0] == max(imp):
           cnt += 1

           if idx[0] == find:
               print(cnt)
               break
           else:
               imp.pop(0)
               idx.pop(0)
        else:
            imp.append(imp.pop(0))
            idx.append(idx.pop(0))