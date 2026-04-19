class Solution:
    def isBalanced(self, s):
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapping.values():  # opening brackets
                stack.append(char)
            else:  # closing brackets
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
        
        return len(stack) == 0