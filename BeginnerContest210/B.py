N = int(input())
S = input()

takahashi = 1

for card in S:
    if takahashi == 1 and card == '1':
        print('Takahashi')
        break
    elif takahashi == -1 and card == '1':
        print('Aoki')
        break
    takahashi *= -1