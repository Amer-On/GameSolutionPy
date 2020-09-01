# Тот же код с другими переменными, отстутствием комментариев и с вводом через консоль

n, m = map(int, input().split())
w = [list(map(int, input().split()))for i in range(n)]
a = [[0]*m for i in range(n)]
a[0][0] = w[0][0]

for j in range(1, m):
    a[0][j] = a[0][j-1] + w[0][j]
for i in range(1, n):
    a[i][0] = a[i-1][0] + w[i][0]
for i in range(1, n):
    for j in range(1, m):
        if a[i][j-1] >= a[i-1][j]:
            a[i][j] = a[i][j-1] + w[i][j]
        else:
            a[i][j] = a[i-1][j] + w[i][j]

moved = []
x, y = len(a)-1, len(a[-1])-1
while True:
    if x == 0 and y == 0:
        break
    if x > 0 and y > 0:
        if a[x][y-1] <= a[x-1][y] <= a[x][y]:
            x -= 1
            moved.append('D')
        elif a[x-1][y] <= a[x][y-1] <= a[x][y]:
            y -= 1
            moved.append('R')
    else:
        if x == 0:
            y -= 1
            moved.append('R')
        elif y == 0:
            x -= 1
            moved.append('D')


moved = moved[::-1]
print(a[-1][-1])
print(' '.join(moved))
