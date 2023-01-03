N = int( input())
M = int(input())
arr = [True] * N

for i in range(M):
    start, end = map(int, (input().split(' ')))
    for j in range(start, end):
        arr[j] = False

print(len(list(filter(lambda x: x == True, arr))))
