## README.md

Convert String to Title Case

This folder contains the solution for the problem Convert String to Title Case.
The objective is to format each given string so that every word follows proper title case rules, with an exception for acronyms.

Problem Description

You are given a string S that contains English letters and spaces. You must convert it into title case. In title case, the first letter of each word is uppercase and the remaining letters are lowercase. However, if a word is entirely in uppercase (an acronym), that word should remain unchanged.

A word is defined as a sequence of English letters separated by single spaces.
The input contains no leading, trailing, or multiple spaces between words.

Acronym Rule
If a word contains only uppercase letters A to Z, it must remain unchanged.

Input Format

The first line contains an integer T, the number of test cases.
Each of the next T lines contains a string S.

Output Format

For each test case, print the converted title case string.

Constraints

1 ≤ T ≤ 100
1 ≤ |S| ≤ 1000

Examples

Input:
5
hello world
this is a CODECHEF problem
WELCOME to the JUNGLE
the quick BROWN fOx
programming in PYTHON

Output:
Hello World
This Is A CODECHEF Problem
WELCOME To The JUNGLE
The Quick BROWN Fox
Programming In PYTHON

Explanation
In the first test case, each word is capitalized as they are not acronyms.
In the second test case, "CODECHEF" is an acronym and remains in uppercase.
In the third test case, "WELCOME" and "JUNGLE" are considered acronyms.
In the fourth test case, "BROWN" is an acronym, while the rest of the words follow the title case rule.
In the fifth test case, "PYTHON" is an acronym, and the rest of the string is converted to title case.

Approach

1. Split the string into words.
2. For each word:
   a. If all letters are uppercase, keep it unchanged.
   b. Otherwise, convert the first character to uppercase and the rest to lowercase.
3. Join all processed words with a single space.
4. Output the final result for every test case.

This approach ensures correct handling of normal words and acronyms while meeting all problem constraints.

