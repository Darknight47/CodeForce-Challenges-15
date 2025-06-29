"""
------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1982/A ---------------------------------------

Dima loves watching soccer. In such a game, the score on the scoreboard is represented as x : y, where x is the number of goals of the first team, and y
is the number of goals of the second team. At any given time, only one team can score a goal, so the score x : y
 can change to either (x+1) : y, or x : (y+1).

While watching a soccer game, Dima was distracted by very important matters, and after some time, he returned to watching the game. 
Dima remembers the score right before he was distracted, and the score right after he returned. Given these two scores, he wonders the following question. 
Is it possible that, while Dima was not watching the game, the teams never had an equal score?

It is guaranteed that at neither of the two time points Dima remembers the teams had equal scores. However, it is possible that the score did not change during his absence.

Help Dima and answer the question!

Input
Each test consists of several test cases. The first line contains an integer t (1 ≤ t ≤ 10^4) — the number of test cases. Then follows the description of the test cases.

The first line of each test case contains two integers x1,y1 (0 ≤ x1, y1 ≤ 10^9, x1≠y1) — the score before Dima was distracted.

The second line of each test case contains two integers x2,y2 (x1 ≤ x2 ≤ 10^9, y1 ≤ y2 ≤ 10^9, x2≠y2) — the score when Dima returned.

Output
For each test case, output "YES" without quotes if it is possible, that the teams never had a tie while Dima was away, otherwise output "NO" without quotes.

You can output each letter in any case (for example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as a positive answer).

Input:
6
1 0
5 0
1 2
3 2
1 2
4 5
1 2
4 3
1 2
1 2
998244353 0
1000000000 999999999

Output:
YES
NO
YES
NO
YES
YES
"""
cases = int(input())
for _ in range(cases):
    x, y = map(int, input().split())
    x2, y2 = map(int, input().split())
    if((x < y and x2 > y2) or (x > y and x2 < y2)):
        print("NO")
    else:
        print("YES")