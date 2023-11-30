<<<<<<< HEAD
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

def reproduzir_musica(vai):
    scope = 'user-modify-playback-state' 
    # Escopo de permissão para modificar o estado de reprodução
    redirect_uri = 'http://localhost:8888/callback' 
    # Sua URI de redirecionamento personalizada

    # Obter as credenciais do Spotify das variáveis de ambiente
    client_id = os.getenv('SPOTIPY_CLIENT_ID')
    client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, scope=scope, redirect_uri=redirect_uri))

    sp.start_playback(uris=[vai])

     # Verifica e ajusta o volume se estiver baixo
    sp.volume(100)  # Define um limite de volume (exemplo: 50)

__all__ = ['reproduzir_musica']
=======
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

def reproduzir_musica(vai):
    scope = 'user-modify-playback-state' 
    # Escopo de permissão para modificar o estado de reprodução
    redirect_uri = 'http://localhost:8888/callback' 
    # Sua URI de redirecionamento personalizada

    # Obter as credenciais do Spotify das variáveis de ambiente
    client_id = os.getenv('SPOTIPY_CLIENT_ID')
    client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, scope=scope, redirect_uri=redirect_uri))

    sp.start_playback(uris=[vai])

     # Verifica e ajusta o volume se estiver baixo
    sp.volume(100)  # Define um limite de volume (exemplo: 50)

__all__ = ['reproduzir_musica']
>>>>>>> dea7fc3c04e5b894aadbe8d51f2be9f94d57ca82
