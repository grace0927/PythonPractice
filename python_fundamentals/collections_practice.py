from pprint import pprint as pp


def print_title(title):
    half_banner = '*'*10
    print(half_banner + title + half_banner)

def tuple_practice():
    print_title('tuple')

    t = ("Norway", 4.342, 4)

    for item in t:
        print(item)

    h = (381)
    print(type(h))

    k = (381,)
    print(type(k))

    print(4 in t)

def str_practice():
    print_title('str')

    m = ' '.join(['hello', 'world'])
    print(m)

    print(m.split(' '))

    hello, _, world = m.partition(' ')
    print('{hello}, {world}'.format(hello=hello, world=world))

def range_practice():
    print_title('range')

    for i in range(5):
        print(i)

    print(list(range(5, 10)))

    print(list(range(-1, 10, 2)))

    t = [6, 12, 243, 23, 2342]
    for item in enumerate(t):
        print(item)

    for k, v in enumerate(t):
        print("k={}, v={}".format(k, v))

def list_practice():
    print_title('list')

    m = "hello world my friends are here".split(' ')
    print(m[-1])

    print(m[2:])
    print(m[:4])
    full = m[:]
    print(full)
    print(m.copy())
    print(list(m))

    k = [[3, 4], [5, 6]]
    v = k.copy()
    print(k[0] is v[0]) # they point to the same object, it shadow copy reference but not recursively
    print(k is v)
    print(k == v)
    k[0].append(1)
    print(v)

def dict_practice():
    print_title('dict')

    city = {'China': 'Beijing',
            'USA': 'Washington'}
    print(city['USA'])

    for value in city.values():
        print(value)

    nba = dict(Lakers='Los Angeles', Bulls='Chicago', Knicks="New York")
    copy = nba.copy()
    print(copy)

    nba.update(Celtics='Boston')
    texas = dict(Rockets='Hoston', Spurs='San Antonio', Mavericks='Dallas')
    nba.update(texas)
    print(nba)

    for key in nba:
        print('nba team {key} is in city {value}'.format(key=key, value=nba[key]))

    for team, city in nba.items():
        print(f'City {city} has nba team {team}')

    print('Lakers' in nba)
    print('Look' in nba)
    pp(nba)

def set_practice():
    print_title('set')

    nba_city = {'Los Angeles', 'Dallas', 'Chicago', 'New York'}
    print(type(nba_city))

    team = set(['Lakers', 'Spurs', 'Mavericks'])
    print(team)

    team.add('Rockets')
    team.update(['Rockets', 'Bulls'])
    print(team)

    west_team = {'Lakers', 'Kings', 'Rockets'}
    ca_team = {'Lakers', 'Kings', 'Clippers'}
    taxes_team = {'Rockets'}
    print(west_team.union(ca_team))
    print(west_team.intersection(ca_team))
    print(west_team.difference(ca_team))
    print(west_team.symmetric_difference(ca_team))
    print(taxes_team.issubset(west_team))
    print(west_team.issuperset(west_team))
    print(ca_team.isdisjoint(taxes_team))

tuple_practice()
str_practice()
range_practice()
list_practice()
dict_practice()
set_practice()
