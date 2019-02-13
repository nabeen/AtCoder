#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc111/tasks/abc111_a


def main() -> None:
    n = input()
    out = ""
    for v in n:
        if v == '9':
            out += "1"
        elif v == '1':
            out += "9"
    print(out)


if __name__ == '__main__':
    main()
