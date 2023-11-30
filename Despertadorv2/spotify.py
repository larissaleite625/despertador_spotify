import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
import platform
import random

def verificar_spotify_aberto():
    sistema_operacional = platform.system()
    if sistema_operacional == 'Windows':
        os.system('start spotify')
    elif sistema_operacional == 'Darwin':  # macOS
        os.system('open -a "Spotify"')
    elif sistema_operacional == 'Linux':
        os.system('spotify &')
    else:
        print("Sistema operacional não suportado. Verifique se o Spotify está aberto.")

def reproduzir_playlist(playlist_uri):
    scope = 'user-modify-playback-state'
    redirect_uri = 'http://localhost:8888/callback'

    # Obter as credenciais do Spotify das variáveis de ambiente
    client_id = os.getenv('SPOTIPY_CLIENT_ID')
    client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, scope=scope, redirect_uri=redirect_uri))

    # Verifica se o Spotify está aberto e, se não estiver, abri-lo
    verificar_spotify_aberto()

    # Pausa a reprodução atual, se houver
    sp.pause_playback()

    # Obter as faixas da playlist
    results = sp.playlist_tracks(playlist_uri, fields="items(track(id))")
    tracks = results['items']

    if not tracks:
        print("A playlist não possui nenhuma música.")
        return

    # Escolher uma música aleatória da playlist
    random_track = random.choice(tracks)

    # Reproduzir a música aleatória
    sp.start_playback(uris=[random_track['track']['id']])

    # Verifica e ajusta o volume se estiver baixo
    sp.volume(100)  

__all__ = ['reproduzir_playlist', 'verificar_spotify_aberto']
