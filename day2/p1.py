#!/usr/bin/python3

import re

with open('input.txt') as f:
  input = f.read().splitlines()

# 1-3 a: abcde
r = re.compile(r'(\d+)-(\d+) ([a-z]): ([a-z]+)')

count = 0
for entry in input:
  m = r.match(entry)
  if m is None:
    print(entry)
    break
  c = m.group(4).count(m.group(3))
  if c >= int(m.group(1)) and c <= int(m.group(2)):
    count += 1
print(count)
