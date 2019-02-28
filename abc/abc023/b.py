#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc023/tasks/abc023_b


def main() -> None:
    N = int(input())
    S = input()
    acs = 'b'
    if N == 1 and S == 'b':
        print('0')
        exit()

    for i in range(1, 101):
        if i % 3 == 1:
            acs = 'a' + acs + 'c'
        elif i % 3 == 2:
            acs = 'c' + acs + 'a'
        elif i % 3 == 0:
            acs = 'b' + acs + 'b'

        if acs == S:
            print(i)
            exit()

    print('-1')


if __name__ == '__main__':
    main()
