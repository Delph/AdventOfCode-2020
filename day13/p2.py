#!/usr/bin/python3

def chinese(remainders, moduli):
  N = 1
  for m in moduli:
    N *= m

  x = 0
  for r, m in zip(remainders, moduli):
    Ni = N // m
    Xi = 1
    while (Ni * Xi) % m != 1:
      Xi += 1
    x += r * Ni * Xi
  return x % N

with open('input.txt') as f:
  input = f.read().splitlines()


services = list(map(int, [x if x != 'x' else 0 for x in input[1].split(',')]))

modified_positions = [s-i for i, s in enumerate(services) if s != 0]
services = [s for i, s in enumerate(services) if s != 0]

print(chinese(modified_positions, services))
