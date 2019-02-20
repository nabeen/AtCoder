#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc103/tasks/abc103_a


def main() -> None:
    l = list(map(int, input().split()))
    ls = sorted(l, reverse=True)
    ans = 0
    for i in range(len(ls) - 1):
        ans = ans + abs(ls[i] - ls[i+1])

    print(ans)


if __name__ == '__main__':
    main()
