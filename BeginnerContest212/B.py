X = [int(_) for _ in list(input())]

def check_weak_num(X):
    tmp = X[0]
    for i in range(1, len(X)):
        if X[i] != ((tmp + 1) % 10):
            return False
        tmp = X[i]

    return True

if len(set(X)) == 1 or check_weak_num(X):
    print('Weak')
else:
    print('Strong')
