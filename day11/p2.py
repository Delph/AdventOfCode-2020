#!/usr/bin/python3

with open('input.txt') as f:
  input = f.read().splitlines()


EMPTY = 'L'
OCCUPIED = '#'
FLOOR = '.'

_cache = {}
def find_seats(x, y, state):
  if f'{y}_{x}' in _cache:
    return _cache[f'{y}_{x}']
  h = len(state)
  w = len(state[0])

  seats = []
  # go left
  for i in range(x-1, -1, -1):
    if state[y][i] != FLOOR:
      seats.append([y, i])
      break
  # go right
  for i in range(x+1, w):
    if state[y][i] != FLOOR:
      seats.append([y, i])
      break

  # go up
  for j in range(y-1, -1, -1):
    if state[j][x] != FLOOR:
      seats.append([j, x])
      break
  # go down
  for j in range(y+1, h):
    if state[j][x] != FLOOR:
      seats.append([j, x])
      break

  # go left up
  lu = min(x+1, y+1)
  for i in range(1, lu):
    if state[y-i][x-i] != FLOOR:
        seats.append([y-i, x-i])
        break
  # go left down
  ld = min(x+1, h-y)
  for i in range(1, ld):
    if state[y+i][x-i] != FLOOR:
      seats.append([y+i, x-i])
      break

  # go right up
  ru = min(w-x, y+1)
  for i in range(1, ru):
    if state[y-i][x+i] != FLOOR:
      seats.append([y-i, x+i])
      break
  # go right down
  rd = min(w-x, h-y)
  for i in range(1, rd):
    if state[y+i][x+i] != FLOOR:
      seats.append([y+i, x+i])
      break

  _cache[f'{y}_{x}'] = seats
  return seats

def take_seat(x, y, state):
  if state[y][x] != EMPTY:
    return False

  seats = find_seats(x, y, state)
  for j,i in seats:
    if state[j][i] == OCCUPIED:
      return False
  return True

def leave_seat(x, y, state):
  if state[y][x] != OCCUPIED:
    return False

  seats = find_seats(x, y, state)
  count = 0
  for j,i in seats:
    if state[j][i] == OCCUPIED:
      count += 1
  return count >= 5


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
