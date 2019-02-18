#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc009/tasks/abc009_2

from collections import Counter


def main() -> None:
    x = int(input())
    l = [int(input()) for _ in range(x)]
    i_uniq = sorted(list(set(l)), reverse=True)
    print(i_uniq[1])


if __name__ == '__main__':
    main()
