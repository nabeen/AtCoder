#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc096/tasks/abc096_c


def main() -> None:
    H, W = map(int, input().split())
    s = ['0' + input() + '0' for _ in range(H)]
    s.insert(0, '0' * (W + 2))
    s.append('0' * (W + 2))
    for i in range(1, H + 1):
        for j in range(1, W + 1):
            # print(s[i][j])
            if s[i][j] == "#":
                if s[i+1][j] == "#" or s[i-1][j] == "#" or s[i][j+1] == "#" or s[i][j-1] == "#":
                    continue
                else:
                    print("No")
                    exit()
    print("Yes")


if __name__ == '__main__':
    main()
