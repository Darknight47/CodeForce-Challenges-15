"""
-------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1714/C ---------------------------

Find the minimum number with the given sum of digits s such that all digits in it are distinct (i.e. all digits are unique).

For example, if s=20, then the answer is 389. 
This is the minimum number in which all digits are different and the sum of the digits is 20 (3+8+9=20).

For the given s print the required number.

Input
The first line contains an integer t (1 ≤ t ≤ 45) — the number of test cases.

Each test case is specified by a line that contains the only integer s (1 ≤ s ≤ 45).

Output
Print t integers — the answers to the given test cases.

Input:
4
20
8
45
10

Output:
389
8
123456789
19
"""
cases = int(input())
for _ in range(cases):
    num = int(input())
    ans = []
    for dig in range(9, 0, -1):
        if(num >= dig):
            ans.append(dig)
            num -= dig
    print(int(''.join(map(str, sorted(ans)))))