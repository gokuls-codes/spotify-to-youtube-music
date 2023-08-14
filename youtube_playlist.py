from ytmusicapi import YTMusic

yt = YTMusic('oauth.json')
playlistId = yt.create_playlist('tamil love songs test', 'made using python')
to_add_ids = []

unable_to_add = []

with open("100%love.txt", "r") as f:
    lines = f.readlines()
    
for line in lines:
    track_name = line.strip()
    
    if not track_name:
        continue
    
    search_results = yt.search(track_name)
    if 'title' in search_results[0]:
        print(search_results[0]['title'])
    else:
        print("notitle: ", track_name)
    if 'videoId' in search_results[0]:
        to_add_ids.append(search_results[0]['videoId'])
        yt.add_playlist_items(playlistId, [search_results[0]['videoId']])
        print("Added: ", track_name)
    else:
        unable_to_add.append(track_name)
        print(f"unable to add: {track_name}")
    
print(to_add_ids)

print(f"Successfully added {len(to_add_ids)} to playlist: * love songs tamil *")

# search_results = yt.search('So baby from doctor')

# print(search_results[0])

print(unable_to_add)