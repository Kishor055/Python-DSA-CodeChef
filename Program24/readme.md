# **Single Number — README**

## **Problem Description**

You are given a non-empty array of integers `nums`.
Every element in the array appears **exactly twice**, except for **one unique number**, which appears **only once**.

Your task is to **find and return** that unique number.

The solution must satisfy:

* **Time Complexity:** O(n)
* **Space Complexity:** O(1)

---

## **Input Constraints**

* `1 ≤ nums.length ≤ 3 × 10^4`
* `-3 × 10^4 ≤ nums[i] ≤ 3 × 10^4`
* Exactly **one element** appears once, all others appear twice.

---

## **Approach**

The most efficient solution uses the **XOR operation**:

* XOR of a number with itself is **0**
  → `x ^ x = 0`
* XOR of a number with `0` is the number
  → `x ^ 0 = x`
* XOR is **commutative and associative**

Thus, XOR-ing all numbers together cancels out the duplicates, leaving the unique number.

---

## **Sample Input & Output**

### **Sample 1**

**Input**

```
3
1
10
5
```

**Output**

```
3
```

### **Sample 2**

**Input**

```
9 1 9 2 1
```

**Output**

```
2
```

### **Sample 3**

**Input**

```
7 3 5 3 7
```

**Output**

```
5
```

### **Sample 4**

**Input**

```
10
```

**Output**

```
10
```

---

## **Solution Code (Python)**

```python
class Solution:
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result ^= num
        return result
```

---

If you want, I can also give you the **full solution.py**, formatted for your platform.
