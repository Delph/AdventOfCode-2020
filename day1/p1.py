#!/usr/bin/python3

#with open('test.txt') as f:
with open('input.txt') as f:
  input = f.read().splitlines()

# sort it into order
input = sorted([int(x) for x in input])

for i in input:
  target = 2020 - i
  if target in input:
    print(f'{i} {target} {i * target}')
