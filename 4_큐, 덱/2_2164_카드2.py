import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())

deq = deque([i for i in range(1, N+1)])

if N == 1:
    print(1)
else:
    while len(deq) > 1:
        deq.popleft()
        deq.append(deq.popleft())
    print(deq[0])
