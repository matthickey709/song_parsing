import re
import json
from pprint import pprint

songs = []
with open('4chords.txt', 'r') as f:
    songs = f.readlines()

songs_formatted = []

# Iterate through every song in the lsit
for song in songs:
    if song.startswith('#'):
        continue
    curr_song = {}
    # Parse for title
    title = re.search('^\"(.*)\"\s+', string=song)
    if title:
        curr_song['title'] = title.group(1)
    # Parse for artist
    artist = re.search('^\".*\"\s+(.*)\s+[vi|V|I|VI].*$', string=song)
    if artist:
        curr_song['artist'] = artist.group(1)
    # Parse for chord progression
    chords = re.search("([A-Za-z]{1,2}-[A-Za-z]{1,2}-[A-Za-z]{1,2}-[A-Za-z]{1,2}.*)$", string=song)
    if chords:
        curr_song['chord-progression'] = chords.group(1)

    # Song needs all attributes to be added to dict
    if title and artist and chords:
        songs_formatted.append(curr_song)
    else:
        print "Trouble with song: ", song

with open('4chords_formatted.json', 'w+') as js:
    json.dump(songs_formatted, js, indent=4)
