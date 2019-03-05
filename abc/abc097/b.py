#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc097/tasks/abc097_b


def main() -> None:
    X = int(input())
    ans = 0
    for i in range(1, X + 1):
        for j in range(2, X + 1):
            if i ** j > X:
                break
            elif ans < i ** j:
                ans = i ** j
    print(ans if X != 1 else 1)


if __name__ == '__main__':
    main()
