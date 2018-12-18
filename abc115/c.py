# https://atcoder.jp/contests/abc115/tasks/abc115_c

H, W = map(int, input().split())
S = [int(input()) for _ in range(H)]
S.sort()
res = None
for i in range(len(S) - W + 1):
    sdiff = S[i + W - 1] - S[i]
    if res is None:
        res = sdiff
    if res > sdiff:
        res = sdiff

print(res)
