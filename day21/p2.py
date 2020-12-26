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

# for each ingredient with an allergen, find the allergen
mapped_allergens = {}

while len(mapped_allergens.keys()) < len(ingredients_with_allergens):
  for a in allergens:
    foods_with_allergen = [f for f in foods if a in f['allergens']]
    ingredient_sets = []
    for f in foods_with_allergen:
      ingredient_sets.append(set(f['ingredients']))
    intersection = ingredient_sets[0].intersection(*ingredient_sets[1:]) - set(mapped_allergens.values())
    if len(intersection) == 1:
      mapped_allergens[a] = list(intersection)[0]

canonical_dangerous_ingredients = []
for a in sorted(mapped_allergens.keys()):
  canonical_dangerous_ingredients.append(mapped_allergens[a])
print(','.join(canonical_dangerous_ingredients))
