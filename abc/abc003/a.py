#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc003/tasks/abc003_1


def main() -> None:
    s = int(input())
    num = 0
    for i in range(1, s + 1):
        num = num + i
    print("%s" % str(int(num/s*10000)))


if __name__ == '__main__':
    main()
