N = int(input())
A = list(map(int, input().split()))

score = 0
alternating_flag = True
while A:
    if alternating_flag:
        score += max(A)
        alternating_flag = False
    else:
        score -= max(A)
        alternating_flag = True
    A.remove(max(A))

print(score)
