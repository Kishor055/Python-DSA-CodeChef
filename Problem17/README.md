# Rotate String

You are given two strings S and G of equal length. Determine whether string S can be transformed into string G by performing a series of left-shifts.

A left-shift operation moves the first character of a string to the end of the string. For example, a left-shift on "abcde" results in "bcdea".

If it is possible to transform S into G using zero or more left-shifts, print "Yes". Otherwise, print "No".

## Input Format

The first line contains a string `S`.
The second line contains a string `G`.

## Output Format

Print `"Yes"` if `S` can be rotated to become `G`, otherwise print `"No"`.

## Constraints

* 1 ≤ length of S, G ≤ 100
* S and G consist of lowercase English letters.

## Sample Input 1

```
hello
ohell
```

## Sample Output 1

```
Yes
```

**Explanation:**
"hello" left-shifted 4 times becomes "ohell", so the answer is "Yes".

## Sample Input 2

```
world
dlrow
```

## Sample Output 2

```
No
```

**Explanation:**
No sequence of left-shifts can transform "world" into "dlrow".

