#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc114/tasks/abc114_c
N = int(input())


def main() -> None:
    print(dfs('0'))


def dfs(s: str):
    if int(s) > N:
        return 0
    ret = 1 if all(s.count(c) > 0 for c in '753') else 0
    for c in '753':
        ret += dfs(s + c)
    return ret


if __name__ == '__main__':
    main()
