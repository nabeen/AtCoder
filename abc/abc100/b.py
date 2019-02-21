#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc100/tasks/abc100_b

# Dは0,1,2のいずれかである
# Nは1以上100以下の整数
# 100でちょうどD回割りきれる正の整数の中でN番目に小さいものを出力しなさい.
# D N


def main() -> None:
    D, N = map(int, input().split())
    if N != 100:
        print(100 ** D * N)
    else:
        print(100 ** D * 101)


if __name__ == '__main__':
    main()
