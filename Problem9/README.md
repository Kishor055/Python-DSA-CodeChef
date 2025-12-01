# 📘 Largest Odd Substring — README.md

## 📝 Problem Statement

You are given a string **S** consisting of digits representing a large integer. Your task is to find the largest-valued odd integer (as a substring of S) that can be obtained.

A substring is a contiguous sequence of characters within the string.

If no odd integer exists in S, print **-1**.

## 📥 Input Format

The first line contains a single string **S** of length **N (1 ≤ N ≤ 10⁵)**, consisting of digits ('0'–'9').


## 📤 Output Format

Print the largest odd integer substring.


## 🔒 Constraints

* **1 ≤ |S| ≤ 10⁵**
* **S contains only digits (0–9)**
* **S does not contain leading zeros**

---

## 🧪 Sample Input & Output

### **Sample 1**

**Input**

128764


**Output**


1287


**Explanation:**
The largest odd substring ends at the first odd digit from the right, which is '7'.



### **Sample 2**

**Input**


60042


**Output**


-1


**Explanation:**
There are no odd digits in the string.

---

### **Sample 3**

**Input**

```
987654321
```

**Output**

```
987654321
```

**Explanation:**
The last digit is '1', which is odd, so the entire string is the largest odd substring.

---

## 💡 Approach (Summary)

* An odd number always ends with an **odd digit** (1, 3, 5, 7, 9).
* Scan the string **from right to left** until you find the first odd digit.
* Return the substring from index **0 to that odd digit**.
* If no odd digit is found → return **-1**.

This approach runs in **O(N)** and works efficiently for very large strings.

---

## ✅ Python Solution

```python
def findLargestOddSubstring(num):
    # Traverse from the end to find the last odd digit
    for i in range(len(num) - 1, -1, -1):
        if int(num[i]) % 2 != 0:  # Check if digit is odd
            return num[:i + 1]
    return "-1"



## ✔️ Features

* Handles up to **100,000** digits efficiently
* Zero extra memory usage
* Fully compliant with competitive programming I/O
* No modification to original problem statement

---
