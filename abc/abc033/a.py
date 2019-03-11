#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc033/tasks/abc033_a


def main() -> None:
    N = input()
    s = N[0]
    for n in N:
        if s != n:
            print('DIFFERENT')
            exit()
    print('SAME')


if __name__ == '__main__':
    main()
