from palindrome_pairs import Solution

obj = Solution()

# Test Case 1
arr1 = ["geekf", "geeks", "or", "keeg", "abc", "bc"]
print(obj.palindromePairs(arr1))
# Output: True

# Test Case 2
arr2 = ["abc", "xyxcba", "geekst", "or", "bc"]
print(obj.palindromePairs(arr2))
# Output: True

# Test Case 3
arr3 = ["aa"]
print(obj.palindromePairs(arr3))
# Output: False
