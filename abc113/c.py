#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc113/tasks/abc113_c


def main() -> None:
    N, M = map(int, input().split())
    PYT = [tuple(map(int, input().split())) for _ in range(M)]
    PYTS = sorted(PYT)

    before = 0
    tmp = {}
    for py in PYTS:
        if before != py[0]:
            # 初期化する
            before = py[0]
            count = 0
        count += 1
        tmp[py] = count

    for py in PYT:
        print("{:06}{:06}".format(py[0], tmp[py]))


if __name__ == '__main__':
    main()
