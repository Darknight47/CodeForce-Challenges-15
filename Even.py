"""
---------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1139/A ----------------------------------------

You are given a string s=s1s2…sn of length n, which only contains digits 1, 2, ..., 9.

A substring s[l…r] of s is a string slsl+1sl+2…sr. 
A substring s[l…r] of s is called even if the number represented by it is even.

Find the number of even substrings of s. 
Note, that even if some substrings are equal as strings, but have different l and r, they are counted as different substrings.

Input
The first line contains an integer n (1 ≤ n ≤ 65000) — the length of the string s.

The second line contains a string s of length n. The string s consists only of digits 1, 2, ..., 9.

Output
Print the number of even substrings of s.

Input:
4
1234

Output:
6
"""
sze = int(input())
s = input()
ans = 0
for i, ch in enumerate(s):
    if ch in '2468':
        ans += i + 1
print(ans)