#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc015/tasks/abc015_2

import math


def main() -> None:
    N = int(input())
    A = list(map(int, input().split()))
    bug_total = 0
    bug_target = 0
    for i in A:
        bug_total = bug_total + i
        bug_target = bug_target + 1 if i != 0 else bug_target
    print(math.ceil(bug_total / bug_target))


if __name__ == '__main__':
    main()
