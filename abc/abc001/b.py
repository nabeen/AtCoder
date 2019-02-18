#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc001/tasks/abc001_2


def main() -> None:
    km = int(input()) / 1000
    vv = ''
    if km < 0.1:
        vv = "00"
    elif km <= 5:
        vv = km * 10
    elif km <= 30:
        vv= km + 50
    elif km <= 70:
        vv = (km - 30) / 5 + 80
    elif km > 70:
        vv = '89'

    print('{:0>2}'.format(str(int(vv))))


if __name__ == '__main__':
    main()
