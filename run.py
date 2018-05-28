#!/usr/bin/env python3

import sys, json, logging, argparse, collections
import spotipy, spotipy.util as util


#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


#TODO:
# create an aws account and _use_ it!
# refactor authenticate function.
# song recommendations
# graphing and mapping of existing library
# incorporate database work
# make it a console app

creds = json.load(open('./credentials.json'))
client_id = creds['SPOTIPY_CLIENT_ID']
client_secret = creds['SPOTIPY_CLIENT_SECRET']
redirect_uri = creds['SPOTIPY_REDIRECT_URL']
scope = 'user-top-read user-library-read'


def main():
    (token, username) = authenticate()
    trackFeatures(token, username)


def authenticate():
    #Check for username
    if len(sys.argv) > 1:
        username = sys.argv[1]
        token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)
        if(token):
            print('User was authenticated successfully.')

            return(token, username)
            #trackFeatures(token, username)
        else:
            print("Authentication failed for ", username)
    else:
        print("Please specify a user to Authenticate" % (sys.argv[0]))
        sys.exit()

def trackFeatures(token, username):
    sp = spotipy.Spotify(auth=token)
    user = sp.user(username)
    recently_played = sp.current_user_top_tracks(limit=5)

    print('Track Name \t')
    for track in recently_played['items']:
        track_analysis = sp.audio_analysis(track['id'])
        track_features = sp.audio_features(track['id'])
        duration = track_features[0]['duration_ms']
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

        print(track['name'])
        #logging.debug('this is a message
    return


if __name__== "__main__":
  main()
