N, K = map(int, input().split())
candy = list(map(int, input().split()))

color_max_num = 1
consecutive_candy = candy[:K]
for i in range(1, N - K + 1):
    if len(set(consecutive_candy)) > color_max_num:
        color_max_num = len(set(consecutive_candy))
    consecutive_candy.append(candy[i+K-1])
    consecutive_candy = consecutive_candy[1:]

print(color_max_num)