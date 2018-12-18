# https://atcoder.jp/contests/abc115/tasks/abc115_a

line = int(input())
out = ''
for i in range(25 - line):
    out = out + ' Eve'

print('Christmas%s' % out)
