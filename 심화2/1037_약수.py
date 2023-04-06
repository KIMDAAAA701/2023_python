# def solve_divisor(N):
#     d = set()
#     for i in range(2, int(N/2+1)+1):
#         if N % i == 0:
#             d.add(i)
#     return len(d)
#
# if __name__ == '__main__':
#     # num_divisor = int(input())
#     # divisor = list(map(int, input().split()))
#
#     # num_divisor = 6
#     # divisor = [3, 4, 2, 12, 6, 8]
#
#     num_divisor = 14
#     divisor = [14, 26456, 2, 28, 13228, 3307, 7, 23149, 8, 6614, 46298, 56, 4, 92596]
#     #
#     # # num_divisor = 2
#     # divisor = [4, 2]
#
#     divisor.sort()
#     candidate = set()
#
#     mid = int(num_divisor/2)
#
#
#     for d1 in divisor[0:mid]:
#         for d2 in divisor[mid:]:
#             candidate.add(d1*d2)
#
#     for can in sorted(candidate):
#         if solve_divisor(can) == num_divisor:
#             print(can)
#             break

x = int(input())
a = list(map(int, input().split()))
a.sort()
print(a[0]*a[-1])