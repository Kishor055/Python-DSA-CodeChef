# cook your dish here
# Number of test cases
T = int(input())

for _ in range(T):
    S = input().strip()
    words = S.split()  # Split the string into words
    result = []

    for word in words:
        if word.isupper():  # Check if word is an acronym
            result.append(word)
        else:
            # Capitalize first letter and lowercase the rest
            result.append(word.capitalize())

    # Join words back into a single string
    print(" ".join(result))
