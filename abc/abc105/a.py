#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc105/tasks/abc105_a


def main() -> None:
    A, B = map(int, input().split())
    print('0' if A % B == 0 else 1)


if __name__ == '__main__':
    main()
