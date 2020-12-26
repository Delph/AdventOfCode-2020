#!/usr/bin/python3


#starting = [0, 3, 6]
starting = [11, 0, 1, 10, 5, 19]

numbers = {}
last = None
turn = 1


def add_number(n, turn):
  if n in numbers:
    numbers[n][1] = numbers[n][0]
    numbers[n][0] = turn
  else:
    numbers[n] = [turn, None]

def next_number(last):
  if numbers[last][1] == None:
    return 0
  return numbers[last][0] - numbers[last][1]


# setup
for n in starting:
  add_number(n, turn)
  last = n
  turn += 1


while turn < 30_000_000:
  n = next_number(last)
  add_number(n, turn)
  last = n
  turn += 1
print(next_number(last))
