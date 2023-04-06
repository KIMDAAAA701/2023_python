N, K = map(int, input().split())

up = 1
down = 1

for n in range(N-K+1, N+1):
    up = up * n
for k in range(2, K+1):
    down = down * k

print(int(up/down))
