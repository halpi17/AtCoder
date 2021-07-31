import sys

def find_smallest_difference(A, B, m, n):
    A.sort()
    B.sort()

    a = 0
    b = 0

    result = sys.maxsize

    while (a < m and b < n):
        if (abs(A[a] - B[b]) < result):
            result = abs(A[a] - B[b])
        if (A[a] < B[b]):
            a += 1
        else:
            b += 1
    return result

N, M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(find_smallest_difference(A, B, len(A), len(B)))
