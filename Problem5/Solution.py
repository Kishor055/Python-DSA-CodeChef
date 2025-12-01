t = int(input())

while t > 0:
    n = int(input())
    s = input().strip()

    dna = []                      # to store encoded characters
    for i in range(0, n, 2):      # take 2 characters at a time
        pair = s[i:i+2]

        if pair == "00":
            dna.append("A")
        elif pair == "01":
            dna.append("T")
        elif pair == "10":
            dna.append("C")
        else:                     # "11"
            dna.append("G")

    print("".join(dna))
    t -= 1
