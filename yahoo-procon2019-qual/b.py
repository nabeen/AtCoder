#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/yahoo-procon2019-qual/tasks/yahoo_procon2019_qual_b


def main() -> None:
    r = (str(input()) + " " + str(input()) + " " + str(input())).split()
    pos = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
    }
    for i in r:
        pos[int(i)] += 1

    num = 0
    for i in pos.values():
        if i >= 2:
            num = num + 1

    print("%s" % "YES" if num >= 2 else "NO")


if __name__ == '__main__':
    main()
