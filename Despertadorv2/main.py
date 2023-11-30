import datetime
import time
from spotify import reproduzir_playlist, verificar_spotify_aberto
import os

# Obter as credenciais do Spotify das variáveis de ambiente
client_id = os.getenv('SPOTIPY_CLIENT_ID')
client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')

# Defina a URI da playlist que deseja reproduzir
playlist_uri = 'spotify:playlist:4ldSeoFvJskVe5NmFUWhxf'

# Defina o horário de despertar
hora_despertar = datetime.datetime.now().replace(hour=15, minute=38)

# Verificar se o Spotify está aberto e, se não estiver, abri-lo
verificar_spotify_aberto()

# Loop até o horário de despertar ser alcançado
while True:
    agora = datetime.datetime.now()
    if agora >= hora_despertar and agora.weekday() < 5:  # Toca apenas de segunda a sexta-feira (0 a 4)
        reproduzir_playlist(playlist_uri)
        break
    else:
        print("AMIMIR...")
        time.sleep(60)  # Verifica a cada minuto
