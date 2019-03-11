#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc035/tasks/abc035_a


def main() -> None:
    W, H = map(int, input().split())
    if W / H == 4 / 3:
        print('4:3')
    else:
        print('16:9')


if __name__ == '__main__':
    main()
