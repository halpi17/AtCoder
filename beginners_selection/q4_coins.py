A = int(input()) # 500yen
B = int(input()) # 100yen
C = int(input()) # 50yen
X = int(input()) # total

ways = 0
for i in range(A+1):
    for j in range(B+1):
        for k in range(C+1):
            if 500 * i + 100 * j + 50 * k == X:
                ways += 1

print(ways)
