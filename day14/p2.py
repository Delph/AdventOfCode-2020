#!/usr/bin/python3

#with open('test.txt') as f:
with open('input.txt') as f:
  input = f.read().splitlines()


mem = {}
mask_x = None
mask_1 = None

def replace_x(src, rep):
  p = 0
  r = ''
  for i in range(len(src)):
    if src[i] == 'X':
      r += rep[p]
      p += 1
    else:
      r += src[i]
  return r

def replace(src, rep):
  r = ''
  for i in range(len(src)):
    if rep[i] == 'X':
      r += 'X'
    else:
      r += src[i]
  return r

for instr in input:
  op, arg = instr.split(' = ')
  if op == 'mask':
    mask_x = arg.replace('1', '0')
    mask_1 = int(arg.replace('X', '0'), 2)
  else:
    addr_base = int(op[4:op.index(']')]) | mask_1
    addr_base = replace(f'{addr_base:036b}', mask_x)
    value = int(arg)
    max = 2 ** mask_x.count('X')
    for i in range(max):
      f = replace_x(addr_base, (f'{i:b}').zfill(mask_x.count('X')))
      addr = int(f, 2)
      if addr not in mem:
        mem[addr] = 0
      mem[addr] = value
print(sum([v for v in mem.values()]))
