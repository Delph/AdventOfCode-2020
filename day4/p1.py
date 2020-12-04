#!/usr/bin/python3

with open('input.txt') as f:
  input = f.read().splitlines()

# a valid passport has at least 7 fields, cid is optional
def valid(passport):
  if len(passport.keys()) == 8:
    return True
  if 'cid' not in passport:
    return True

  return False

passports = []
current = {}
for line in input:
  if line == '':
    passports.append(current)
    current = {}
    continue;
  for p in line.split(' '):
    k, v = p.split(':')
    current[k] = v
passports.append(current)

count = 0
for passport in passports:
  if valid(passport):
    count += 1
print(count)
