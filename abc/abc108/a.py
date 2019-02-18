#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc108/tasks/abc108_a


def main() -> None:
    N = int(input())
    a = N // 2
    b = N // 2 + N % 2
    print(a * b)


if __name__ == '__main__':
    main()
