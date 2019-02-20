#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc101/tasks/abc101_a


def main() -> None:
    S = input()
    ans = 0
    for s in S:
        if s == '+':
            ans += 1
        elif s == '-':
            ans -= 1
    print(ans)


if __name__ == '__main__':
    main()
