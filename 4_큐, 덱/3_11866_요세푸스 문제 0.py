import sys
from collections import deque

N, K = map(int, sys.stdin.readline().rstrip().split())

circle = deque([i for i in range(1, N+1)])

kill = []
while len(circle) > 0:
    for i in range(K-1):
        circle.append(circle.popleft())
    kill.append(circle.popleft())

print("<" + ", ".join(map(str, kill)) + ">")
