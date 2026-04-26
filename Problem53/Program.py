def has_pair_with_sum(arr, K):
    arr.sort()
    left, right = 0, len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == K:
            return True
        elif current_sum < K:
            left += 1
        else:
            right -= 1

    return False
