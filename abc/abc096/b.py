#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc096/tasks/abc096_b


def main() -> None:
    A, B, C = map(int, input().split())
    K = int(input())
    m = [A, B, C]
    m.sort(reverse=True)
    ans = m[0] * (2 ** K)
    ans += sum(m[1:])
    print(ans)


if __name__ == '__main__':
    main()
