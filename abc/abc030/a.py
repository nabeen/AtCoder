#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc030/tasks/abc030_a


def main() -> None:
    A, B, C, D = map(int, input().split())
    if A / B == C / D:
        print('DRAW')
    elif A / B >= C / D:
        print('AOKI')
    elif A / B <= C / D:
        print('TAKAHASHI')


if __name__ == '__main__':
    main()
