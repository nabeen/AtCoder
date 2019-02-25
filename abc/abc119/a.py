#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc119/tasks/abc119_a


def main() -> None:
    S = input()
    Y, M, D = S.split("/")
    if int(Y) >= 2019 and int(M) <= 4:
        print("Heisei")
    else:
        print("TBD")


if __name__ == '__main__':
    main()
