#!/usr/bin/python3

with open('input.txt') as f:
#with open('test.txt') as f:
  input = f.read().splitlines()


adapters = sorted(map(int, input))
print(adapters)
jolts = 0
diff = [0, 0, 1]
for adapter in adapters:
  if adapter - jolts > 3:
    print(f'diff too high! adapter {adapter} and {jolts} jolts')
    break
  diff[adapter - jolts - 1] += 1
  if adapter - jolts == 3:
    print(f'{jolts} {adapter}')
  jolts = adapter
print(diff)
print(diff[0] * diff[2])
