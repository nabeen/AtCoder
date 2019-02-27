#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc015/tasks/abc015_1


def main() -> None:
    A = input()
    B = input()
    print(calc(A, B))


def calc(a: str, b: str) -> str:
    if len(a) > len(b):
        return a
    else:
        return b


if __name__ == '__main__':
    main()
