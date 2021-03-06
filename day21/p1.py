#!/usr/bin/python3

with open('input.txt') as f:
#with open('test.txt') as f:
  input = f.read().splitlines()


foods = []
allergens = []
ingredients = []

for line in input:
  ins, als = line[:-1].split(' (contains ')
  food = {
    'ingredients': ins.split(' '),
    'allergens': als.split(', ')
  }

  foods.append(food)
  for i in food['ingredients']:
    if i not in ingredients:
      ingredients.append(i)

  for a in food['allergens']:
    if a not in allergens:
      allergens.append(a)

ingredients_with_allergens = set()
for a in allergens:
  foods_with_allergen = [f for f in foods if a in f['allergens']]

  ingredient_sets = []
  for f in foods_with_allergen:
    ingredient_sets.append(set(f['ingredients']))
  intersection = ingredient_sets[0].intersection(*ingredient_sets[1:])
  ingredients_with_allergens.update(intersection)
inert_ingredients = set(ingredients) - ingredients_with_allergens

count = 0
for f in foods:
  for i in f['ingredients']:
    if i in inert_ingredients:
      count += 1
print(count)
