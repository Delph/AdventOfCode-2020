#!/usr/bin/python3

with open('input.txt') as f:
  input = f.read().splitlines()


EMPTY = 'L'
OCCUPIED = '#'
FLOOR = '.'

def take_seat(x, y, state):
  if state[y][x] != EMPTY:
    return False

  for i in range(-1, 2):
    for j in range(-1, 2):
      if i == 0 and j == 0:
        continue
      if y + i < 0 or y + i >= len(state):
        continue
      if x + j < 0 or x + j >= len(state[0]):
        continue
      if state[y + i][x + j] == OCCUPIED:
        return False
  return True

def leave_seat(x, y, state):
  if state[y][x] != OCCUPIED:
    return False

  count = 0
  for i in range(-1, 2):
    for j in range(-1, 2):
      if i == 0 and j == 0:
        continue
      if y + i < 0 or y + i >= len(state):
        continue
      if x + j < 0 or x + j >= len(state[0]):
        continue
      if state[y + i][x + j] == OCCUPIED:
        count += 1
  return count >= 4


def replace(str, idx, c):
  return str[0:idx] + c + str[idx+1:]


def step(state):
  after = [r for r in state]
  for y in range(len(state)):
    for x in range(len(state[0])):
      if state[y][x] == FLOOR:
        continue
      if take_seat(x, y, state):
        after[y] = replace(after[y], x, OCCUPIED)
      if leave_seat(x, y, state):
        after[y] = replace(after[y], x, EMPTY)
  return after


def display(state):
  for r in state:
    print(r)
  print('')


last = None
state = step(input)
steps = 1
while state != last:
  steps += 1
  last = state
  state = step(state)

print(steps)

count = 0
for r in state:
  count += len([1 for x in r if x == OCCUPIED])
print(count)
