# Chef and Character Frequency Sort

Chef is experimenting with strings!
He wants to rearrange all the characters of a given string `S` in **decreasing order of their frequency**.

If two characters have the same frequency, sort them in **lexicographical (ASCII) order**.

Help Chef by printing the final rearranged string.

## Input Format

* The first and only line contains a string `S`.
* The string consists of uppercase and lowercase English letters and digits.

## Output Format

* Print the rearranged string after sorting by the given rules.

## Constraints

* 1 ≤ |S| ≤ 5 × 10⁵

## Sample Input 1

```
CookBook
```

## Sample Output 1

```
ooookkBC
```

## Sample Input 2

```
aabbbcddd
```

## Sample Output 2

```
bbbdddaac
```

---

## solution.py

Here’s an efficient Python solution using `collections.Counter`:

```python
from collections import Counter

def frequency_sort(s):
    # Count frequency of each character
    freq = Counter(s)
    
    # Sort by (-frequency, character) so that higher frequency comes first,
    # and lexicographical order resolves ties
    sorted_chars = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    
    # Build the final string
    result = ''.join(char * count for char, count in sorted_chars)
    return result

# Read input
S = input().strip()
print(frequency_sort(S))
```

### ✅ How it works:

1. `Counter(s)` counts the occurrences of each character in the string.
2. Sorting key `(-count, char)` ensures:

   * Higher frequency comes first (`-count` for descending).
   * Lexicographical order for ties.
3. Multiply each character by its frequency to rebuild the string.
4. Works efficiently for strings up to length `5 × 10⁵`.

---

**Sample Run 1:**

```
Input:
CookBook
Output:
ooookkBC
```

**Sample Run 2:**

```
Input:
aabbbcddd
Output:
bbbdddaac
```

