# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_l
N,K = map(int,input().split())
A = list(map(int,input().split()))

def count(x):
    sum = 0
    for i in range(N):
        sum += x // A[i] 
    return sum

Left = 1
Right = 10**9

while Left<Right:
    Mid = (Left+Right)//2
    
    res = count(Mid)
    
    if res < K: # 小さすぎる
        Left = Mid + 1
    
    else: # 大きすぎる
        Right = Mid

print(Left)



# これはダメ
# N,K = map(int,input().split())
# A = list(map(int,input().split()))
 
 
# def count(x):
#     sum = 0
#     for i in range(N):
#         sum += x // A[i] 
#     return sum
 
# Left = 1
# Right = 10**9
 
# while Left < Right:
#     Mid = (Left+Right)//2
    
#     res = count(Mid)
    
#     if res > K:
#         Right = Mid
 
#     else:
#         Left = Mid + 1
    
#     # print(f'mid:{mid} l:{l} r:{r} res:{res}')
 
# print(Left)
 