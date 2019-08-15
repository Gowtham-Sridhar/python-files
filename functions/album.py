
def make_album(artist, title, no_of_tracks=''):
    ''' return a dictionary of information about a album '''
    album = {'artist': artist, 'title': title}
    if no_of_tracks:
        album['tracks'] = no_of_tracks
    return album

album_0 = make_album('taylor swift', 'blank space')
print(album_0)
album_1 = make_album('eminem', 'venom')
album_2 = make_album('kety berry', 'dark horse')
print(album_1)
print(album_2)

album_3 = make_album('50 cent', 'heal', 23)
print(album_3)