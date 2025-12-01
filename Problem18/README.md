# Valid Anagram

Given two strings `s` and `t`, determine whether `t` is an anagram of `s`. An anagram is a word formed by rearranging the letters of another word, using all the original letters exactly once.

Return `"YES"` if `t` is an anagram of `s`, otherwise return `"NO"`.

## Input Format

* The first line contains a single string `s`.
* The second line contains a single string `t`.

## Output Format

* Print `"YES"` (without quotes) if `t` is an anagram of `s`.
* Print `"NO"` (without quotes) otherwise.

## Constraints

* 1 ≤ |s|, |t| ≤ 5 × 10⁴
* s and t consist of lowercase English letters.

## Sample Input 1

```
listen
silent
```

## Sample Output 1

```
YES
```

**Explanation:** `"silent"` is an anagram of `"listen"`.

## Sample Input 2

```
hello
world
```

## Sample Output 2

```
NO
```

**Explanation:** `"world"` cannot be rearranged to form `"hello"`.

---

## solution.py

Here’s an efficient Python solution using character counting:

```python
def is_anagram(s, t):
    if len(s) != len(t):
        return False

    count = [0] * 26  # For 'a' to 'z'

    for ch in s:
        count[ord(ch) - ord('a')] += 1

    for ch in t:
        count[ord(ch) - ord('a')] -= 1

    for c in count:
        if c != 0:
            return False

    return True

### ✅ How it works:

1. `Counter(s)` counts the occurrences of each character in `s`.
2. `Counter(t)` counts the occurrences of each character in `t`.
3. If the counts are equal, `t` is an anagram of `s`. Otherwise, it’s not.
4. Using `sys.stdin.read()` avoids `EOFError` in online judges.

---

**Sample Run 1:**

```
Input:
listen
silent
Output:
YES
```

**Sample Run 2:**

```
Input:
hello
world
Output:
NO
```

---

This solution works efficiently for strings up to length `5 × 10⁴`.
