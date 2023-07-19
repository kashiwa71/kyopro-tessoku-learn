# Q: https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ck
# A: https://github.com/E869120/kyopro-tessoku/blob/main/editorial/chap03/python/answer_B12.py
# cf: https://github.com/E869120/kyopro-tessoku/blob/main/editorial/chap03/chap03.pdf

N = int(input())

# 最初の自分の回答
# Left = 1
# Right = 100000
# n = 0
# x = 0 
# while abs(n - N)> 0.001:
#     if n < N:
#         Left = x + 1
#     else:
#         Right = x

#     x = (Left+Right)//2 # kirisute
#     n = x + x**3

Left = 0
Right = 100 # ★高々100

for i in range(20): # 100/2**20 = 0.000095 < 0.001：xを20回割ればこの誤差に落ち着く 
    Mid = (Left + Right) / 2 # 整数絡むから普通に割る
    val = Mid + Mid**3
    print('L:{}\tR:{}\tval:{}'.format(Left,Right,val))
    if val > N:
        Right = Mid
    else:
        Left = Mid

print(Mid)
