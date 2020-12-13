#!/usr/bin/python3

with open('input.txt') as f:
  input = f.read().splitlines()


wx = 10
wy = 1
x = 0
y = 0
d = ['E', 'S', 'W', 'N']

for instruction in input:
  c = instruction[0]
  m = int(instruction[1:])

  if c == 'R':
    r = m // 90
    for _ in range(r):
      t = wy
      wy = -wx
      wx = t
  if c == 'L':
    l = m // 90
    for _ in range(l):
      t = wy
      wy = wx
      wx = -t
  if c == 'F':
    x += wx * m
    y += wy * m
  if c == 'N':
    wy += m
  if c == 'E':
    wx += m
  if c == 'S':
    wy -= m
  if c == 'W':
    wx -= m
print(x, y)
print(abs(x)+abs(y))
