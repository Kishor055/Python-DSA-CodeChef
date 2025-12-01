t = int(input())
vowels = set("aeiou")

while t > 0:
    s = input().strip()
    
    count = 0
    happy = False
    
    for ch in s:
        if ch in vowels:
            count += 1
            if count > 2:
                happy = True
                break
        else:
            count = 0
    
    if happy:
        print("HAPPY")
    else:
        print("SAD")
    
    t -= 1
