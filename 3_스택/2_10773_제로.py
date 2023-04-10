import sys

K = int(sys.stdin.readline().rstrip())

numbers = []
for _ in range(K):
    num = int(sys.stdin.readline().rstrip())
    if num != 0:
        numbers.append(num)
    else:
        numbers.pop()
print(sum(numbers))