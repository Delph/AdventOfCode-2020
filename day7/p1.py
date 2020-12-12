#!/usr/bin/python3

import re

with open('input.txt') as f:
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


gold_list = []
def can_contain_shiny_gold_bag(bag):
  if bag == 'shiny gold':
    return True
  if bag in gold_list:
    return True

  for b in bags[bag].keys():
    if can_contain_shiny_gold_bag(b):
      gold_list.append(bag)
      return True
  return False

last = -1
while len(gold_list) > last:
  last = len(gold_list)
  for bag in bags.keys():
    can_contain_shiny_gold_bag(bag)

print(len(gold_list))
