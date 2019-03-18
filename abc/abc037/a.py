#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc037/tasks/abc037_a


def main() -> None:
    A, B, C = map(int, input().split())
    print(C // min(A, B))


if __name__ == '__main__':
    main()
