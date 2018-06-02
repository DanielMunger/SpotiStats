#!/usr/bin/env python3


# mortdecai13

import os, sys, json, logging, argparse, collections
import spotipy, spotipy.util as util, numpy as np
import pandas as pd, seaborn as sns, matplotlib.pyplot as plt
import fcntl, termios, struct
import pprint

from Track import Track

#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


#TODO:
# create an aws account and _use_ it!
# refactor authenticate function.
# song recommendations
# graphing and mapping of existing library
# incorporate database work
# make it a console app
    # error handling

creds = json.load(open('./credentials.json'))
client_id = creds['SPOTIPY_CLIENT_ID']
client_secret = creds['SPOTIPY_CLIENT_SECRET']
redirect_uri = creds['SPOTIPY_REDIRECT_URL']
scope = 'user-top-read user-library-read'


def main():
    displayTitle()
    username = input('Please enter your Spotify username: ')
    if len(sys.argv) == 0:
        print('Please, enter your username')
    (token) = authenticate(username)
    trackFeatures(token, username)




#graphic functions
def displayTitle():
    os.system('clear')
    (width, height) = terminal_size()
    print("*"*width)
    print("\t            Welcome to SpotiStats!                  \t")
    print("\t SPOTISTATS: A terminal app to analyze spotify data \t")
    print("*"*width)

def terminal_size():
    #not my code, but it's cool
    th, tw, hp, wp = struct.unpack('HHHH',
    fcntl.ioctl(0, termios.TIOCGWINSZ,
    struct.pack('HHHH', 0, 0, 0, 0)))
    return tw, th

def drawTrackFeatures(tracks):
    # header
    (width, height) = terminal_size()
    header = ['Artist', 'Title', 'Duration', 'Danceability', 'Energy', 'Key', 'Loudness', 'Acousticness', 'Speechiness', 'Instrumentalness', 'Liveness', 'Valence', 'Mode']
    headerOut = ''
    for item in header:
        headerOut += '| ' + str(item) + ' '
    headerOut += '\n'+'_'*width

    # make it pretty
    print(headerOut)
    for track in tracks:
        row = [track.artist, track.title, str(track.duration)+'s', track.danceability, track.energy, track.key, track.loudness, track.acousticness, track.speechiness, track.instrumentalness, track.liveness, track.valence, track.mode]
        rowOut = ''
        for item in row:
            rowOut += '| ' + str(item) + ' '
        print(rowOut)

#auth and user interaction
def authenticate(username):
    #Check for username
    #logging.debug('Authenticating')
    token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)
    if(token):
        print('User was authenticated successfully.')
        return(token)
        #trackFeatures(token, username)
    else:
        print("Authentication failed for ", username)
    # else:
    #     print("Please specify a user to Authenticate" % (sys.argv[0]))
    #     sys.exit()


#analysis and data gathering
def trackFeatures(token, username):
    sp = spotipy.Spotify(auth=token)
    user = sp.user(username)
    saved_tracks = sp.current_user_saved_tracks(limit=5)
    pp = pprint.PrettyPrinter(indent=1, depth=2)
    #pp.pprint(saved_tracks['items'])
    tracks = []
    for track in saved_tracks['items']:
        #pp.pprint(track['track']['id'])
        #track_analysis = sp.audio_analysis(track['track']['id'])
        track_features = sp.audio_features(track['track']['id'])
        duration = track_features[0]['duration_ms']
        duration /=1000
        danceability = track_features[0]['danceability']
        energy = track_features[0]['energy']
        key = track_features[0]['key']
        loudness = track_features[0]['loudness']
        acousticness = track_features[0]['acousticness']
        speechiness = track_features[0]['speechiness']
        instrumentalness = track_features[0]['instrumentalness']
        liveness = track_features[0]['liveness']
        valence = track_features[0]['valence']
        mode = track_features[0]['mode']
        artist = track['track']['album']['artists'][0]['name']
        title = track['track']['name']

        newTrack = Track(artist, title, duration, danceability, energy, key, loudness, acousticness, speechiness, instrumentalness, liveness, valence, mode)
        tracks.append(newTrack)

    drawTrackFeatures(tracks)
    analyze(tracks)

def analyze(tracks):
        df_features = pd.DataFrame(tracks)[["id", "analysis_url", "duration_ms", "acousticness", "danceability", "energy", "instrumentalness", "liveness", "loudness", "valence",
        "speechiness", "key", "mode", "tempo", "time_signature"]]

if __name__== "__main__":
  main()
