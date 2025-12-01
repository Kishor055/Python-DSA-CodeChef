def reverse_words(s: str) -> str:
    # Trim leading and trailing spaces
    s = s.strip()
    
    # Split by one or more spaces
    words = s.split()
    
    # Reverse words and join with single space
    return ' '.join(reversed(words))
