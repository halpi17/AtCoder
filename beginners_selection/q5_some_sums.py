N, A, B = map(int, input().split())

more_a_under_b_sum = 0
for num in range(1, N+1):
    each_digits_sum = sum(list(map(int, str(num))))
    if each_digits_sum >= A and each_digits_sum <= B:
        more_a_under_b_sum += num

print(more_a_under_b_sum)
