"""
-------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2094/B -----------------------------------

In Bobritto Bandito's home town of residence, there are an infinite number of houses on an infinite number line, with houses at …,−2,−1,0,1,2,…. 
On day 0, he started a plague by giving an infection to the unfortunate residents of house 0. 
Each succeeding day, the plague spreads to exactly one healthy household that is next to an infected household. 
It can be shown that each day the infected houses form a continuous segment.

Let the segment starting at the l-th house and ending at the r-th house be denoted as [l,r]. 
You know that after n days, the segment [l,r] became infected. 
Find any such segment [l′,r′] that could have been infected on the m-th day (m ≤ n).

Input
The first line contains an integer t (1 ≤ t ≤ 100) – the number of independent test cases.

The only line of each test case contains four integers n, m, l, and r (1 ≤ m ≤ n ≤ 2000, −n ≤ l ≤ 0 ≤ r ≤ n, r −l = n).

Output
For each test case, output two integers l′ and r′ on a new line. If there are multiple solutions, output any.

Input:
4
4 2 -2 2
4 1 0 4
3 3 -1 2
9 8 -6 3

Output:
-1 1
0 1
-1 2
-5 3
"""
cases = int(input())
for _ in range(cases):
    n, m, l, r = map(int, input().split())
    x, y = l, r
    remaining = n - m

    while remaining > 0:
        if(abs(x) > 0):
            x -= 1 if x > 0 else -1
        elif(abs(y) > 0):
            y -= 1 if y > 0 else -1
        else:
            x -= 1
        remaining -= 1
    
    print(x, y)