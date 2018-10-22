import re
import json
import sys
import os
from pprint import pprint

dirname = os.path.dirname(__file__)
output_filename = os.path.join(dirname, '..', '4chords_formatted.json')
input_filename = os.path.join(dirname, '4chords.txt')

songs = []
def gen_json_list():
    with open(input_filename, 'r') as f:
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
            print("Trouble with song: ", song)

    with open(output_filename, 'w+') as js:
        json.dump(songs_formatted, js, indent=4)

    return songs_formatted
