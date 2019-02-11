#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc004/tasks/abc004_2


def main() -> None:
    x = [
        input().split(),
        input().split(),
        input().split(),
        input().split(),
    ]
    x.reverse()
    for i in x:
        i.reverse()
    for j in x:
        print(' '.join(j))


if __name__ == '__main__':
    main()
