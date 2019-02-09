#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/yahoo-procon2019-qual/tasks/yahoo_procon2019_qual_a


def main() -> None:
    x, y = map(int, input().split())
    print("%s" % "YES" if (x + 1) / 2 >= y else "NO")


if __name__ == '__main__':
    main()
