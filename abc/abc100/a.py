#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc100/tasks/abc100_a


def main() -> None:
    A, B = map(int, input().split())
    print("Yay!" if f(A, B) else ":(")


def f(A: str, B: str) -> bool:
    if A > 8 or B > 8:
        return False
    else:
        return True


if __name__ == '__main__':
    main()
