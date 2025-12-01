def is_anagram(s, t):
    if len(s) != len(t):
        return False

    count = [0] * 26  # For 'a' to 'z'

    for ch in s:
        count[ord(ch) - ord('a')] += 1

    for ch in t:
        count[ord(ch) - ord('a')] -= 1

    for c in count:
        if c != 0:
            return False

    return True