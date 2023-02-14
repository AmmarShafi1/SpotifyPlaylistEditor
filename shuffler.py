import spotipy
import random
from spotipy.oauth2 import SpotifyOAuth
import cred


def get_user_id():
    # Gets the user's unique Username ID
    scope = "playlist-read-collaborative"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_id, client_secret=cred.client_secret,
                                                   redirect_uri=cred.redirect_url, scope=scope))
    results = sp.me()
    return results['id']


def get_play_id(playListName: str):
    # Get the unique playlist ID matching the Name
    scope = "playlist-read-collaborative"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_id, client_secret=cred.client_secret,
                                                   redirect_uri=cred.redirect_url, scope=scope))
    results = sp.current_user_playlists()
    playlist_id = ""
    for idx, item in enumerate(results['items']):
        if item['name'] == playListName:
            playlist_id += item['id']
    return playlist_id


def get_track_ids(username, playlist_id):
    # Get all the track IDs in the playlist in the form of a list
    scope = 'playlist-modify-public'
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_id, client_secret=cred.client_secret,
                                                   redirect_uri=cred.redirect_url, scope=scope))
    r = sp.user_playlist_tracks(username, playlist_id)
    t = r['items']
    ids = []
    while r['next']:
        r = sp.next(r)
        t.extend(r['items'])
    for s in t: ids.append(s["track"]["id"])
    return ids


def shuffleTracks(tracks, username, playlist_id):
    # shuffles the 'tracks' list
    tracks = get_track_ids(username, playlist_id)
    random.shuffle(tracks)
    return (tracks)


def createNewPl(pl_name, tracks, username):
    # Create/Remake the requested playlist
    # This will check to see if the shuffled playlist already exists, if this is the case
    # all the songs will be deleted, and then re-added. Otherwise, a new playlist will be created
    # and the new playlist ID will be retrieved
    scope = 'playlist-modify-public'
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_id, client_secret=cred.client_secret,
                                                   redirect_uri=cred.redirect_url, scope=scope))
    if get_play_id(pl_name + " Shuffle") == "":
        sp.user_playlist_create(username, pl_name + " Shuffle", True, False)
        newPlid = get_play_id(pl_name + " Shuffle")
    else:
        newPlid = get_play_id(pl_name + " Shuffle")
        temp = tracks
        while True:
            if (len(temp) > 100):
                remTracks = temp[0:100]
            else:
                remTracks = temp
            sp.user_playlist_remove_all_occurrences_of_tracks(username, newPlid, remTracks)
            if (len(temp) < 100):
                break
            temp = temp[100:(len(temp))]
    while True:
        # This is implemented in such fashion because the spotify API only allows for up to 100 insertions
        # to a playlist at a time
        if (len(tracks) > 100):
            newTracks = tracks[0:100]
        else:
            newTracks = tracks
        sp.user_playlist_add_tracks(username, newPlid, newTracks)
        if (len(tracks)) < 100:
            break
        tracks = tracks[100:(len(tracks))]

def combineNewPl(pl_name, tracks, username):
    # Create/Remake the requested playlist
    # This will check to see if the shuffled playlist already exists, if this is the case
    # all the songs will be deleted, and then re-added. Otherwise, a new playlist will be created
    # and the new playlist ID will be retrieved
    scope = 'playlist-modify-public'
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_id, client_secret=cred.client_secret,
                                                   redirect_uri=cred.redirect_url, scope=scope))
    if get_play_id(pl_name) == "":
        sp.user_playlist_create(username, pl_name, True, False)
        newPlid = get_play_id(pl_name)
    else:
        newPlid = get_play_id(pl_name)
        temp = tracks
        while True:
            if (len(temp) > 100):
                remTracks = temp[0:100]
            else:
                remTracks = temp
            sp.user_playlist_remove_all_occurrences_of_tracks(username, newPlid, remTracks)
            if (len(temp) < 100):
                break
            temp = temp[100:(len(temp))]
    while True:
        # This is implemented in such fashion because the spotify API only allows for up to 100 insertions
        # to a playlist at a time
        if (len(tracks) > 100):
            newTracks = tracks[0:100]
        else:
            newTracks = tracks
        sp.user_playlist_add_tracks(username, newPlid, newTracks)
        if (len(tracks)) < 100:
            break
        tracks = tracks[100:(len(tracks))]

