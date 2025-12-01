# cook your dish here
# Find maximum in an array for each testcase

T = int(input())

for _ in range(T):
    N = int(input())
    mountains = list(map(int, input().split()))
    print(max(mountains))
