#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc019/tasks/abc019_2


def main() -> None:
    s = input()
    tmp = 1
    ans = ""
    for i in range(len(s) - 1):
        if s[i] != s[i+1]:
            ans = ans + s[i] + str(tmp)
            tmp = 1
        else:
            tmp = tmp + 1
    ans = ans + s[-1] + str(tmp)
    print(ans)


if __name__ == '__main__':
    main()
