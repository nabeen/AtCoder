#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc104/tasks/abc104_b

import re


def main() -> None:
    print("AC" if re.search("^A[a-z]+C([a-z]*)[a-z]$", input()) else "WA")


if __name__ == '__main__':
    main()
