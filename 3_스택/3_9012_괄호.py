import sys

T = int(sys.stdin.readline().rstrip())


for _ in range(0, T):
    input = sys.stdin.readline().rstrip()
    vps = []
    out = ""
    for str in input:
        if str == '(':
            vps.append(1)
        elif str == ')':
            if len(vps) > 0:
                vps.pop()
            else:
                out = "NO"
                break
    if vps != [] or out == "NO":
        print("NO")
    else:
        print("YES")