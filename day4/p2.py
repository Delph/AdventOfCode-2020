#!/usr/bin/python3

with open('input.txt') as f:
  input = f.read().splitlines()

def valid(passport):
  if 'byr' not in passport:
    return False
  if int(passport['byr']) < 1920 or int(passport['byr']) > 2002:
    return False

  if 'iyr' not in passport:
    return False
  if int(passport['iyr']) < 2010 or int(passport['iyr']) > 2020:
    return False

  if 'eyr' not in passport:
    return False
  if int(passport['eyr']) < 2020 or int(passport['eyr']) > 2030:
    return False

  if 'hgt' not in passport:
    return False
  height = passport['hgt']
  if height[-2:] == 'cm':
    cm = int(height[:-2])
    if cm < 150 or cm > 193:
      return False
  elif height[-2:] == 'in':
    inches = int(height[:-2])
    if inches < 59 or inches > 76:
      return False
  else:
    return False

  if 'hcl' not in passport:
    return False
  hcol = passport['hcl']
  if hcol[0] != '#':
    return False
  for i in range(6):
    if hcol[1+i] not in '0123456789abcdef':
      return False

  if 'ecl' not in passport:
    return False
  ecol = passport['ecl']
  if ecol not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
    return False

  if 'pid' not in passport:
    return False
  if len(passport['pid']) != 9:
    return False
  try:
    int(passport['pid'])
  except:
    return False

  return True

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
