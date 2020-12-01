#!/usr/bin/python3

#with open('test.txt') as f:
with open('input.txt') as f:
  input = f.read().splitlines()

# sort it into order
input = sorted([int(x) for x in input])

for i in input:
  for j in input:
    if i == j:
      continue
    target = 2020 - i - j
    if target in input:
      print(f'{i} {j} {target} {i * j * target}')
