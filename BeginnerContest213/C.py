import numpy as np

H, W, N = map(int, input().split())

AB = [map(int, input().split()) for _ in range(N)]
A, B = [list(i) for i in zip(*AB)]

# H行W列の2次元配列を0で初期化
ABlist = np.zeros((H, W))

# 存在するカードの代入
for i in range(N):
    ABlist[A[i] - 1][B[i] - 1] = i + 1

"""先頭からの削除では範囲外参照を起こすため，末尾からの削除で実装"""
# カードが存在しない行の削除
for h in range(H - 1, -1, -1):
    if all([x == 0 for x in ABlist[h, :]]):
        ABlist = np.delete(ABlist, h, 0)

# カードが存在しない列の削除
for w in range(W - 1, -1, -1):
    if all([y == 0 for y in ABlist[:, w]]):
        ABlist = np.delete(ABlist, w, 1)

# 残ったカードのインデックス検知
result = []
for i in range(len(ABlist[0, :])):
    for j in range(len(ABlist[:, 0])):
        for x in range(len(ABlist[0, :]) * len(ABlist[:, 0])):
            if ABlist[i][j] == (x + 1):
                result.insert((x), [i + 1, j + 1])

for card in result:
    print(card[0], card[1])