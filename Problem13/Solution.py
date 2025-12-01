def add_one(num_str):
    num_list = list(num_str)
    i = len(num_list) - 1

    # Add 1 starting from the rightmost digit
    while i >= 0:
        if num_list[i] == '9':
            num_list[i] = '0'
            i -= 1
        else:
            num_list[i] = str(int(num_list[i]) + 1)
            break
    else:
        # If all digits were 9 (e.g., 999 → 1000)
        num_list.insert(0, '1')

    return "".join(num_list)


# Main code for testcases
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = input().strip()
    print(add_one(N))
