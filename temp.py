from ytmusicapi import YTMusic

ytmusic = YTMusic('oauth.json')


search_results = ytmusic.search("Po nee po")
print(search_results[0])
print(search_results[0]['videoId'])