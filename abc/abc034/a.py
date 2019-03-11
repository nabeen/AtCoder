#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc034/tasks/abc034_a


def main() -> None:
    x, y = map(int, input().split())
    if x < y:
        print('Better')
    else:
        print('Worse')


if __name__ == '__main__':
    main()
