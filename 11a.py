# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_k

N, X = map(int,input().split())
A = list(map(int,input().split()))
# A = [0] + A


# def search(N,X,A) -> int:
#     L = 1
#     R = N

#     while (L <= R):
#         M = (L+R)//2

#         if A[M] < X: 
#             L = M+1
#         elif A[M] == X:
#             return M
#         elif X < A[M]:
#             R = M-1

# print(search(N,X,A))

import bisect
print(bisect.bisect(A,X))

# https://docs.python.org/ja/3.8/library/bisect.html
# bisect_left() と似ていますが、 a に含まれる x のうち、どのエントリーよりも後ろ(右)にくるような挿入点を返します。
# 
# X = 47
# A = 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67
#     0  1  2  3  4  5  6  7  8  9  10^
#  -> 挿入店は11だから11を返す