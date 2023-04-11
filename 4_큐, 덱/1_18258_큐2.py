import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())

s = deque()
for _ in range(N):
    line = (sys.stdin.readline().rstrip()).split()

    cmd = str(line[0])
    if len(line) > 1:
        x = int(line[-1])

    if cmd == "empty":
        print(0 if s else 1)
    elif cmd == "push":
        s.append(x)
    elif cmd == "size":
        print(len(s))
    elif len(s) == 0:
        print(-1)
    elif cmd == "pop":
        print(s.popleft())
    elif cmd == "front":
        print(s[0])
    elif cmd == "back":
        print(s[-1])