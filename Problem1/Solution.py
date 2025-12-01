# Search an element in an array

# read N and X
N, X = map(int, input().split())

# read array A
A = list(map(int, input().split()))

# check if X is present
if X in A:
    print("YES")
else:
    print("NO")
