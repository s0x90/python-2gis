# -*- coding: utf-8 -*-


import dgis
from envparse import env

if __name__ == '__main__':
    env.read_envfile()
    API_KEY = env('API_KEY', None)
    client = dgis.API(API_KEY)
    firms = client.search(q=u'пиво', point=[56.001573, 54.7069285], radius=1000,
                            fields='items.adm_div, items.address, items.point', sort='distance')

    branch_id = firms['result']['items'][0]['id']
    branch = client.get_branch(id=branch_id)
    print(branch)
