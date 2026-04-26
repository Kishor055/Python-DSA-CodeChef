# 📈 Best Time to Buy and Sell Stock

## 🧩 Problem Statement

You are given an array `prices[]` where `prices[i]` represents the price of a stock on the `i-th` day.

You are allowed to complete **at most one transaction** (i.e., buy once and sell once).

Your task is to find the **maximum profit** possible. If no profit is possible, return `0`.

---

## 📥 Input

* An integer array `prices[]`

---

## 📤 Output

* Maximum profit achievable with one buy-sell transaction
* Return `0` if no profit is possible

---

## 📌 Constraints

* You must buy before you sell
* Only one transaction is allowed

---

## 📊 Examples

### Example 1

```
Input: prices = [7, 1, 5, 3, 6, 4]
Output: 5
Explanation: Buy at 1 and sell at 6 → profit = 5
```

---

### Example 2

```
Input: prices = [7, 6, 4, 3, 1]
Output: 0
Explanation: No profitable transaction possible
```

---

## 🚀 Approaches

---

## 1️⃣ Brute Force Approach

### 💡 Idea

Check all possible buy-sell pairs.

### ⏱ Complexity

* Time: **O(n²)**
* Space: **O(1)**

### 💻 Code (Python)

```python id="bf_stock"
def max_profit(prices):
    n = len(prices)
    max_profit = 0

    for i in range(n):
        for j in range(i + 1, n):
            max_profit = max(max_profit, prices[j] - prices[i])

    return max_profit
```

---

## 2️⃣ Optimal Approach (One Pass)

### 💡 Idea

Track the **minimum price so far** and compute maximum profit at each step.

### 🧠 Key Insight

Instead of checking all pairs, we maintain:

* Lowest buying price
* Maximum profit so far

---

### ⏱ Complexity

* Time: **O(n)**
* Space: **O(1)**

---

### 💻 Code (Python)

```python id="opt_stock"
def max_profit(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)

    return max_profit
```

---

## 📊 Complexity Comparison

| Approach         | Time Complexity | Space Complexity | Efficiency |
| ---------------- | --------------- | ---------------- | ---------- |
| Brute Force      | O(n²)           | O(1)             | ❌ Slow     |
| Optimal (Greedy) | O(n)            | O(1)             | ✅ Best     |

---

## 🧠 Key Idea

* Always track the **minimum buying price**
* At each day, calculate potential profit
* Update maximum profit dynamically

---

## 🏁 Conclusion

This problem is a classic example of a **Greedy Algorithm optimization problem**, widely used in coding interviews.

It teaches:

* Subarray optimization
* Greedy decision making
* Real-time profit tracking

---

