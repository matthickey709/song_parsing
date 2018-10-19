# Song Parser
Parses songs from a semi-formatted text file and stores each song's information in JSON.

## Song Formatting
This parser reads lines that describe a song in the following format:

```
"{Song Name}" {Artist} {Chord Progression(s)}
```  

and it creates a JSON file where each entry in the JS array has these 3 fields:

```
{
    "chord-progression": "I-V-vi-IV", 
    "artist": "The Beatles", 
    "title": "Let It Be"
}
```
