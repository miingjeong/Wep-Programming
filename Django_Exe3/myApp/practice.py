import sys

N = int(input())
A = []
B = []

for _ in range(N):
    A = list(map(int, stdin.readline().split()))
    B = sorted(A)

    print(B)
    A = []