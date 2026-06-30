#code Chef
import math
t = int(input())
for _ in range(t):
    l, b = map(int, input().split())
    gcd = math.gcd(l, b)
    squares = (l // gcd) * (b // gcd)
    print(squares)


#2
t = int(input())

for _ in range(t):
    d, n = map(int, input().split())
    for i in range(d):
        n = n * (n + 1) // 2
    print(n)

#3
t = int(input())
for _ in range(t):
    balls, boxes = map(int, input().split())
    if balls >= boxes:
        print(balls - boxes)
    else:
        print(0)

  #4
t = int(input())
for _ in range(t):
    n = int(input())

    if n % 10 == 0:
        print(0)
    elif n % 2 == 0:
        print(1)
    else:
        print(-1)

#5
t = int(input())

for _ in range(t):
    n = int(input())

    print(1, n - 1)
