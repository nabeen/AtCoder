#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc052/tasks/abc052_a


def main() -> None:
    A, B, C, D = map(int, input().split())
    print(max(A * B, C * D))


if __name__ == '__main__':
    main()
