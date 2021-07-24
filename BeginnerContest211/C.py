from itertools import *
import itertools

S = input()

chokudai = 'chokudai'
chokudai_count = 0

# for i in range(len(S)-7):
#     print(S[i:i+8])

h_list = [''.join(v) for v in list(itertools.combinations(S, 8))]
for h in h_list:
    if h == chokudai:
        chokudai_count += 1

# print(h_list)
print(chokudai_count % (10**9 + 7))