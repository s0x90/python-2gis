# -*- coding: utf-8 -*-


import dgis
from envparse import env

if __name__ == '__main__':
    env.read_envfile()
    API_KEY = env('API_KEY', None)
    client = dgis.API(API_KEY)
    print(client.search(q=u'пиво', point=[56.001573, 54.7069285], radius=1000, sort='distance'))
