def solve():
    n = int(input())
    s = input()
    alice_score = 0
    bob_score = 0
    server = 'A'

    for winner in s:
        if server == 'A':  # Alice is serving
            if winner == 'A':
                alice_score += 1
            else:
                server = 'B'  # Bob becomes the server
        else:  # Bob is serving
            if winner == 'B':
                bob_score += 1
            else:
                server = 'A'  # Alice becomes the server

    print(alice_score, bob_score)

t = int(input())
for _ in range(t):
    solve()