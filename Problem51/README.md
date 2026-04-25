# 🔗 URL Hashing Algorithm

A lightweight and efficient custom URL hashing algorithm that converts a given URL into a compact hash string using block-based processing and character mapping.

---

## 🚀 Problem Statement

Given:

* A **URL string**
* A **hash string** (used for mapping)
* An integer **k** (block size)

### Task:

1. Divide the URL into blocks of size `k` (left to right)
2. Convert each character into a numeric value:

   * `'a' → 0`, `'b' → 1`, ..., `'z' → 25`
   * `':' → 26`
   * `'/' → 27`
   * `'.' → 28`
3. Compute the sum of values for each block
4. Map the sum using:

   ```
   index = sum % len(hash_string)
   ```
5. Append `hash_string[index]` to the result
6. Return the final hashed string

---

## 🧠 Example

### Input:

```
url = "https://xyz.com"
hash_string = "pqrst"
k = 4
```

### Processing:

Blocks:

```
http | s:// | xyz. | com
```

### Computation:

```
60 % 5 = 0 → p
98 % 5 = 3 → s
100 % 5 = 0 → p
28 % 5 = 3 → s
```

### Output:

```
psps
```

---

## ⚙️ Approach

* Traverse the URL in chunks of size `k`
* Convert each character using defined mapping
* Compute block sum efficiently
* Use modulo operation to map into hash string

---

## ⏱️ Time Complexity

```
O(n)
```

* Single pass through the URL string

---

## 🧩 Edge Cases Handled

* Last block smaller than `k`
* Special characters (`:`, `/`, `.`)
* Large input size (up to 10⁵)

---

## 💻 Implementation (Python)

```python
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
```

---

## 🧪 Sample Test

```python
url = "https://caayxdycdzwxwac.com"
hash_string = "awpixaia"
k = 7

print(getHashedURL(url, hash_string, k))
```

### Output:

```
iawp
```

---

## 📌 Key Takeaways

* Demonstrates **string manipulation + hashing logic**
* Efficient and scalable approach
* Can be extended to:

  * URL shortening systems
  * Custom encoding mechanisms
  * Lightweight hashing utilities

---

## 🔮 Future Improvements

* Add unit testing (pytest / unittest)
* Extend support for more characters
* Convert to other languages (C++, Java)
* Build a full **URL shortener system** using this logic

---

## 👨‍💻 Author

**Kishor Kakde Patil**
Electronics & Communication Engineering
AI | ML | Cloud Enthusiast 🚀
