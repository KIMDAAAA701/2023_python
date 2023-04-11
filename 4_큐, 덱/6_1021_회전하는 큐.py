import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())

target = list(map(int, sys.stdin.readline().rstrip().split()))

cnt = 0 # 연산의 최소값

q = deque(range(1, N+1))

cnt = 0

for t in target:
    if q.index(t) >= (len(q)/2):
        k = len(q) - q.index(t)
        cnt += k
        q.rotate(k)
    else:
        k = q.index(t)
        cnt += k
        q.rotate(-k)
    q.popleft()
print(cnt)