def shuffleOldPl(pl_name, tracks, username):
    print("shuffleoldpl")
    scope = 'playlist-modify-public'
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_id, client_secret=cred.client_secret,
                                                   redirect_uri=cred.redirect_url, scope=scope))
    newPlid = get_play_id(pl_name)
    temp = tracks
    while True:
        if (len(temp) > 100):
            remTracks = temp[0:100]
        else:
            remTracks = temp
        sp.user_playlist_remove_all_occurrences_of_tracks(username, newPlid, remTracks)
        if (len(temp) < 100):
            break
        temp = temp[100:(len(temp))]
    while True:
        # This is implemented in such fashion because the spotify API only allows for up to 100 insertions
        # to a playlist at a time
        if (len(tracks) > 100):
            newTracks = tracks[0:100]
        else:
            newTracks = tracks
        sp.user_playlist_add_tracks(username, newPlid, newTracks)
        if (len(tracks)) < 100:
            break
        tracks = tracks[100:(len(tracks))]
    return(newPlid)

def get_play_pic():
    # Get the unique playlist ID matching the Name
    scope = "playlist-read-collaborative"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_id, client_secret=cred.client_secret,
                                                   redirect_uri=cred.redirect_url, scope=scope))
    results = sp.current_user_playlists()
    covers = []
    for idx, item in enumerate(results['items']):
        covers.append(sp.playlist_cover_image(item['id'])[0])
    coverLinks = []
    for item in covers:
        coverLinks.append(item["url"])
    return coverLinks


def get_play_names():
    # get a list of the user's playlist's names
    scope = "playlist-read-collaborative"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_id, client_secret=cred.client_secret,
                                                   redirect_uri=cred.redirect_url, scope=scope))
    results = sp.current_user_playlists()
    playNames = []
    for idx, item in enumerate(results['items']):
        playNames.append(item['name'])
    return playNames


def newShufflePl(pl_name):
    username = get_user_id()
    playlist_id = get_play_id(pl_name)
    tracks = shuffleTracks(get_track_ids(username, playlist_id), username, playlist_id)
    createNewPl(pl_name, tracks, username)
    newPID = get_play_id(pl_name + " Shuffle")
    return newPID

def oldShufflePl(pl_name):
    username = get_user_id()
    playlist_id = get_play_id(pl_name)
    tracks = shuffleTracks(get_track_ids(username, playlist_id), username, playlist_id)
    shuffleOldPl(pl_name, tracks, username)
    newPID = get_play_id(pl_name)
    return newPID

def labeledPlaySet():
    # creates a nested lists where the first index is the picture URL and the second index is the name of the playlist
    names = ((get_play_names()))
    pics = ((get_play_pic()))
    labeledPics = []
    for i in range(len(names)):
        labeledPics.append([pics[i], names[i]])
    return labeledPics


def plInfo(pID):
    # get a playlist's name, url, and image url
    scope = "playlist-read-collaborative"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_id, client_secret=cred.client_secret,
                                                   redirect_uri=cred.redirect_url, scope=scope))
    PL = sp.playlist(pID)
    name = PL['name']
    url = (PL['external_urls']['spotify'])
    img = (PL['images'][0]['url'])
    return [name, url, img]

def getCombineTracks(plNums):
    username = get_user_id()
    plNames = get_play_names()
    returntracks = []

    for number in plNums:
        tempTracks = (get_track_ids(username, get_play_id(plNames[number])))
        for track in tempTracks:
            if track in returntracks:
                continue
            else:
                returntracks.append(track)
    return returntracks
def combinePl(plNums,newName):
    username = get_user_id()
    tracks = getCombineTracks(plNums)
    combineNewPl(newName,tracks,username)
    newPID = get_play_id(newName)
    return newPID



