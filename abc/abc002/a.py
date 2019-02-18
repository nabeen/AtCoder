#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc002/tasks/abc002_1


def main() -> None:
    x, y = map(int, input().split())
    print("%s" % x if x > y else y)


if __name__ == '__main__':
    main()
