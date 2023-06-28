import datetime
import time
from spotify import reproduzir_musica
import os

# Obter as credenciais do Spotify das variáveis de ambiente
client_id = os.getenv('SPOTIPY_CLIENT_ID')
print(os.getenv('SPOTIPY_CLIENT_SECRET'))
client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')

# Defina a URI da música que deseja reproduzir
music_uri = 'spotify:track:2HLY1qDaWKodXeR6FQJQux'

#music_uri = 'spotify:track:0mKGwFMHzTprtS2vpR3b6s' 
#ID de Cozy
#https://open.spotify.com/intl-pt/track/0mKGwFMHzTprtS2vpR3b6s?si=d23274c76516460b
#Link pra Cozy


# Defina o horário de despertar
hora_despertar = datetime.datetime(2023, 6, 28, 17, 51)  #27 de junho de 2023, 7:30 AM

# Loop até o horário de despertar ser alcançado
while True:
    agora = datetime.datetime.now()
    if agora >= hora_despertar:
        reproduzir_musica(music_uri)
        break
    else:
        print("Ainda não é hora de acordar. Verificando novamente em 10 min...")
        time.sleep(600)  # Aguarda 10 min antes de verificar novamente
