"""
------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1703/A ----------------------------------

There is a string s of length 3, consisting of uppercase and lowercase English letters. Check if it is equal to "YES" (without quotes), where each letter can be in any case. 
For example, "yES", "Yes", "yes" are all allowable.

Input
The first line of the input contains an integer t (1 ≤ t ≤ 10^3) — the number of testcases.

The description of each test consists of one line containing one string s
consisting of three characters. Each character of s is either an uppercase or lowercase English letter.

Output
For each test case, output "YES" (without quotes) if s satisfies the condition, and "NO" (without quotes) otherwise.

You can output "YES" and "NO" in any case (for example, strings "yES", "yes" and "Yes" will be recognized as a positive response).

Input:
10
YES
yES
yes
Yes
YeS
Noo
orZ
yEz
Yas
XES

Output:
YES
YES
YES
YES
YES
NO
NO
NO
NO
NO
"""
cases = int(input())
for _ in range(cases):
    n = input().lower()
    print("YES" if n == 'yes' else "NO")