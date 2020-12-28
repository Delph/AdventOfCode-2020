#!/usr/bin/python3

with open('input.txt') as f:
  input = f.read().splitlines()


mem = {}
mask_0 = None
mask_1 = None

for instr in input:
  op, arg = instr.split(' = ')
  if op == 'mask':
    mask_0 = int(arg.replace('X', '1'), 2)
    mask_1 = int(arg.replace('X', '0'), 2)
  else:
    addr = int(op[4:op.index(']')])
    value = int(arg)
    if addr not in mem:
      mem[addr] = 0
    mem[addr] = value & mask_0 | mask_1
print(sum([v for v in mem.values()]))
