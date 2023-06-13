# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_cj
# https://github.com/E869120/kyopro-tessoku/tree/main/editorial/chap03
import bisect

N = int(input())
A = list(map(int,input().split()))
Q = int(input())
X = [int(input()) for _ in range(Q)]

A = sorted(A)
# A.sort() でもよかった https://github.com/E869120/kyopro-tessoku/blob/0d4d2e98d4a6f3abe2d59308bb0127c13089043f/editorial/chap03/python/answer_B11.py#LL12C7-L12C7
for i in range(Q):
    print(bisect.bisect_left(A,X[i]))