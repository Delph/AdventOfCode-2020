#!/usr/bin/python3

with open('input.txt') as f:
  input = f.read().splitlines()


earliest = int(input[0])
services = list(map(int, [x for x in input[1].split(',') if x != 'x']))

closest = 0
bus = None
for service in services:
  n = ((earliest // service) + 1) * service
  if closest == 0 or n < closest:
    closest = n
    bus = service

print((closest - earliest) * bus)
