#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc014/tasks/abc014_1


def main() -> None:
    a = int(input())
    b = int(input())
    print(b - (a % b) if a % b != 0 else 0)


if __name__ == '__main__':
    main()
