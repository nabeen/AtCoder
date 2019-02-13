#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc112/tasks/abc112_b


def main() -> None:
    N, T = map(int, input().split())
    R = [[int(i) for i in input().split()] for _ in range(N)]
    ROK = [x for x in R if int(x[1]) <= T]
    if ROK:
        ROK.sort(key=lambda x: x[0])
        print(ROK[0][0])
    else:
        print('TLE')


if __name__ == '__main__':
    main()
