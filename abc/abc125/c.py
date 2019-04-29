#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import fractions


def main() -> None:
    N = int(input())
    A = list(map(int, input().split()))

    gcd_l = [0]
    gcd_r = [0]
    for i in range(N):
        gcd_l.append(fractions.gcd(gcd_l[i], A[i]))
        gcd_r.append(fractions.gcd(gcd_r[i], A[-(i + 1)]))
    gcd_r = gcd_r[::-1]

    ans = []
    for i in range(N):
        ans.append(fractions.gcd(gcd_l[i], gcd_r[i + 1]))

    print(max(ans))


if __name__ == '__main__':
    main()
