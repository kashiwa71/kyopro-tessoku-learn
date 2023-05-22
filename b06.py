# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ce

N = int(input())
A = list(map(int,input().split()))
Q = int(input())
L = []
R = []

for _ in range(Q):
    l, r = map(int,input().split())
    L.append(l)
    R.append(r)

Win =  [0]*(N+1)
Lose = [0]*(N+1)

for i in range(N):
    Win[i+1] = Win[i]
    Lose[i+1] = Lose[i]

    if A[i] == 1:
        Win[i+1] += 1
    else:
        Lose[i+1] += 1

# print(Win)
# print(Lose)

for q in range(Q):
    w =  Win[ R[q] ] -  Win[ L[q] -1 ]
    l = Lose[ R[q] ] - Lose[ L[q] -1 ]

    if w>l:
        print('win')
    elif w==l:
        print('draw')
    else:
        print('lose')