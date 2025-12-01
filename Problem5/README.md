# 📘 DNA Storage — README.md

A clean and well-documented explanation of the **DNA Storage Encoding Problem**, commonly found in competitive programming and DSA practice.

---

## 🧬 Problem Overview

You are given a **binary string of even length** and must encode it into a DNA-style string using the following mapping:

| Binary Pair | Encoded As |
| ----------- | ---------- |
| `00`        | **A**      |
| `01`        | **T**      |
| `10`        | **C**      |
| `11`        | **G**      |

The conversion is done **left to right**, taking **two characters at a time**.

---

## 🔍 Input Format

* First line contains integer `T` → number of test cases.
* For each test case:

  * Integer `N` → length of string (N is even)
  * Binary string `S` of length `N`

---

## 📤 Output Format

For each test case, print the encoded DNA sequence on a new line.

---

## 🧾 Constraints

* `1 ≤ T ≤ 100`
* `2 ≤ N ≤ 10³`
* `N` is always even
* Sum of all N across testcases ≤ `1000`
* String `S` contains only `'0'` and `'1'`
* Output is **case-sensitive**

---

## 🧪 Sample Input

```
4
2
00
4
0011
6
101010
4
1001
```

## ✅ Sample Output

```
A
AG
CCC
CT
```

---

## 🧠 Explanation

* `00 → A`
* `11 → G`
* `10 → C`
* `01 → T`

Example walkthrough:

* `0011` → `00 → A`, `11 → G` → **AG**
* `101010` → `10, 10, 10` → **CCC**
* `1001` → `10 → C`, `01 → T` → **CT**

---

## 🧩 Python Solution

This solution follows the competitive-programming style and handles all constraints efficiently.

```python
t = int(input())

while t > 0:
    n = int(input())
    s = input().strip()

    result = []

    for i in range(0, n, 2):
        pair = s[i:i+2]

        if pair == "00":
            result.append("A")
        elif pair == "01":
            result.append("T")
        elif pair == "10":
            result.append("C")
        else:  # "11"
            result.append("G")

    print("".join(result))

    t -= 1
```

---

## ✔ Features of This Implementation

* Works efficiently within all input limits
* Clean, readable, beginner-friendly
* Exactly follows the mapping rules
* Perfect for DSA notes or GitHub code repositories
