class Solution:

    def is_palindrome(self, s: str) -> bool:
        return s == s[::-1]

    def palindromePairs(self, arr):

        # Store all words for O(1) lookup
        words = set(arr)

        for word in arr:

            length = len(word)

            # Try all partitions
            for i in range(length + 1):

                prefix = word[:i]
                suffix = word[i:]

                # Case 1:
                # Prefix is palindrome
                rev_suffix = suffix[::-1]

                if self.is_palindrome(prefix):
                    if rev_suffix in words and rev_suffix != word:
                        return True

                # Case 2:
                # Suffix is palindrome
                rev_prefix = prefix[::-1]

                if i != length and self.is_palindrome(suffix):
                    if rev_prefix in words and rev_prefix != word:
                        return True

        return False


# Driver Code
if __name__ == "__main__":

    obj = Solution()

    arr1 = ["geekf", "geeks", "or", "keeg", "abc", "bc"]
    print(obj.palindromePairs(arr1))

    arr2 = ["abc", "xyxcba", "geekst", "or", "bc"]
    print(obj.palindromePairs(arr2))

    arr3 = ["aa"]
    print(obj.palindromePairs(arr3))
