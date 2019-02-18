#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc012/tasks/abc012_2


def main() -> None:
    sec = int(input())
    m, s = divmod(sec, 60)
    h, m = divmod(m, 60)
    if h >= 24:
        # 頭打ち
        print("23:59:59")
    else:
        print("{:0=2}:{:0=2}:{:0=2}".format(h,m,s))


if __name__ == '__main__':
    main()
