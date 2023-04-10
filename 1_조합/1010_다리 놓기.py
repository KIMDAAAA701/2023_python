def f(N):
    if N > 1:
        return (N * f(N - 1))
    else:
        return 1

if __name__ == '__main__':
    case = int(input())
    for _ in range(case):
        N, M = list(map(int, input().split()))
        print(f(M) // (f(M-N)*f(N)))