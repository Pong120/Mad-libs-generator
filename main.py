from data import nouns, verbs, adjectives, places, templates
import random

print('Welcome to Mad Libs Generator')

template = random.choice(templates)
templates.remove(template)
print(f'This template is created for you: {template}')
chance = input('You have one chance to request new template. Change it or not(y/n):').lower()
if chance == 'y':
    new_template = random.choice(templates)
    print(new_template)

selected_noun = random.choice(nouns)
selected_verb = random.choice(verbs)
selected_adjective = random.choice(adjectives)
selected_place = random.choice(places)

story = template.format(noun=selected_noun, verb=selected_verb, adjective=selected_adjective, place=selected_place)

print('\nHere is your Mad Libs story:')
print(story)
