t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    t -= 1

    # We only need two largest DISTINCT values
    largest = -1
    second = -1

    for x in a:
        if x > largest:
            if x != largest:
                second = largest
            largest = x
        elif x != largest and x > second:
            second = x

    print(largest + second)
