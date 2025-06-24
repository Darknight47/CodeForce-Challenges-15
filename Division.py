"""
-------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1669/A -------------------------------

Codeforces separates its users into 4 divisions by their rating:

For Division 1: 1900 ≤ rating
For Division 2: 1600 ≤ rating ≤ 1899
For Division 3: 1400 ≤ rating ≤ 1599
For Division 4: rating ≤ 1399

Given a rating, print in which division the rating belongs.

Input
The first line of the input contains an integer t (1 ≤ t ≤ 10^4) — the number of testcases.

The description of each test consists of one line containing one integer rating (−5000 ≤ rating ≤ 5000).

Output
For each test case, output a single line containing the correct division in the format "Division X", 
where X is an integer between 1 and 4 representing the division for the corresponding rating.

Input:
7
-789
1299
1300
1399
1400
1679
2300

Output:
Division 4
Division 4
Division 4
Division 4
Division 3
Division 2
Division 1
"""
cases = int(input())
for _ in range(cases):
    num = int(input())
    if(num >= 1900):
        print("Division 1")
    elif(1600 <= num <= 1899):
        print("Division 2")
    elif(1400 <= num <= 1599):
        print("Division 3")
    else:
        print("Division 4")