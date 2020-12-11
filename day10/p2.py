#!/usr/bin/python3

import functools

with open('input.txt') as f:
#with open('test.txt') as f:
  input = f.read().splitlines()


adapters = sorted(map(int, input))
target = adapters[-1] + 3

@functools.lru_cache
def arrangement(jolts, target):
  count = 0
  for i in range(1, 4):
    if jolts + i in adapters:
      if adapters[-1] == jolts + i:
        return count + 1
      count += arrangement(jolts + i, target)
  return count

print(arrangement(0, target))
