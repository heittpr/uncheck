import requests, json

with open('auth.json', 'r') as f:
    auth = json.loads(f.read())

api = 'https://api.twitter.com'

def check(username):
    endpoint = '/2/users/by/username/{}'

    url = api + endpoint.format(username)
    h = { 'Authorization': f'Bearer {auth["bearer"]}' }

    r = requests.get(url, headers=h)
    r = json.loads(r.content)

    if 'errors' in r:
        for e in r['errors']:
            if e['detail'].startswith('Could not find user with username'):
                return True

    return False
