#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc123/tasks/abc123_b


def main() -> None:
    num = [int(input()) for _ in range(5)]
    ans = 0
    m = [0]
    for i in num:
        if i % 10:
            ans += i + 10 - i % 10
            m.append(10 - i % 10)
        else:
            ans += i
    print(ans - max(m))


if __name__ == '__main__':
    main()
