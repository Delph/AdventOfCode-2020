#!/usr/bin/python3

with open('input.txt') as f:
  input = f.read().splitlines()


x = 0
y = 0
target = len(input)
trees = 0
while y < target:
  if input[y][x] == '#':
    trees += 1
  x += 3
  x %= len(input[0])
  y += 1
print(trees)
