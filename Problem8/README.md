# Different Consecutive Characters — README.md

## 🧩 Problem: Different Consecutive Characters

Chef has a binary string **S** of length **N**. Chef can perform the following operation on **S**:

Insert any character (**0** or **1**) at any position in **S**.

Find the **minimum number of operations** Chef needs to perform so that **no two consecutive characters are same** in **S**.

---

## 📥 Input Format

* The first line contains a single integer **T** — the number of test cases.
* Then the test cases follow.
* The first line of each test case contains an integer **N** — the length of the binary string **S**.
* The second line of each test case contains a binary string **S** containing **0s and 1s only**.

---

## 📤 Output Format

For each test case, output on a new line the **minimum number of operations** Chef needs to perform so that no two consecutive characters are same in **S**.

---

## 🔢 Constraints

```
1 ≤ T ≤ 100
1 ≤ N ≤ 1000
```

---

## 📘 Sample Input

```
3
2
11
4
0101
5
00100
```

## 📗 Sample Output

```
1
0
2
```

---

## 📝 Explanation (from problem statement)

**Test case 1:**
We can perform:
`11 → 1 0 1` (insert 0 between two 1s)

**Test case 2:**
String `0101` already has alternating characters — no operations needed.

**Test case 3:**
We can perform:
`00100 → 0​1​0100 → 01010​1​0`
Total operations = **2**

---

## 🧠 Approach Summary

* We scan the string from left to right.
* Count how many times **S[i] == S[i+1]**.
* Every such pair requires inserting **one character** to separate them.
* Total count = minimum operations.

This works because insertion always "fixes" exactly one violation.

---

## 🧾 Python Solution (ready to commit)

```python
t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    ops = 0
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            ops += 1

    print(ops)
```

