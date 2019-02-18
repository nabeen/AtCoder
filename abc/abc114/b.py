#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc114/tasks/abc114_b


def main() -> None:
    v = str(input())
    m = int(v)
    base = 753
    for i in range(len(v) - 2):
        res = abs(base - int(v[i:i+3]))
        m = res if m > res else m

    print(m)


if __name__ == '__main__':
    main()
