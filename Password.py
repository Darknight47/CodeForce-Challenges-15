"""
----------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/770/A ------------------------------------

Innokentiy decides to change the password in the social net "Contact!", but he is too lazy to invent a new password by himself. That is why he needs your help.

Innokentiy decides that new password should satisfy the following conditions:

the length of the password must be equal to n,
the password should consist only of lowercase Latin letters,
the number of distinct symbols in the password must be equal to k,
any two consecutive symbols in the password must be distinct.
Your task is to help Innokentiy and to invent a new password which will satisfy all given conditions.

Input
The first line contains two positive integers n and k (2 ≤ n ≤ 100, 2 ≤ k ≤ min(n, 26)) — the length of the password and the number of distinct symbols in it.

Pay attention that a desired new password always exists.

Output
Print any password which satisfies all conditions given by Innokentiy.

Input:
4 3

Output:
java
"""
import string
import random

n, k = map(int, input().split())
characters = string.ascii_lowercase[:k]

password = list(characters)
random.shuffle(password)

while len(password) < n:
    lastChar = password[-1]
    choices = [c for c in characters if c != lastChar]
    nextChar = random.choice(choices)
    password.append(nextChar)
print(''.join(password))