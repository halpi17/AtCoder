N = int(input())

pos_x = 0
pos_y = 0
pre_t = 0
can = True
for _ in range(N):
    t, x, y = map(int, input().split())
    for _ in range(t - pre_t):
        if pos_x < x:
            pos_x += 1
        elif pos_x > x:
            pos_x -= 1
        elif pos_y < y:
            pos_y += 1
        elif pos_y > y:
            pos_y -= 1
        else:
            pos_y -= 1

    pre_t = t

    if pos_x != x or pos_y != y:
        can = False

if can:
    print("Yes")
else:
    print("No")
