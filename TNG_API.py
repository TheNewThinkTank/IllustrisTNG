import requests
# from pprint import pprint
import pp

# Run and send output to logfile:
# python TNG_API.py >log 2>&1

baseUrl = 'http://www.tng-project.org/api/'
headers = {"api-key": "07f16468518e6f28c60862e20b0f36f0"}


def get(path, params=None):
    # make HTTP GET request to path
    r = requests.get(path, params=params, headers=headers)

    # raise exception if response code is not HTTP SUCCESS (200)
    r.raise_for_status()

    if r.headers['content-type'] == 'application/json':
        return r.json()  # parse json responses automatically
    return r


r = get(baseUrl)

print("Name of response dictionary key: ", r.keys())
print("Number of simulations: \t \t ", len(r['simulations']), "\n")
print("\n Fields of first sim.:")
pp(r['simulations'][0])
names = [sim['name'] for sim in r['simulations']]
print("\n \n Names of all simulations:")
pp(names)

Sim = "TNG100-1-Dark"

i = names.index(Sim)  # names.index('Illustris-3')
print(f"\n \n Index of simulation ({Sim}): {i}")
sim = get(r['simulations'][i]['url'])
print("\n \n Keys:")
pp(sim.keys())
print("\n \n Number of dark matter particles: ", sim['num_dm'])
print("\n Snapshots URL: \t \t  ", sim['snapshots'])
snaps = get(sim['snapshots'])
print("\n Number of snapshots: \t \t  ", len(snaps))
print("\n \n Data for last snapshot:")
pp(snaps[-1])
snap = get(snaps[-1]['url'])
print("\n \n Last snapshot:")
pp(snap)

subs = get(snap['subhalos'])
print("\n \n Subhalo: \t ", subs, "\n")
print("type(subs): \t ", type(subs))

# print(subs.json(), "\n")
# print(str(subs), "\n")
# print("Subhalo keys: ", subs.keys(), "\n")

# print(subs['count'])
print("\n \n Content:")
pp(dir(subs))
print("\n \n Dictionary items:")
pp(subs.__dict__)

'''
subs['count']

subs['next']

len(subs['results'])

subs = get(snap['subhalos'], {'limit': 220})
len(subs['results'])

subs['next']

subs['results'][0]

subs = get( snap['subhalos'], {'limit':20, 'order_by':'-mass_stars'} )

len(subs['results'])

[ subs['results'][i]['id'] for i in range(5) ]

sub = get( subs['results'][1]['url'] )
sub

url = sub['related']['parent_halo'] + "info.json"
url

parent_fof = get(url)
parent_fof.keys()

parent_fof['Group']


def get(path, params=None):
    # make HTTP GET request to path
    r = requests.get(path, params=params, headers=headers)

    # raise exception if response code is not HTTP SUCCESS (200)
    r.raise_for_status()

    if r.headers['content-type'] == 'application/json':
        return r.json()  # parse json responses automatically

    if 'content-disposition' in r.headers:
        filename = r.headers['content-disposition'].split("filename=")[1]
        with open(filename, 'wb') as f:
            f.write(r.content)
        return filename  # return the filename string

    return r

# Now, request the main progenitor branch from the SubLink merger trees of this subhalo.
'''
