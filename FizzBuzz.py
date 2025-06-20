"""
----------------------------- Link for the challenge: https://codeforces.com/contest/2070/problem/A ---------------------------

FizzBuzz is one of the most well-known problems from coding interviews. In this problem, we will consider a remixed version of FizzBuzz:

Given an integer n, process all integers from 0 to n. 
For every integer such that its remainders modulo 3 and modulo 5 are the same (so, for every integer i such that i mod 3 = i mod 5), print FizzBuzz.

However, you don't have to solve it. Instead, given the integer n, you have to report how many times the correct solution to that problem will print FizzBuzz.

Input
The first line contains one integer t (1 ≤ t ≤ 10^4) — the number of test cases.

Each test case contains one line consisting of one integer n (0 ≤ n ≤ 10^9).

Output
For each test case, print one integer — the number of times the correct solution will print FizzBuzz with the given value of n.

Input:
7
0
5
15
42
1337
17101997
998244353

Output:
1
3
4
9
270
3420402
199648872
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    full = n // 15
    remaining = n % 15
    count = full * 3 + sum(1 for r in range(1, remaining + 1) if r % 3 == r % 5)
    print(count + 1)