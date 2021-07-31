import heapq

Q = int(input())

a = []
sum = 0

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        heapq.heappush(a, query[1] - sum)
    elif query[0] == 2:
        sum += query[1]
    elif query[0] == 3:
        print(heapq.heappop(a) + sum)
