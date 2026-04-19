class Solution:
    def reverseWords(self, s):
        # Step 1: Split by dot
        words = s.split('.')
        
        # Step 2: Remove empty strings
        filtered_words = [word for word in words if word]
        
        # Step 3: Reverse words
        filtered_words.reverse()
        
        # Step 4: Join with single dot
        return '.'.join(filtered_words)