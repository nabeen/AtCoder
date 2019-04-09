#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc123/tasks/abc123_a


def main() -> None:
    num = [int(input()) for _ in range(5)]
    k = int(input())
    if max(num) - min(num) <= k:
        print('Yay!')
    else:
        print(':(')


if __name__ == '__main__':
    main()
