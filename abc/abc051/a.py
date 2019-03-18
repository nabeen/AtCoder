#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc051/tasks/abc051_a

import re


def main() -> None:
    s = input()
    print(re.sub(',', ' ', s))


if __name__ == '__main__':
    main()
