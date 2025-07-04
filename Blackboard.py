"""
------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2123/A --------------------------------

Initially, the integers from 0 to n−1 are written on a blackboard.

In one round,
Alice chooses an integer a on the blackboard and erases it;
then Bob chooses an integer b on the blackboard such that a + b ≡ 3 (mod4)∗ and erases it.
Rounds take place in succession until a player is unable to make a move — the first player who is unable to make a move loses. Determine who wins with optimal play.

∗ We define that x≡y(modm) whenever x−y is an integer multiple of m.

Input
The first line contains an integer t (1 ≤ t ≤ 100)  — the number of test cases.

The only line of each test case contains an integer n (1 ≤ n ≤ 100) — the number of integers written on the blackboard.

Output
For each test case, output on a single line "Alice" if Alice wins with optimal play, and "Bob" if Bob wins with optimal play.

You can output the answer in any case (upper or lower). For example, the strings "aLiCe", "alice", "ALICE", and "alICE" will be recognized as "Alice".

Input:
5
2
4
5
7
100

Output:
Alice
Bob
Alice
Alice
Bob
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    if(n % 4 == 0):
        print("BOB")
    else:
        print("ALICE")