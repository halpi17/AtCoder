S = input()

t_str = ["dream", "dreamer", "erase", "eraser"]

while S[-7:] in t_str or S[-6:] in t_str or S[-5:] in t_str:
    for t in t_str:
        if S.endswith(t):
            S = S[:-len(t)]
            break

if S:
    print("NO")
else:
    print("YES")
