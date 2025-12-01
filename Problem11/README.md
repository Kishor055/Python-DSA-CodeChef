# World Chess Championship Prize Calculator

## Description

This project calculates the prize money received by Carlsen in a World Chess Championship based on the outcomes of 14 classical games. Each game can be won by Carlsen, won by Chef, or end in a draw. The prize distribution is determined according to the championship rules.

* Winner of a game: 2 points
* Loser of a game: 0 points
* Draw: 1 point for each player

At the end of 14 games:

* Player with more points wins: 60% of the total prize pool
* Loser: 40% of the total prize pool
* If points are tied: Carlsen (defending champion) wins with 55% of the prize, and Chef gets 45%.

## Input

1. Number of test cases `T`.
2. For each test case:

   * An integer `X` denoting the total prize pool factor (total prize = 100 × X).
   * A string of length 14 consisting of characters `C`, `N`, `D` representing the outcomes of the games.

## Output

For each test case, print the total prize money won by Carlsen.

## Constraints

* 1 ≤ T ≤ 1000
* 1 ≤ X ≤ 10^6
* Each result string `S` has length 14 and contains only `C`, `N`, `D`.

## Example

**Input:**

```
4
100
CCCCCCCCCCCCCC
400
CDCDCDCDCDCDCD
30
DDCCNNDDDCCNND
1
NNDNNDDDNNDNDN
```

**Output:**

```
6000
24000
1650
40
```

## How It Works

1. Count points for Carlsen and Chef based on the match results.
2. Determine the prize according to who has more points or if there is a tie.
3. Output Carlsen’s prize for each test case.

## Explanation

**Test case 1:**  
Since Carlsen won all the games, he will be crowned the champion and will get  
`60 ⋅ X = 60 ⋅ 100 = 6000`

**Test case 2:**  
Carlsen won 7 games and drew 7, so his score is  
`2 ⋅ 7 + 1 ⋅ 7 = 21`  
Chef lost 7 games and drew 7, so his score is  
`0 ⋅ 7 + 1 ⋅ 7 = 7`  
Since Carlsen has more points, he will be crowned the champion and will get  
`60 ⋅ X = 60 ⋅ 400 = 24000`

**Test case 3:**  
Carlsen and Chef both end up with 14 points.  
So, Carlsen is declared the winner, but because the points were tied, he receives  
`55 ⋅ X = 55 ⋅ 30 = 1650`

**Test case 4:**  
Chef has more points, so Carlsen loses.  
Carlsen gets `40 ⋅ X = 40 ⋅ 1 = 40`

---
