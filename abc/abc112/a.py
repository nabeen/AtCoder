#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc112/tasks/abc112_a


def main() -> None:
    n = int(input())
    if n == 1:
        print("Hello World")
    elif n == 2:
        print("%s" % (int(input()) + int(input())))


if __name__ == '__main__':
    main()
