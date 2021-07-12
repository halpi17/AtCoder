N, Y = map(int, input().split())

none_flag = True
for x in range(N + 1):
    if not none_flag:
        break
    for y in range(N - x + 1):
        if 10000 * x + 5000 * y + 1000 * (N - x - y) == Y and none_flag:
            print(x, y, (N - x - y))
            none_flag = False
            break

if none_flag:
    print(-1, -1, -1)
