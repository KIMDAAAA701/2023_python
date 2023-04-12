import sys
def recursion(s, l, r, cnt):
    if l >= r:
        return (1, cnt)
    elif s[l] != s[r]:
        return (0, cnt)
    else:
        return recursion(s, l+1, r-1, cnt+1)

if __name__ == '__main__':
    T = int(sys.stdin.readline().rstrip())

    for _ in range(T):
        S = sys.stdin.readline().rstrip()
        cnt = 0
        output = recursion(S, 0, len(S) - 1, cnt+1)

        print(output[0], output[1])
