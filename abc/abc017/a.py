#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc017/tasks/abc017_1


def main() -> None:
    S1, E1 = map(int, input().split())
    S2, E2 = map(int, input().split())
    S3, E3 = map(int, input().split())
    print(int(S1 * E1 / 10 + S2 * E2 / 10 + S3 * E3 / 10))


if __name__ == '__main__':
    main()
