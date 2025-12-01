# Take Discount or Not

## Problem Statement

Chef wants to buy `N` items from a shop. Each item `i` has a price `A[i]`. There is a discount coupon available that costs `X` rupees and reduces the price of every item by `Y` rupees. If an item's price is less than or equal to `Y`, it becomes free (cost = 0).

Determine whether Chef should buy the discount coupon. Chef will buy the coupon **only if the total price with the coupon is strictly less than the total price without the coupon**.

---

## Input Format

* The first line contains an integer `T`, the number of test cases.
* For each test case:

  * The first line contains three integers `N`, `X`, and `Y`.
  * The second line contains `N` space-separated integers `A[1], A[2], ..., A[N]`, representing the prices of the items.

---

## Output Format

For each test case, print:

* `COUPON` if Chef should buy the discount coupon.
* `NO COUPON` otherwise.

> Output is case-insensitive.

---

## Constraints

* (1 \le T \le 1000)
* (1 \le N \le 100)
* (1 \le X, Y \le 10^5)
* (1 \le A[i] \le 10^5)

---

## Sample Input

```
5
4 30 10
15 8 22 6
4 40 10
15 8 22 6
4 34 10
15 8 22 6
2 10 100
60 80
3 30 5
50 60 50
```

## Sample Output

```
COUPON
NO COUPON
NO COUPON
COUPON
NO COUPON
```

---

## Explanation

**Test case 1:**

* Original cost: 15 + 8 + 22 + 6 = 51
* Coupon cost = 30, new item costs after discount: max(15-10,0)+max(8-10,0)+max(22-10,0)+max(6-10,0) = 5 + 0 + 12 + 0 = 17
* Total with coupon = 30 + 17 = 47 < 51 → **COUPON**

**Test case 2:**

* Total with coupon = 40 + 17 = 57 > 51 → **NO COUPON**

**Test case 4:**

* Coupon reduces all items below `Y`, total with coupon = 10 + 0 < 140 → **COUPON**

---

## Approach

1. Calculate the total cost without coupon.
2. Calculate the total cost with coupon:

   * For each item, reduced cost = `max(A[i] - Y, 0)`
   * Total with coupon = sum of reduced costs + X (coupon cost)
3. Compare the two totals:

   * If total with coupon < total without coupon → print `COUPON`
   * Else → print `NO COUPON`

---

## Python Example

```python
T = int(input())
for _ in range(T):
    N, X, Y = map(int, input().split())
    A = list(map(int, input().split()))
    total_without_coupon = sum(A)
    total_with_coupon = X + sum(max(a - Y, 0) for a in A)
    if total_with_coupon < total_without_coupon:
        print("COUPON")
    else:
        print("NO COUPON")
```

