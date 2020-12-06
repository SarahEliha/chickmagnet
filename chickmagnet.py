import os, requests, time, json, sys

APP_ID = 'APP_ID'
API = 'https://torrentapi.org/pubapi_v2.php?app_id=' + APP_ID + '&'

session = requests.Session()
session.headers.update({'Accept': 'application/json', 'User-Agent': APP_ID + '/' + APP_ID})

request = session.get(API, params={'app_id': APP_ID, 'get_token': 'get_token'})
TOKEN = request.json()['token']

print('Getting torrents...')
search_string = sys.argv[1]
results = None
while True:
    try:
        time.sleep(1)
        request = session.get(API, params={'app_id': APP_ID, 'ranked': 0, 'token': TOKEN, 'limit': 100, 'mode': 'search', 'category': 4, 'search_string': search_string})
        results = request.json()['torrent_results']
        break
    except KeyError:
        print('Failed. Trying again...')
count = 0
magnets = ''
for result in results:
    #print(result.get('download'))
    count += 1
    magnets += str(result) + ' '
if count >= 100:
    print('\nIf the number of magnet links are greater than 100 then there might be more than 100 results. API limits results to maximum 100.')

os.system('qbittorrent-nox ' + magnets)
print('\nAdded ' + str(count) + ' torrents.')
