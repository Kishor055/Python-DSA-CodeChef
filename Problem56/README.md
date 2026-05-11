# Palindrome Pairs Detection — Python

A professional and optimized Python solution for solving the **Palindrome Pairs** problem using **Hashing + String Partitioning**.

---

# 📌 Problem Statement

Given an array of strings `arr[]`, determine whether there exists a pair of indices `(i, j)` such that:

* `i ≠ j`
* `arr[i] + arr[j]` forms a palindrome

Return:

* `True` → if such a pair exists
* `False` → otherwise

A palindrome is a string that reads the same forward and backward.

---

# 🚀 Features

✅ Optimized HashSet-based solution
✅ Efficient palindrome checking
✅ Handles edge cases
✅ Interview-ready implementation
✅ Clean and modular code
✅ Time Complexity: `O(n × l²)`
✅ Space Complexity: `O(n × l)`

---

# 📂 Project Structure

```bash
Palindrome-Pairs/
│
├── palindrome_pairs.py     # Main optimized solution
├── brute_force.py          # Brute force approach
├── README.md               # Documentation
└── test_cases.py           # Sample test cases
```

---

# 🧠 Algorithm Explanation

## Optimized Approach

The solution uses:

* HashSet for fast word lookup
* Prefix/Suffix partitioning
* Reverse string matching

For every word:

1. Split the word into prefix and suffix
2. Check:

   * If prefix is palindrome → reverse of suffix exists
   * If suffix is palindrome → reverse of prefix exists

This avoids checking every pair directly.

---

# 📈 Complexity Analysis

## Time Complexity

[
O(n \times l^2)
]

Where:

* `n` = number of strings
* `l` = maximum string length

---

## Space Complexity

[
O(n \times l)
]

---

# 💻 Optimized Python Solution

## `palindrome_pairs.py`

```python
class Solution:

    def is_palindrome(self, s: str) -> bool:
        return s == s[::-1]

    def palindromePairs(self, arr):

        # Store all words for O(1) lookup
        words = set(arr)

        for word in arr:

            length = len(word)

            # Try all partitions
            for i in range(length + 1):

                prefix = word[:i]
                suffix = word[i:]

                # Case 1:
                # Prefix is palindrome
                rev_suffix = suffix[::-1]

                if self.is_palindrome(prefix):
                    if rev_suffix in words and rev_suffix != word:
                        return True

                # Case 2:
                # Suffix is palindrome
                rev_prefix = prefix[::-1]

                if i != length and self.is_palindrome(suffix):
                    if rev_prefix in words and rev_prefix != word:
                        return True

        return False


# Driver Code
if __name__ == "__main__":

    obj = Solution()

    arr1 = ["geekf", "geeks", "or", "keeg", "abc", "bc"]
    print(obj.palindromePairs(arr1))

    arr2 = ["abc", "xyxcba", "geekst", "or", "bc"]
    print(obj.palindromePairs(arr2))

    arr3 = ["aa"]
    print(obj.palindromePairs(arr3))
```

---

# 🐢 Brute Force Approach

## `brute_force.py`

```python
def palindrome_pairs_bruteforce(arr):

    def is_palindrome(s):
        return s == s[::-1]

    n = len(arr)

    for i in range(n):
        for j in range(n):

            if i != j:

                combined = arr[i] + arr[j]

                if is_palindrome(combined):
                    return True

    return False
```

---

# 🧪 Sample Test Cases

## `test_cases.py`

```python
from palindrome_pairs import Solution

obj = Solution()

# Test Case 1
arr1 = ["geekf", "geeks", "or", "keeg", "abc", "bc"]
print(obj.palindromePairs(arr1))
# Output: True

# Test Case 2
arr2 = ["abc", "xyxcba", "geekst", "or", "bc"]
print(obj.palindromePairs(arr2))
# Output: True

# Test Case 3
arr3 = ["aa"]
print(obj.palindromePairs(arr3))
# Output: False
```

---

# ▶️ How to Run

## Step 1 — Clone Repository

```bash
git clone https://github.com/your-username/Palindrome-Pairs.git
```

---

## Step 2 — Navigate to Project Folder

```bash
cd Palindrome-Pairs
```

---

## Step 3 — Run Program

```bash
python palindrome_pairs.py
```

---

# ✅ Example Output

```bash
True
True
False
```

---

# 🔍 Dry Run Example

## Input

```python
arr = ["abc", "cba"]
```

## Process

```python
"abc" + "cba" = "abccba"
```

`"abccba"` is a palindrome.

## Output

```python
True
```

---

# ⚠️ Edge Cases Covered

✔ Single string array
✔ Reverse word existence
✔ Empty prefix/suffix
✔ Duplicate prevention
✔ Large constraints support
✔ Different word lengths

---

# 🏆 Why This Solution is Efficient

| Approach    | Time Complexity |
| ----------- | --------------- |
| Brute Force | O(n² × l)       |
| Optimized   | O(n × l²)       |

The optimized solution significantly reduces unnecessary comparisons.

---

# 🎯 Interview Tips

### Key Observation

A palindrome pair exists when:

* One part of the string is already a palindrome
* The remaining part's reverse exists in the array

This insight enables efficient hashing-based optimization.

---

# 📚 Topics Used

* Hashing
* String Manipulation
* Two-Pointer Palindrome Checking
* Prefix/Suffix Partitioning
* Optimization Techniques

---

# 👨‍💻 Author

Developed using professional Python coding standards for:

* Coding Interviews
* Competitive Programming
* DSA Practice
* Technical Assessments

---

# 📜 License

This project is open-source and available under the MIT License.

---

# ⭐ Support

If you found this project useful:

⭐ Star the repository
🍴 Fork the project
🧠 Practice more DSA problems
🚀 Improve and contribute
