#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc099/tasks/abc099_a

# 1 <= N <= 1998


def main() -> None:
    N = int(input())
    print(f(N))


def f(N: int) -> str:
    s = ""
    if N < 1000:
        s = "ABC"
    else:
        s = "ABD"

    return s



if __name__ == '__main__':
    main()
