A, B = map(int, input().split())

C = 0
while True:
    if A ^ C == B:
        print(C)
        break
    C += 1