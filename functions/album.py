
def make_album(artist, title, no_of_tracks=''):
    ''' return a dictionary of information about a album '''
    album = {'artist': artist, 'title': title}
    if no_of_tracks:
        album['tracks'] = no_of_tracks
    return album

# album_0 = make_album('taylor swift', 'blank space')
# print(album_0)

# album_3 = make_album('50 cent', 'heal', 23)
# print(album_3)

while True:
    print('\nEnter album details:')
    print('Enter "q" to close the program.')
    artist = input('Enter artist name: ')
    if artist == 'q':
        break
    title = input('Enter album title: ')
    if title == 'q':
        break
    track = input('Enter no of tracks: ')
    if track == 'q':
        break
    elif track:
        album = make_album(artist, title, track)
    else:
        album = make_album(artist, title)

    print(album)