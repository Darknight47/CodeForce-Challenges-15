"""
------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1619/B -----------------------------

Polycarp likes squares and cubes of positive integers. Here is the beginning of the sequence of numbers he likes: 1, 4, 8, 9, ....

For a given number n, count the number of integers from 1 to n that Polycarp likes. 
In other words, find the number of such x that x is a square of a positive integer number or a cube of a positive integer number (or both a square and a cube simultaneously).

Input
The first line contains an integer t (1 ≤ t ≤ 20) — the number of test cases.

Then t lines contain the test cases, one per line. Each of the lines contains one integer n (1 ≤ n ≤ 10^9).

Output
For each test case, print the answer you are looking for — the number of integers from 1 to n that Polycarp likes.

Input:
6
10
1
25
1000000000
999999999
500000000

Output:
4
1
6
32591
32590
23125
"""
cases = int(input())
for _ in range(cases):
    num = int(input())
    tempSet = set()
    #maxSquare = int(num ** 0.5)
    idx = 1
    while(idx * idx <= num):
        tempSet.add(idx * idx)
        idx += 1
    idxx = 1
    while(idxx * idxx * idxx <= num):
        tempSet.add(idxx * idxx * idxx)
        idxx += 1

    print(len(tempSet))