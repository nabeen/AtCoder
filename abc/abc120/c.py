#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc120/tasks/abc120_c

import collections


def main() -> None:
    S = list(input())
    a = collections.Counter(S)
    zero = a['0']
    one = a['1']
    if zero >= one:
        print(one * 2)
    else:
        print(zero * 2)


if __name__ == '__main__':
    main()
