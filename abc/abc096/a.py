#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc096/tasks/abc096_a


def main() -> None:
    a, b = map(int, input().split())
    ans = 0
    for i in range(1, 13):
        if a > i:
            ans += 1
        elif a >= i and b >= i:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
