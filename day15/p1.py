#!/usr/bin/python3


def rindex(l, e):
  return len(l) - l[::-1].index(e) - 1


#numbers = [0, 3, 6]
numbers = [11, 0, 1, 10, 5, 19]

last = numbers[-1]

while len(numbers) < 2020:
  if numbers.count(last) == 1:
    numbers.append(0)
  else:
    prev = rindex(numbers, last)
    prevprev = rindex(numbers[:prev], last)

    numbers.append(prev - prevprev)
  last = numbers[-1]
print(numbers[2019])
