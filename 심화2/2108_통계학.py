# from collections import Counter
# def count_element(nums):
#     most_common = Counter(numbers).most_common()
#     if len(most_common) == 1:
#         second_most_common = most_common[0][0]
#     else:
#         second_most_common = sorted(set(numbers), key=lambda x: (-Counter(numbers)[x], x))[1]
#     print(second_most_common)
#
#
# numbers = []
#
# for _ in range(int(input())):
#     numbers.append(int(input()))
#
# numbers.sort()
#
# print(round(sum(numbers)/len(numbers)))
# print(numbers[len(numbers)//2])
# count_element(numbers)
# print(numbers[-1] - numbers[0])

########################################
########################################
from collections import Counter
import sys

def statistics(numbers):
    numbers.sort()

    cnt = Counter(numbers).most_common(2)

    print(round(sum(numbers) / len(numbers)))
    print(numbers[len(numbers) // 2])

    if len(cnt) > 1:
        if cnt[0][1] == cnt[1][1]:
            print(cnt[1][0])
        else:
            print(cnt[0][0])
    else:
        print(cnt[0][0])
    print(max(numbers) - min(numbers))


if __name__ == "__main__":
    numbers = []
    for _ in range(int(sys.stdin.readline())):
        num = int(sys.stdin.readline())
        numbers.append(num)

    statistics(numbers=numbers)
########################################
########################################