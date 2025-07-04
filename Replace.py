"""
----------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1807/C ---------------------------

You are given a string s consisting of lowercase Latin characters. 
In an operation, you can take a character and replace all occurrences of this character with 0 or replace all occurrences of this character with 1.

Is it possible to perform some number of moves so that the resulting string is an alternating binary string†?

For example, consider the string abacaba. You can perform the following moves:

Replace a with 0. Now the string is 0b0c0b0.
Replace b with 1. Now the string is 010c010.
Replace c with 1. Now the string is 0101010.
This is an alternating binary string.
†An alternating binary string is a string of 0s and 1s such that no two adjacent bits are equal. 
For example, 01010101, 101, 1 are alternating binary strings, but 0110, 0a0a0, 10100 are not.

Input
The input consists of multiple test cases. The first line contains an integer t (1 ≤ t ≤ 100) — the number of test cases. The description of the test cases follows.

The first line of each test case contains an integer n (1 ≤ n ≤ 2000) — the length of the string s.

The second line of each test case contains a string consisting of n lowercase Latin characters — the string s.

Output
For each test case, output "YES" (without quotes) if you can make the string into an alternating binary string, and "NO" (without quotes) otherwise.

You can output the answer in any case (for example, the strings "yEs", "yes", "Yes" and "YES" will be recognized as a positive answer).

Input:
8
7
abacaba
2
aa
1
y
4
bkpt
6
ninfia
6
banana
10
codeforces
8
testcase

Output:
YES
NO
YES
YES
NO
YES
NO
NO
"""
def isValid(startValue):
    diction = {}
    for i, ch in enumerate(s):
        expected = (startValue + i) % 2
        if(ch in diction):
            if(diction[ch] != expected):
                return False
        else:
            diction[ch] = expected
    return True

cases = int(input())
for _ in range(cases):
    sze = int(input())
    s = input()
    if(isValid(0) or isValid(1)):
        print("YES")
    else:
        print("NO")
