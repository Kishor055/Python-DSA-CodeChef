# 🔤 Anagram Checker

## 📌 Problem Statement

Given two non-empty strings `s1` and `s2`, determine whether they are **anagrams** of each other.

Two strings are considered anagrams if:

* They contain the **same characters**
* Each character appears with the **same frequency**
* The order of characters does **not matter**

---

## ✅ Examples

| Input                     | Output  | Explanation                   |
| ------------------------- | ------- | ----------------------------- |
| `"geeks"`, `"kseeg"`      | `True`  | Same characters and frequency |
| `"allergy"`, `"allergyy"` | `False` | Extra `'y'` in second string  |
| `"listen"`, `"lists"`     | `False` | Missing/extra characters      |

---

## 🚀 Approach

### 🔹 Method 1: Sorting

* Sort both strings.
* If sorted versions are equal → anagrams.

### 🔹 Method 2: Frequency Count (Optimal)

* Count occurrences of each character.
* Compare frequency maps.

---

## 💻 Implementation

### ✔️ Method 1: Sorting

```python id="ana1"
class Solution:
    def areAnagrams(self, s1, s2):
        return sorted(s1) == sorted(s2)
```

---

### ✔️ Method 2: Using Frequency Count (Dictionary)

```python id="ana2"
class Solution:
    def areAnagrams(self, s1, s2):
        if len(s1) != len(s2):
            return False
        
        freq = {}
        
        for char in s1:
            freq[char] = freq.get(char, 0) + 1
        
        for char in s2:
            if char not in freq or freq[char] == 0:
                return False
            freq[char] -= 1
        
        return True
```

---

### ✔️ Method 3: Using Fixed-Size Array (Most Efficient)

```python id="ana3"
class Solution:
    def areAnagrams(self, s1, s2):
        if len(s1) != len(s2):
            return False
        
        count = [0] * 26
        
        for i in range(len(s1)):
            count[ord(s1[i]) - ord('a')] += 1
            count[ord(s2[i]) - ord('a')] -= 1
        
        return all(c == 0 for c in count)
```

---

## ⏱️ Complexity Analysis

| Method           | Time Complexity | Space Complexity |
| ---------------- | --------------- | ---------------- |
| Sorting          | `O(n log n)`    | `O(1)` / `O(n)`  |
| Dictionary Count | `O(n)`          | `O(n)`           |
| Array Count      | `O(n)`          | `O(1)`           |

---

## 🎯 Key Insights

* Anagrams depend entirely on **character frequency**, not order.
* Sorting is simple but not optimal.
* Frequency counting provides **linear time performance**.
* Fixed-size arrays are the most efficient when dealing with limited character sets.

---

## 📦 Constraints

* `1 ≤ s1.size(), s2.size() ≤ 10^5`
* Strings contain only lowercase English letters (`a–z`).

---

## 🏁 Conclusion

The anagram problem is a classic example of:

* Hashing / frequency counting
* Efficient string comparison
* Optimization trade-offs between simplicity and performance

---