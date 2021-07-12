N = int(input())
d = [int(input()) for _ in range(N)]
d.sort(reverse=True)

steps = max_steps = 1
for i in range(1, len(d)):
    if d[i-1] > d[i]:
        steps += 1
        if steps > max_steps:
            max_steps = steps
    elif d[i-1] == d[i]:
        continue
    else:
        steps = 0

print(max_steps)
