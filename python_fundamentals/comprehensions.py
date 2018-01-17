import os
import glob

from math import factorial, sqrt
from pprint import pprint as pp


def list_exec():
    words = "The Union and Confederacy quickly raised volunteer and conscription armies.".split()
    print(words)
    length = [len(word) for word in words]
    print(length)
    print([len(str(factorial(x))) for x in range(20)])

def set_exec():
    print({len(str(factorial(x))) for x in range(20)})

def dict_exec():
    nba_team_to_city = {'Pacer': 'Indiana',
                        'Lakers': 'Los Angeles',
                        'Kings': 'Sacramento',
                        'Spurs': 'San Antonio'}
    city_to_team = {city:team for team, city in nba_team_to_city.items()}
    pp(city_to_team)
    words = ['hi', 'hello', 'world']
    pp({x[0]:x for x in words})
    file_sizes = {os.path.realpath(p):os.stat(p).st_size
                  for p in glob.glob('*.py')}
    pp(file_sizes)

def filter_exec():
    primes = [x for x in range(101) if is_prime(x)]
    print(primes)
    prime_square_divisors = {x*x:(1, x, x*x) for x in range(101)
                             if is_prime(x)}
    pp(prime_square_divisors)

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

list_exec()
set_exec()
dict_exec()
filter_exec()
