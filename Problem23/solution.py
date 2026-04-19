t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    happy_days = 0

    for i in range(n):
        alice = a[i]
        bob = b[i]

        # Conditions:
        # Alice happy if Bob ≤ 2 × Alice
        # Bob happy if Alice ≤ 2 × Bob
        if bob <= 2 * alice and alice <= 2 * bob:
            happy_days += 1

    print(happy_days)

    t -= 1
