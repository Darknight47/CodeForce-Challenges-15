"""
------------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/2001/B ------------------------------------

There is an integer sequence a of length n, where each element is initially −1.

Misuki has two typewriters where the first one writes letters from left to right, with a pointer initially pointing to 1, 
and another writes letters from right to left with a pointer initially pointing to n.

Misuki would choose one of the typewriters and use it to perform the following operations until a becomes a permutation of [1,2,…,n]

write number: write the minimum positive integer that isn't present in the array a to the element a(i), i is the position where the pointer points at. Such operation can be performed only when ai=−1.
carriage return: return the pointer to its initial position (i.e. 1 for the first typewriter, n for the second)
move pointer: move the pointer to the next position, let i be the position the pointer points at before this operation, 
if Misuki is using the first typewriter, i:=i+1 would happen, and i:=i−1 otherwise. Such operation can be performed only if after the operation, 1 ≤ i ≤ n holds.
Your task is to construct any permutation p of length n, 
such that the minimum number of carriage return operations needed to make a=p is the same no matter which typewriter Misuki is using.

Input
Each test contains multiple test cases. The first line of input contains a single integer t (1 ≤ t ≤ 500) — the number of test cases. The description of the test cases follows.

The first line of each test case contains a single integer n (1 ≤ n ≤ 2⋅10^5) — the length of the permutation.

It is guaranteed that the sum of n over all test cases does not exceed 2⋅10^5.

Output
For each test case, output a line of n integers, representing the permutation p of length n such that the minimum number of carriage return operations needed to make a=p is 
the same no matter which typewriter Misuki is using, or −1 if it is impossible to do so.

If there are multiple valid permutations, you can output any of them.

Input:
3
1
2
3

Output:
1
-1
3 1 2
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    if(n % 2 == 0):
        print(-1)
    else:
        print(1, end= ' ')
        i = 2
        while(i <= n):
            if(i + 1 <= n):
                print(i + 1, i, end=' ')
                i += 2
            else:
                print(i, end= ' ')
                break
        print()