#!/usr/bin/python3

with open('input.txt') as f:
  input = list(map(int, f.read().splitlines()))

PREMABLE_LENGTH = 25

idx = PREMABLE_LENGTH
while idx < len(input):
  section = input[idx - PREMABLE_LENGTH:idx]

  target = input[idx]
  found = False
  for i, j in enumerate(section):
    if target - j in section[i+1:]:
      idx += 1
      found = True
      break
  if not found:
    print(target)
    break
