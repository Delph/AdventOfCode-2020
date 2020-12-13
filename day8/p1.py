#!/usr/bin/python3

with open('input.txt') as f:
  input = f.read().splitlines()

accumulator = 0
ip = 0

ip_visited = []
while ip < len(input):
  if ip in ip_visited:
    break
  ip_visited.append(ip)
  instruction = input[ip]
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
print(accumulator)
