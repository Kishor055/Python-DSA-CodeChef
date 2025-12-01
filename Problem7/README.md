## 📝 Problem Statement

Wordle
Chef invented a modified wordle.

There is a hidden word **S** and a guess word **T**, both of length **5**.

Chef defines a string **M** to determine the correctness of the guess word. For the
**i<sup>th</sup>** index:

* If the guess at the **i<sup>th</sup>** index is correct, the **i<sup>th</sup>** character of **M** is **G**.
* If the guess at the **i<sup>th</sup>** index is wrong, the **i<sup>th</sup>** character of **M** is **B**.

Given the hidden word **S** and guess **T**, determine string **M**.

---

## 📥 Input Format

* First line will contain **T**, number of test cases. Then the test cases follow.
* Each test case contains two lines of input.
* First line contains the string **S** – the hidden word.
* Second line contains the string **T** – the guess word.

---

## 📤 Output Format

For each test case, print the value of string **M**.

You may print each character of the string in uppercase or lowercase
(for example, the strings **BgBgB**, **BGBGB**, **bgbGB**, and **bgbgb** will all be treated as identical).

---

## 🔒 Constraints

```
1 ≤ T ≤ 1000
|S| = |T| = 5
S, T contain uppercase English alphabets only.
```

---

## 🧪 Sample 1

### **Input**

```
3
ABCDE
EDCBA
ROUND
RINGS
START
STUNT
```

### **Output**

```
BBGBB
GBBBB
GGBBG
```

---

## 🧠 Explanation

### Test Case 1:

S = ABCDE and T = EDCBA. The string M is:

* A ≠ E → M[1] = B
* B ≠ D → M[2] = B
* C = C → M[3] = G
* D ≠ B → M[4] = B
* E ≠ A → M[5] = B

Thus, **M = BBGBB**

---

### Test Case 2:

S = ROUND and T = RINGS. The string M is:

* R = R → M[1] = G
* O ≠ I → M[2] = B
* U ≠ N → M[3] = B
* N ≠ G → M[4] = B
* D ≠ S → M[5] = B

Thus, **M = GBBBB**

---

## ✅ Python Solution (full, final, error-free)

```python
def solve():
    t = int(input())
    for _ in range(t):
        S = input().strip()
        T = input().strip()

        M = []
        for i in range(5):
            if S[i] == T[i]:
                M.append("G")
            else:
                M.append("B")

        print("".join(M))
```
---