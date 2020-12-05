#!/usr/bin/python3

with open('input.txt') as f:
  input = f.read().splitlines()


ids = []
for p in input:
  c_min = 0
  c_max = 127
  for c in p[:7]:
    if c == 'F':
      c_max = c_min + (c_max - c_min) // 2
    elif c == 'B':
      c_min = c_min + (c_max - c_min) // 2 + 1

  r_min = 0
  r_max = 7
  for r in p[7:]:
    if r == 'L':
      r_max = r_min + (r_max - r_min) // 2
    elif r == 'R':
      r_min = r_min + (r_max - r_min) // 2 + 1

  ids.append(c_min * 8 + r_min)

ids.sort()
prev = -1
for id in ids:
  # it's not going to be the first id, so just skip it
  if prev == -1:
    prev = id
    continue
  if prev+2 == id:
    print(prev+1)
    break
  prev = id

