#!/usr/bin/python3

with open('input.txt') as f:
  input = f.read().splitlines()


x = 0
y = 0
f = 'E'
d = ['E', 'S', 'W', 'N']

for instruction in input:
  c = instruction[0]
  m = int(instruction[1:])

  if c == 'R':
    f = d[(d.index(f) + m // 90) % 4]
  if c == 'L':
    f = d[(d.index(f) - m // 90 + 4) % 4]
  if c == 'F':
    if f == 'E':
      x += m
    elif f == 'W':
      x -= m
    elif f == 'N':
      y += m
    elif f == 'S':
      y -= m
  if c == 'N':
    y += m
  if c == 'E':
    x += m
  if c == 'S':
    y -= m
  if c == 'W':
    x -= m
print(x, y)
print(abs(x)+abs(y))
