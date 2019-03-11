#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc028/tasks/abc028_a


def main() -> None:
    N = int(input())
    if N <= 59:
        print('Bad')
    elif N <= 89:
        print('Good')
    elif N <= 99:
        print('Great')
    else:
        print('Perfect')


if __name__ == '__main__':
    main()
