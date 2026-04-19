# 🧩 Parenthesis Checker

## 📌 Problem Statement

Given a string `s` consisting of characters `'('`, `')'`, `'{'`, `'}'`, `'['`, and `']'`, determine whether the expression is **balanced**.

An expression is considered **balanced** if:

* Every opening bracket has a corresponding closing bracket of the same type.
* Brackets are closed in the correct order.

---

## ✅ Examples

| Input        | Output  | Explanation                 |
| ------------ | ------- | --------------------------- |
| `"[{()}]"`   | `True`  | Properly nested and matched |
| `"[()()]{}"` | `True`  | All brackets are valid      |
| `"([]"`      | `False` | Missing closing `)`         |
| `"([{]})"`   | `False` | Incorrect closing order     |

---

## 🚀 Approach

The problem is efficiently solved using a **stack data structure**:

### 🔹 Algorithm Steps:

1. Initialize an empty stack.
2. Traverse each character in the string:

   * If it is an **opening bracket** (`(`, `{`, `[`), push it onto the stack.
   * If it is a **closing bracket** (`)`, `}`, `]`):

     * Check if the stack is empty → return `False`.
     * Pop the top element and check if it matches the corresponding opening bracket.
3. After processing all characters:

   * If the stack is empty → expression is balanced.
   * Otherwise → not balanced.

---

## 💻 Implementation

```python
class Solution:
    def isBalanced(self, s):
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapping.values():  # opening brackets
                stack.append(char)
            else:  # closing brackets
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
        
        return len(stack) == 0
```

---

## ⏱️ Complexity Analysis

* **Time Complexity:** `O(n)`
  Each character is processed once.

* **Space Complexity:** `O(n)`
  In the worst case, all characters are opening brackets.

---

## 🎯 Key Insights

* A **stack** ensures last-opened brackets are matched first (LIFO order).
* Mapping closing → opening brackets simplifies comparison.
* Early termination improves efficiency for invalid cases.

---

## 📦 Constraints

* `1 ≤ s.size() ≤ 10^6`
* String contains only bracket characters.

---

## 🏁 Conclusion

This problem is a classic example of using stacks for **syntax validation**. The approach is efficient, scalable, and widely applicable in parsing tasks like compilers and interpreters.

---
