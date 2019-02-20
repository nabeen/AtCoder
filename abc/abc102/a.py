#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc102/tasks/abc102_a


def main() -> None:
    N = int(input())
    if N % 2 == 0:
        print(N)
    else:
        print(N * 2)


if __name__ == '__main__':
    main()
