#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc003/tasks/abc003_3

# N個の動画
# K個見れる
# 初期レート0


def main() -> None:
    N, K = map(int, input().split())
    R = sorted(list(map(int, input().split())))
    rate = 0
    for i in R[-K:]:
        rate = (rate + i) / 2
    print("{:.6f}".format(rate))


if __name__ == '__main__':
    main()
