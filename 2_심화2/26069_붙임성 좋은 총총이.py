numbers = input()

dancing = set(["ChongChong"])

for _ in range(0, int(numbers)):
    A, B = map(str, input().split())
    if A in dancing:
        dancing.add(B)
    elif B in dancing:
        dancing.add(A)

print(len(dancing))
