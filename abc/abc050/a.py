#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc050/tasks/abc050_a


def main() -> None:
    A, op, B = map(str, input().split())
    if op == '+':
        print(int(A) + int(B))
    elif op == '-':
        print(int(A) - int(B))


if __name__ == '__main__':
    main()
