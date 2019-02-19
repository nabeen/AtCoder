#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc013/tasks/abc013_1


def main() -> None:
    l = list('ABCDE')
    X = input()
    for v in l:
        if v == X:
            print((l.index(v) + 1))
        else:
            continue


if __name__ == '__main__':
    main()
