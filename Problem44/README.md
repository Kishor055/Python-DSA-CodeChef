# 🔁 Palindrome String

## 📌 Problem Statement

Given a string `s`, determine whether it is a **palindrome**.

A string is called a palindrome if it reads the same **forward and backward**.

---

## ✅ Examples

| Input    | Output  | Explanation                |
| -------- | ------- | -------------------------- |
| `"abba"` | `True`  | Same in both directions    |
| `"abc"`  | `False` | Not the same when reversed |

---

## 🚀 Approach

There are two common ways to solve this problem efficiently:

### 🔹 Method 1: String Reversal (Simple & Pythonic)

* Reverse the string and compare it with the original.
* If both are equal → palindrome.

### 🔹 Method 2: Two-Pointer Technique (Optimal Logic)

* Use two pointers:

  * One starting from the beginning
  * One from the end
* Compare characters while moving inward.
* If any mismatch occurs → not a palindrome.

---

## 💻 Implementation

### ✔️ Method 1: Using Slicing

```python id="pal1"
class Solution:
    def isPalindrome(self, s):
        return s == s[::-1]
```

---

### ✔️ Method 2: Two-Pointer Approach

```python id="pal2"
class Solution:
    def isPalindrome(self, s):
        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        
        return True
```

---

## ⏱️ Complexity Analysis

| Method          | Time Complexity | Space Complexity |
| --------------- | --------------- | ---------------- |
| String Reversal | `O(n)`          | `O(n)`           |
| Two-Pointer     | `O(n)`          | `O(1)`           |

---

## 🎯 Key Insights

* A palindrome is symmetric around its center.
* The **two-pointer approach** is more space-efficient.
* Python slicing provides a quick and readable solution.

---

## 📦 Constraints

* `1 ≤ s.size() ≤ 10^6`
* String contains only lowercase English letters (`a–z`).

---

## 🏁 Conclusion

This is a fundamental string problem that helps build intuition for:

* String traversal
* Symmetry checks
* Efficient comparison techniques

---