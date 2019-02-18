#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc002/tasks/abc002_2

import re


def main() -> None:
    s = input()
    print("%s" % re.sub("[aiueo]", "", s))


if __name__ == '__main__':
    main()
