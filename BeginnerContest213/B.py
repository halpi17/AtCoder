N = int(input())
A = list(map(int, input().split()))

sortedA = sorted(A)
print(A.index(sortedA[N-2]) + 1)