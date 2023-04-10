import sys


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    s = []
    for _ in range(0, N):
        line = (sys.stdin.readline().rstrip()).split()

        cmd = str(line[0])
        if len(line) > 1:
            x = int(line[-1])

        if cmd == "push":
            s.append(x)
        elif cmd == "pop":
            print(s.pop() if s else -1)
        elif cmd == "size":
            print(len(s))
        elif cmd == "empty":
            print(0 if s else 1)
        elif cmd == "top":
            print(s[-1] if s else -1)
