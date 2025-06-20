"""
------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1862/B --------------------------------------

Tema and Vika are playing the following game.

First, Vika comes up with a sequence of positive integers a of length m and writes it down on a piece of paper. Then she takes a new piece of paper and writes down the sequence b

according to the following rule:

First, she writes down a1.
Then, she writes down only those ai (2 ≤ i ≤ m) such that ai−1≤ai. 
Let the length of this sequence be denoted as n.
For example, from the sequence a=[4,3,2,6,3,3], Vika will obtain the sequence b=[4,6,3].

She then gives the piece of paper with the sequence b to Tema. He, in turn, tries to guess the sequence a.

Tema considers winning in such a game highly unlikely, but still wants to find at least one sequence a that could have been originally chosen by Vika. Help him and output any such sequence.

Note that the length of the sequence you output should not exceed the input sequence length by more than two times.

Input
Each test consists of multiple test cases. The first line of input data contains a single integer t (1 ≤ t ≤ 10^4) — the number of test cases. 
This is followed by a description of the test cases.

The first line of each test case contains a single integer n (1 ≤ n ≤ 2⋅10^5) — the length of the sequence b.

The second line of each test case contains n integers b1,b2,b3,…,bn (1 ≤ b(i) ≤ 10^9) — the elements of the sequence.

The sum of the values of n over all test cases does not exceed 2⋅10^5.

Output
For each test case, output two lines. In the first line, output a single integer m— the length of the sequence (n ≤ m ≤ 2⋅n). 
In the second line, output m integers a1,a2,a3,…,am (1 ≤ a(i) ≤ 10^9) — the assumed sequence that Vika could have written on the first piece of paper.

If there are multiple suitable sequences, you can output any of them.

Input:
6
3
4 6 3
3
1 2 3
5
1 7 9 5 7
1
144
2
1 1
5
1 2 2 1 1

Output:
6
4 3 2 6 3 3
3
1 2 3
6
1 7 9 3 5 7
1
144
2
1 1
6
1 2 2 1 1 1
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    arr = list(map(int, input().split()))
    ans = [arr[0]]
    for i in range(1, sze):
        current = arr[i]
        prev = arr[i - 1]
        if(current < prev):
            ans.append(1)
        ans.append(current)
    print(*ans)