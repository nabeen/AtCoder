#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc031/tasks/abc031_a


def main() -> None:
    A, D = map(int, input().split())
    print((max(A, D)) * (min(A, D) + 1))


if __name__ == '__main__':
    main()
