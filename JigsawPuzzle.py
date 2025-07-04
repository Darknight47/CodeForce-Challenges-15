"""
------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2047/A ----------------------------------

Alyona assembles an unusual square Jigsaw Puzzle. She does so in n days in the following manner:

On the first day, she starts by placing the central piece in the center of the table.
On each day after the first one, she places a certain number of pieces around the central piece in clockwise order, always finishing each square layer completely before starting a new one.
For example, she places the first 14 pieces in the following order:

Alyona is happy if at the end of the day the assembled part of the puzzle does not have any started but unfinished layers. 
Given the number of pieces she assembles on each day, find the number of days Alyona is happy on.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 500). The description of the test cases follows.

The first line contains a single integer n (1 ≤ n ≤ 100), the number of days.

The second line contains n integers a1,a2,…,an (1 ≤ a(i) ≤ 100, a(1)=1), where a(i) is the number of pieces Alyona assembles on the i-th day.

It is guaranteed in each test case that at the end of the n days, there are no unfinished layers.

Output
For each test case, print a single integer: the number of days when Alyona is happy.

Input:
5
1
1
2
1 8
5
1 3 2 1 2
7
1 2 1 10 2 7 2
14
1 10 10 100 1 1 10 1 10 2 10 2 10 1

Output:
1
2
2
2
3
"""
cases = int(input())
for _ in range(cases):
    days = int(input())
    piecesArr = list(map(int, input().split()))
    layer = 1
    layerCapacity = 1
    happyDays = 0

    for pieces in piecesArr:
        while(pieces > 0):
            if(pieces < layerCapacity):
                layerCapacity -= pieces
                pieces = 0
            else:
                pieces -= layerCapacity
                layerCapacity = 0
            
            if(layerCapacity == 0):
                if(pieces == 0):
                    happyDays += 1
                layer += 1
                layerCapacity = 8 * (layer - 1)
    
    print(happyDays)