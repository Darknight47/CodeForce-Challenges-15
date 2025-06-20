"""
-------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2060/A --------------------------------

There is an array of 5 integers. Initially, you only know a1,a2,a4,a5. 
You may set a3 to any positive integer, negative integer, or zero. The Fibonacciness of the array is the number of integers i (1 ≤ i ≤ 3) such that ai+2=ai+ai+1. 
Find the maximum Fibonacciness over all integer values of a3.

Input
The first line contains an integer t (1 ≤ t ≤ 500) — the number of test cases.

The only line of each test case contains four integers a1,a2,a4,a5 (1 ≤ai ≤ 100).

Output
For each test case, output the maximum Fibonacciness on a new line.

Input:
6
1 1 3 5
1 3 2 1
8 10 28 100
100 1 100 1
1 100 1 100
100 100 100 100

Output:
3
2
2
1
1
2
"""
cases = int(input())
for _ in range(cases):
    a1, a2, a4, a5 = map(int, input().split())
    candidates = [
        a1 + a2, 
        a4 - a2,
        a5 - a4,
        0
    ]
    ans = 0

    for a3 in candidates:
        score = 0
        if(a3 == a1 + a2):
            score += 1
        if(a4 == a2 + a3):
            score += 1
        if(a5 == a3 + a4):
            score += 1
        ans = max(ans, score)
    
    print(ans)