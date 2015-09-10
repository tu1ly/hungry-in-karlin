
import random
from subprocess import call

import yaml


with open('./venues.yml') as f:
    venues = yaml.load(f)

venue = random.choice(venues)
print(venue['name'])
print(venue['url'])

call(['open', venue['url']])
