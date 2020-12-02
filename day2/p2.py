#!/usr/bin/python3

import re

with open('input.txt') as f:
  input = f.read().splitlines()

# 1-3 a: abcde
r = re.compile(r'(\d+)-(\d+) ([a-z]): ([a-z]+)')

count = 0
for entry in input:
  m = r.match(entry)

  password = m.group(4)
  if (password[int(m.group(1))-1] == m.group(3)) != (password[int(m.group(2))-1] == m.group(3)):
    count += 1
print(count)
