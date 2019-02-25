#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc002/tasks/abc002_3

# 底辺*高さ/2
# A[x][y]
# B[x][y]
# C[x][y]

def main() -> None:
    pos = list(map(int, input().split()))
    a = pos[2] - pos[0]
    b = pos[3] - pos[1]
    c = pos[4] - pos[0]
    d = pos[5] - pos[1]
    print(abs(a * d - b * c) / 2)


if __name__ == '__main__':
    main()
