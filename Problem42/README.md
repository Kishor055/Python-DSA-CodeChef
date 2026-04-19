# 🔄 Reverse a String

## 📌 Problem Statement

Given a string `s`, reverse the string and return the result.

---

## ✅ Examples

| Input     | Output    |
| --------- | --------- |
| `"Geeks"` | `"skeeG"` |
| `"for"`   | `"rof"`   |
| `"a"`     | `"a"`     |

---

## 🚀 Approach

Reversing a string is a fundamental operation that can be achieved in multiple ways. The most efficient and concise method in Python is using **slicing**.

### 🔹 Method 1: Using String Slicing (Recommended)

* Python provides a built-in slicing feature to reverse sequences.
* Syntax: `s[::-1]`

### 🔹 Method 2: Using Two Pointers

* Convert the string into a list (since strings are immutable).
* Swap characters from both ends moving toward the center.
* Convert back to string.

---

## 💻 Implementation

### ✔️ Method 1: Slicing

```python id="rev1"
class Solution:
    def reverseString(self, s):
        return s[::-1]
```

---

### ✔️ Method 2: Two-Pointer Approach

```python id="rev2"
class Solution:
    def reverseString(self, s):
        s_list = list(s)
        left, right = 0, len(s_list) - 1
        
        while left < right:
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1
        
        return ''.join(s_list)
```

---

## ⏱️ Complexity Analysis

| Method      | Time Complexity | Space Complexity |
| ----------- | --------------- | ---------------- |
| Slicing     | `O(n)`          | `O(n)`           |
| Two-pointer | `O(n)`          | `O(n)`           |

---

## 🎯 Key Insights

* Strings in Python are **immutable**, so any modification creates a new string.
* Slicing is the **most concise and Pythonic** approach.
* The two-pointer method demonstrates in-place logic (useful in other languages).

---

## 📦 Constraints

* `1 ≤ s.size() ≤ 10^6`
* String contains only alphabetic characters (uppercase and lowercase).

---

## 🏁 Conclusion

Reversing a string is a simple yet essential problem that introduces key concepts like:

* String manipulation
* Two-pointer techniques
* Efficient use of built-in features

---