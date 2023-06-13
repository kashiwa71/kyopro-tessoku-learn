# p52
# https://atcoder.jp/contests/tessoku-book/tasks/math_and_algorithm_ai


N, Q = map(int, input().split())
A = list(map(int,input().split()))

S = [0]*(N+1)
ans = [0]*(Q)

S[1] = A[0]

for n in range(1,N):
    S[n+1] = S[n] + A[n]

for q in range(Q):
    L, R = map(int,input().split())
    ans[q] = S[R] - S[L-1]

for a in ans:
    print(a)

###############
# 配列のn番目をn日目と扱うように配列の係数を調整する ０番目が1日目となるとわけわからなくなるから

# S[n] + A[n] は以下でも表せる
# 
# B=[0]
# for i in A:
#     B.append(B[-1]+i)
# 
# ref. https://atcoder.jp/contests/tessoku-book/submissions/40603509

# 単に以下の表現でもよい
# s=[0] // 0日目（存在しない。使うのはs[1]以降）
# for i in range(n):
#   s.append(s[i]+a[i])