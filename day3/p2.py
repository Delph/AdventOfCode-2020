#!/usr/bin/python3

with open('input.txt') as f:
  input = f.read().splitlines()


def check_slope(x_inc, y_inc):
  x = 0
  y = 0
  target = len(input)
  trees = 0
  while y < target:
    if input[y][x] == '#':
      trees += 1
    x += x_inc
    x %= len(input[0])
    y += y_inc
  return trees

m = 1
for x in range(1, 8, 2):
  m *= check_slope(x, 1)
m *= check_slope(1, 2)
print(m)
