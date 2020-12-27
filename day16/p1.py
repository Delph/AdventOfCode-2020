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


error_rate = 0
def valid(ticket):
  return sum([1 if valid_field(v) else 0 for v in ticket]) == len(ticket)

for ticket in other_tickets:
  for v in ticket:
    if not valid_field(v):
      error_rate += v
print(error_rate)
