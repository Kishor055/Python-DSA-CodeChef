# 🔁 Reverse Words in a String (Dot Separated)

## 📌 Problem Statement

Given a string `s` where words are separated by dots (`.`), reverse the order of the words **without reversing the individual words**.

### ⚠️ Important Notes:

* The string may contain:

  * Leading dots
  * Trailing dots
  * Multiple dots between words
* The output must:

  * Contain only **valid words**
  * Use a **single dot (`.`)** as a separator
  * Have **no leading or trailing dots**

---

## ✅ Examples

| Input                             | Output                            | Explanation         |
| --------------------------------- | --------------------------------- | ------------------- |
| `"i.like.this.program.very.much"` | `"much.very.program.this.like.i"` | Words reversed      |
| `"..geeks..for.geeks."`           | `"geeks.for.geeks"`               | Extra dots removed  |
| `"..home....."`                   | `"home"`                          | Single word cleaned |

---

## 🚀 Approach

### 🔹 Key Idea:

1. Split the string using `.` as delimiter.
2. Remove empty strings caused by extra dots.
3. Reverse the list of valid words.
4. Join them using a single dot (`.`).

---

## 💻 Implementation

### ✔️ Python Solution

```python id="revwords1"
class Solution:
    def reverseWords(self, s):
        # Step 1: Split by dot
        words = s.split('.')
        
        # Step 2: Remove empty strings
        filtered_words = [word for word in words if word]
        
        # Step 3: Reverse words
        filtered_words.reverse()
        
        # Step 4: Join with single dot
        return '.'.join(filtered_words)
```

---

## ⏱️ Complexity Analysis

* **Time Complexity:** `O(n)`
  Each character is processed once.

* **Space Complexity:** `O(n)`
  For storing words after splitting.

---

## 🎯 Key Insights

* Splitting directly may introduce **empty strings** due to multiple dots.
* Filtering is crucial to ensure correct formatting.
* The problem is more about **string parsing and cleanup** than just reversing.

---

## 📦 Constraints

* `1 ≤ s.length() ≤ 10^6`
* String contains:

  * Lowercase English letters (`a–z`)
  * Dot (`.`) as separator

---

## 🏁 Conclusion

This problem reinforces:

* String manipulation techniques
* Handling edge cases (extra delimiters)
* Clean and efficient data transformation

---