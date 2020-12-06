#!/usr/bin/python3

with open('input.txt') as f:
  input = f.read().splitlines()

count = 0
current = {}
for line in input:
  if len(line) == 0:
    count += len(current.keys())
    current = {}
    continue
  for a in line:
    if a not in current:
      current[a] = 0
    current[a] += 1
count += len(current.keys())
print(count)
