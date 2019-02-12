#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc006/tasks/abc006_2


def main() -> None:
    n = int(input())
    tr = [0, 0, 1]
    s = 0 if n != 3 else 1
    for i in range(3, n):
        s = tr[0] + tr[1] + tr[2]
        tr = tr[1:]
        tr.append(s % 10007)

    print(s % 10007)


if __name__ == '__main__':
    main()
