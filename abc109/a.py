#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc109/tasks/abc109_a


def main() -> None:
    A, B = map(int, input().split())
    print("%s" % "No" if (A * B) % 2 == 0 else "Yes")


if __name__ == '__main__':
    main()
