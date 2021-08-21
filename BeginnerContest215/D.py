from math import *

N, M = map(int, input().split())
A = list(map(int, input().split()))
setA = set(A)

dp = [1] * (M + 1)
dp[0] = 0

for i in range(2, M + 1):
    find = False
    for a in range(i, (10 ** 5) + 1, i):
        if a in setA:
            find = True
            break
    if find:
        for a in range(i, M + 1, i):
            dp[a] = 0

print(sum(dp))
for i in range(M + 1):
    if dp[i] == 1:
        print(i)
