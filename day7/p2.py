#!/usr/bin/python3

import re

with open('input.txt') as f:
#with open('test.txt') as f:
  input = f.read().splitlines()


outer_r = re.compile(r'([a-z ]+) bags contain')
inner_r = re.compile(r'(\d+) ([a-z ]+) bag')

bags = {}
for rule in input:
  bag = outer_r.search(rule).group(1)

  bags[bag] = {}
  latter = rule[rule.index('contain'):]
  for inner in latter.split(','):
    m = inner_r.search(inner)
    if m:
      bags[bag][m.group(2)] = int(m.group(1))


def bags_inside(bag):
  count = 1

  for b, c in bags[bag].items():
    count += c * bags_inside(b)
  return count

print(bags_inside('shiny gold')-1)
