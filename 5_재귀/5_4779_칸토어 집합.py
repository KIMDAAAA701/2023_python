import sys

def Cantor(S):
    # S[:len(S)/3], S[len(S)/3: len(S)/3*2], S[len(S)/3*2:]
    ll = len(S)

    one_S = S[:ll//3]
    two_S = S[ll//3: ll//3*2]
    three_S = S[ll//3*2:]

    two_S = [" "] * int(ll/3)

    if ll == 3:
        return ["-", " ", "-"]
    else:
        return Cantor(one_S) + two_S + Cantor(three_S)


if __name__ == '__main__':
    while True:
        n = sys.stdin.readline().rstrip()
        if n == '':
            break
        if int(n) == 0:
            print("-")
        else:
            array = [ "-" for _ in range(3**int(n)) ]
            out = Cantor(array)
            print(''.join(out))





