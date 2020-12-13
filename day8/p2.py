#!/usr/bin/python3

with open('input.txt') as f:
  input = f.read().splitlines()

def execute(instructions):
  accumulator = 0
  ip = 0

  ip_visited = []
  while ip < len(instructions):
    if ip in ip_visited:
      raise Exception()
    ip_visited.append(ip)
    instruction = instructions[ip]
    op = instruction[:3]
    arg = int(instruction[4:])

    if op == 'acc':
      accumulator += arg
    elif op == 'jmp':
      ip += arg
      continue
    elif op == 'nop':
      pass
    else:
      print(f'invalid instruction: {op} at {ip}')
      break
    ip += 1
  if ip == len(instructions):
    return accumulator
  else:
    raise Exception()

for i, instr in enumerate(input):
  c = [n for n in input]
  if c[i][:3] == 'nop':
    c[i] = f'jmp {c[i][4:]}'
  elif c[i][:3] == 'jmp':
    c[i] = f'nop {c[i][4:]}'
  try:
    print(execute(c))
  except:
    pass
