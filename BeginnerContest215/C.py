import itertools

tmp = input().split()
S = sorted(list(tmp[0]))
K = int(tmp[1])

pair = list(itertools.permutations(S))
pair = list(set(pair))
pair.sort()

s = ""
for i in range(len(S)):
    s += pair[K-1][i]

print(s)
