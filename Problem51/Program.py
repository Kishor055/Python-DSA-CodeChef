def getHashedURL(url, hash_string, k):
    def get_value(c):
        if 'a' <= c <= 'z':
            return ord(c) - ord('a')
        elif c == ':':
            return 26
        elif c == '/':
            return 27
        elif c == '.':
            return 28
        return 0

    n = len(url)
    m = len(hash_string)
    result = []

    for i in range(0, n, k):
        total = 0
        for ch in url[i:i+k]:
            total += get_value(ch)

        index = total % m
        result.append(hash_string[index])

    return ''.join(result)
