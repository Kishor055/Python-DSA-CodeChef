def solve():
    S = input().strip()
    T = input().strip()
    M = []
    for i in range(5):
        if S[i] == T[i]:
            M.append("G")
        else:
            M.append("B")
    print("".join(M))

t = int(input())
for _ in range(t):
    solve()