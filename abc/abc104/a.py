#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc104/tasks/abc104_a

# 0 <= R <= 4208


def main() -> None:
    A = int(input())
    if A < 1200:
        print("ABC")
    elif A < 2800:
        print("ARC")
    else:
        print("AGC")


if __name__ == '__main__':
    main()
