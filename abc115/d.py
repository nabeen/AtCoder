# https://atcoder.jp/contests/abc115/tasks/abc115_d

import re

H, W = map(int, input().split())
L = {0: 'P'}
for i in range(1, H + 1):
    L[i] = 'B' + L[i - 1] + 'P' + L[i - 1] + 'B'
    # del L[i - 1]

print(len(re.findall('P', L[H][-W:])))
