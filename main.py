import json

import indent
import requests
urlh = 'https://www.superheroapi.com/api.php/2619421814940190/search/Hulk'
h = requests.get(urlh)
res_h = requests.get(urlh)
h_dict = res_h.json()

urlc = 'https://www.superheroapi.com/api.php/2619421814940190/search/Captain_America'
c = requests.get(urlc)
res = requests.get(urlc)
c_dict = res.json()


urlt = 'https://www.superheroapi.com/api.php/2619421814940190/search/Thanos'
t = requests.get(urlt)
res_t = requests.get(urlt)
t_dict = res_t.json()

def Intelligence(dict):
    result = dict['results']
    stats = result[0]
    power = stats['powerstats']
    int = power['intelligence']
    return int
Hulk_int = Intelligence(h_dict)
cap_int = Intelligence(c_dict)
thor_int = Intelligence(t_dict)
list_ = [int(Hulk_int),int(cap_int),int(thor_int)]
print('Самый умный:', max(list_))


