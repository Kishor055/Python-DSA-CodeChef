# 📘 Remove Outermost Parentheses — Python Solution

This folder contains the Python solution for the **“Remove Outermost Parentheses”** problem, a common question in Data Structures & Algorithms and competitive programming (e.g., CodeChef, LeetCode).

The task is to process a valid parentheses string, break it into primitive components, and **remove the outermost parentheses** from each primitive segment.

---

## 🔍 Problem Summary

A **valid parentheses string**:

* contains only `(` and `)`
* is properly balanced
* can be decomposed into **primitive parentheses strings**

A **primitive** parentheses string is a valid string that **cannot** be split into two smaller valid parentheses strings.

### 🎯 Objective

For every primitive part inside string `s`, **remove its first and last parenthesis**.

---

## 📥 Input Format

* First line: integer `T` — number of test cases
* Next `T` lines: each containing a valid parentheses string `s`

### Constraints

```
1 ≤ T ≤ 100
1 ≤ |s| ≤ 100000
s contains only '(' and ')'
Total characters across testcases ≤ 1,000,000
```

---

## 📤 Output Format

For each test case, print the modified string after removing the outermost parentheses of each primitive part.

---

## 🧠 Approach (Efficient & Safe)

We maintain a **balance counter**:

* When encountering `'('`:

  * if `balance > 0`, it is **not outermost**, so include it
  * then increase balance

* When encountering `')'`:

  * decrease balance first
  * if `balance > 0`, include it

This ensures we skip the outermost parentheses of each primitive block.

Time Complexity → **O(n)**
Space Complexity → **O(n)**
Handles large inputs safely and avoids `EOFError`.

---

## 🧩 Example

### **Input**

```
4
((()))
(()(()))
()()
((())())(()(()))
```

### **Output**

```
(())
()( )
 
(())()(()(()))
```

---

## 🧾 Python Implementation (Final, Error-Free)

> This version **avoids all EOF issues** by using `sys.stdin.read()` — recommended for CodeChef.

```python
def remove_outer_parentheses(s):
    result = []
    balance = 0

    for ch in s:
        if ch == '(':
            if balance > 0:
                result.append(ch)
            balance += 1
        else:  # ch == ')'
            balance -= 1
            if balance > 0:
                result.append(ch)

    return "".join(result)


def main():
    import sys
    data = sys.stdin.read().strip().split()

    t = int(data[0])
    index = 1
    outputs = []

    for _ in range(t):
        s = data[index]
        index += 1
        outputs.append(remove_outer_parentheses(s))

    print("\n".join(outputs))


if __name__ == "__main__":
    main()
```

---

## ✔ Features

* ⚡ **Optimized** — O(n) per test case
* 🔒 **No Runtime / SIGHUP / EOF errors**
* 📚 **Competitive-programming friendly**
* 🧼 Clean, readable, maintainable code
* 🧪 Handles maximum constraints safely
---