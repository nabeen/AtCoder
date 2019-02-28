#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc019/tasks/abc019_1


def main() -> None:
    a, b, c = map(int, input().split())
    l = [a, b, c]
    l.sort()
    print(l[1])


if __name__ == '__main__':
    main()
