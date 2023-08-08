import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

date_required = input("Enter the date you would like to travel in format YYYY-MM-DD: ")
year = date_required.split('-')[0]
endpoint = f'https://www.billboard.com/charts/hot-100/{date_required}/'

response = requests.get(endpoint)
response.raise_for_status()
data = response.text

soup = BeautifulSoup(data, 'html.parser')

song_names_spans = soup.select("li ul li h3")

song_names = [song.getText().strip() for song in song_names_spans]
print(song_names)

scope = 'playlist-modify-private'
cache_path = 'token.txt'
redirect = 'https://open.spotify.com/'
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(), auth_manager=SpotifyOAuth(scope=scope,
                                                                                                      cache_path=cache_path,
                                                                                                      redirect_uri=redirect))
user_id = sp.current_user()['id']
print(f'user_id: {user_id}')


def playlist_exists(play_name):
    playlists = sp.user_playlists(user=user_id)
    for play in playlists['items']:
        print(f'playlist_name: {play["name"]}')
        if play['name'] == play_name:
            return True
    return False


playlist_name = f'{date_required} Top 100 Billboard songs'
song_uris = []
if not playlist_exists(playlist_name):
    playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False)
    play_id = playlist['id']
    print(f'play_id: {play_id}')
    for item in song_names:
        result = sp.search(q=f'track:{item} year:{year}', type='track', limit=1)
        try:
            song_id = result['tracks']['items'][0]['uri']
            song_uris.append(song_id)
        except IndexError:
            print(f'{item} does not exist in spotify. Skipped')

    sp.playlist_add_items(playlist_id=play_id, items=song_uris)
