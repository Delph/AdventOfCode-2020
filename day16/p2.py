#!/usr/bin/python3

with open('input.txt') as f:
#with open('test.txt') as f:
  input = f.read().splitlines()


fields = {}

my_ticket = []
other_tickets = []

stage = 0
for line in input:
  if line == '':
    stage += 1
    continue
  if line == 'your ticket:' or line == 'nearby tickets:':
    continue

  if stage == 0:
    field, ranges = line.split(': ')
    range0, range1 = ranges.split(' or ')
    fields[field] = [list(map(int, range0.split('-'))), list(map(int, range1.split('-')))]
  if stage == 1:
    my_ticket = list(map(int, line.split(',')))
  if stage == 2:
    other_tickets.append(list(map(int, line.split(','))))


def valid_field(value):
  for r0, r1 in fields.values():
    if value >= r0[0] and value <= r0[1]:
      return True
    if value >= r1[0] and value <= r1[1]:
      return True

  return False


def valid_range(value, r0, r1):
  if value >= r0[0] and value <= r0[1]:
    return True
  if value >= r1[0] and value <= r1[1]:
    return True

  return False


def valid(ticket):
  return sum([1 if valid_field(v) else 0 for v in ticket]) == len(ticket)

valid_tickets = [t for t in other_tickets if valid(t)]

mapping = {}

# for each field, find what column it's valid on for every ticket
while len(mapping.values()) < len(my_ticket):
  for i in range(len(my_ticket)):
    if i in mapping.values():
      continue
    count = 0
    f = None
    for field, ranges in fields.items():
      if field in mapping.keys():
        continue
      valid = True
      for t in valid_tickets:
        if not valid_range(t[i], ranges[0], ranges[1]):
          valid = False
      if valid:
        count += 1
        f = field

    if count == 1:
      mapping[f] = i

departure = 1
for field, idx in mapping.items():
  if field.startswith('departure'):
    departure *= my_ticket[idx]
print(departure)
