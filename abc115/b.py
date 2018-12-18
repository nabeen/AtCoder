# https://atcoder.jp/contests/abc115/tasks/abc115_b

N = int(input())
S = [int(input()) for _ in range(N)]
S.sort(reverse=True)
S[0] = S[0] / 2
print(int(sum(S)))
