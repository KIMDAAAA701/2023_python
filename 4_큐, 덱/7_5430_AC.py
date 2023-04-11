# 찾아보니 R이 들어올 때마다 reverse하면 무조건 시간 초과
# flag를 사용해서 뒤집기 여부를 확인하여 마지막 한 번만 실행
# https://www.acmicpc.net/board/view/25456

from collections import deque

t = int(input())

for i in range(t):
    p = input()
    n = int(input())
    arr = input()[1:-1].split(',')

    queue = deque(arr)

    flag = 0

    if n == 0:
        queue = []

    for j in p:
        if j == 'R':
            flag += 1
        elif j == 'D':
            if len(queue) == 0:
                print("error")
                break
            else:
                if flag % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()

    else:
        if flag % 2 == 0:
            print("[" + ",".join(queue) + "]")
        else:
            queue.reverse()
            print("[" + ",".join(queue) + "]")