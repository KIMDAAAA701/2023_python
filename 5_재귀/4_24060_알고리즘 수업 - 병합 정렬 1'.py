import sys

def merge_sort(A):
    if len(A) == 1:
        return A

    mid = (len(A)+1)//2

    left = merge_sort(A[:mid])
    right = merge_sort(A[mid:])

    i, j = 0, 0
    A2 = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            A2.append(left[i])
            ans.append(left[i])
            i += 1
        else:
            A2.append(right[i])
            ans.append(right[i])
            j += 1
    while i < len(left):
        A2.append(left[i])
        ans.append(left[i])
        i += 1
    while j < len(right):
        A2.append(right[j])
        ans.append(right[j])
        j += 1
    return A2


if __name__ == '__main__':
    N, K = map(int, sys.stdin.readline().rstrip().split())
    A = list(map(int, sys.stdin.readline().rstrip().split()))

    ans = []
    merge_sort(A)

    if len(ans) >= K:
        print(ans[K - 1])
    else:
        print(-1)
