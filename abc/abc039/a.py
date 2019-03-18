#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc039/tasks/abc039_a


def main() -> None:
    A, B, C = map(int, input().split())
    print(2 * (A * B + B * C + C * A))


if __name__ == '__main__':
    main()
