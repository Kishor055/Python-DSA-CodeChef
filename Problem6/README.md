# 📘 Reverse Words in a String — README.md

This folder contains the Python solution for the **“Reverse Words in a String”** problem, commonly asked in DSA practice and competitive programming platforms.

The goal is to reverse the order of words in a given string while handling extra spaces correctly.

---

## 📝 Problem Statement (Unchanged)

You are given a string S consisting of English letters (uppercase and lowercase), digits, and spaces ' '. The string may contain leading or trailing spaces, or multiple spaces between words.

Your task is to reverse the order of the words in the string. A word is defined as a sequence of non-space characters.

The resulting string should:

* Contain words in reversed order.
* Have only single spaces separating words.
* Not contain leading or trailing spaces.

### **Input Format**

The first line of input contains a single string S.

S may contain spaces at the beginning, the end, or multiple consecutive spaces.

### **Output Format**

Print a single line containing the words of S in reversed order, separated by a single space, with no leading or trailing spaces.

### **Constraints**

```
1 ≤ |S| ≤ 10^4
S contains English letters (both uppercase and lowercase), digits, and spaces ' '.
There is at least one word in S.
```

### **Sample 1**

**Input**

```
OpenAI   creates amazing   AI   models  
```

**Output**

```
models AI amazing creates OpenAI
```

### **Sample 2**

**Input**

```
Data   Science is fun
```

**Output**

```
fun is Science Data
```

---

## 🧠 Approach

* Split the string using `.split()`
  → This removes extra spaces and keeps only valid words.
* Reverse the list of words.
* Join them using a **single space**.
* Ensure no leading or trailing spaces appear in the output.

This method is optimal and handles all edge cases.

---

## ✅ Python Solution (`solution.py`)

```python
def reverse_words(s):
    words = s.split()           # Split by whitespace, removes extra spaces
    reversed_words = words[::-1]
    return " ".join(reversed_words)

def main():
    s = input()
    print(reverse_words(s))

if __name__ == "__main__":
    main()
```

---

## ✔ Features

* Handles large strings efficiently (up to 10⁴ characters).
* Automatically removes extra, leading, and trailing spaces.
* Produces clean, competitive-programming-friendly output.
* Works exactly as required in the problem statement.

---
