#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc017/tasks/abc017_2

import re


def main() -> None:
    X = input()
    print(calc(X))


def calc(x: str) -> str:
    x = re.sub("ch", "", x)
    x = re.sub("o", "", x)
    x = re.sub("k", "", x)
    x = re.sub("u", "", x)
    if x == "":
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    main()
