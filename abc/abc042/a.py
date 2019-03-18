#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc042/tasks/abc042_a


def main() -> None:
    A, B, C = map(int, input().split())
    l = [A, B, C]
    l.sort()
    if l[0] == 5 and l[1] == 5 and l[2] == 7:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    main()
