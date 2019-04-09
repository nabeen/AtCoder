#!/usr/bin/env python
# -*- coding: utf-8 -*-
#


def main() -> None:
    N, M, C = map(int, input().split())
    b = tuple(map(int, input().split()))
    l = [tuple(map(int, input().split())) for _ in range(N)]
    # print(b)
    # print(l)
    ans = 0
    for a in l:
        s = 0
        for i in range(len(a)):
            s += a[i] * b[i]
        if s + C > 0:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
