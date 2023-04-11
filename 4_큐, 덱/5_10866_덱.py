import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())

deq = deque()

for _ in range(N):
    line = sys.stdin.readline().rstrip().split()

    cmd = line[0]
    if len(line) > 1:
        x = line[1]

    if cmd == "empty":
        print(0 if deq else 1)
    elif cmd == "size":
        print(len(deq))
    elif cmd == "push_front":
        deq.appendleft(x)
    elif cmd == "push_back":
        deq.append(x)
    elif len(deq) == 0:
        print(-1)
    elif cmd == "pop_front":
        print(deq.popleft())
    elif cmd == "pop_back":
        print(deq.pop())
    elif cmd == "front":
        print(deq[0])
    elif cmd == "back":
        print(deq[-1])