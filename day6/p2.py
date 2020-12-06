#!/usr/bin/python3

with open('input.txt') as f:
  input = f.read().splitlines()

count = 0
current = {}
people = 0
for line in input:
  if len(line) == 0:
    count += len([1 for k,v in current.items() if current[k] == people])
    current = {}
    people = 0
    continue
  people += 1
  for a in line:
    if a not in current:
      current[a] = 0
    current[a] += 1
count += len([1 for k,v in current.items() if current[k] == people])
print(count)
