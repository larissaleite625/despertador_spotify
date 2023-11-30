<<<<<<< HEAD
import datetime
import time
from spotify import reproduzir_musica
import os
import random

# Obter as credenciais do Spotify das variáveis de ambiente
client_id = os.getenv('SPOTIPY_CLIENT_ID')
print(os.getenv('SPOTIPY_CLIENT_SECRET'))
client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')

# National Anthem of USSR, Katioucha, The Red Army Is the Strongest, Katyusha, Moskau, Kamaz
leninista = ['0JRoo5kkeboyTWVdMEU3pw', '19RdiPkl18jXVfnvMaZBQV', '1dGaFOpHvz5fm45rQSYeKC', '5rRAOgZOAqHwUMwVAXkUYU', '4m7p2dejJrMiiA1vg8LDPK', '5ndylO3VZAhTRIARJFD0a5', '1CY57Jb3btf0qYXSqRC9Dm']

#Violent Revolution, Killing In The Name, No Gods, No Masters
rockista_comunista = ['712ukvLX20rwHuTWg7Gcjb', '59WN2psjkt1tyaxjspN8fp', '2SR0CHOWgkVt0nLI9YwYti'] 

#All These Things I Hate, Trust, Dead Memories
rockista_corna = ['6XimI1O15wpfwUdrCnlrxo', '5emb8RDOZtpXlw6D0eEQbz', '7eRG7KNDIgjIk3nvykmhOT'] 

#ALIEN SUPERSTAR, Born This Way, Man Down
fa_de_diva_pop = ['1Hohk6AufHZOrrhMXZppax', '30XU4suKzCeoCK9YFzdufg', '1Bx0zEdVjkFlV27iKaePug']

#Under Again, Somewhere I Belong, A Tout Le Monde
suicida = ['5DayxZpAgBVDCNFjQHWi4g', '3fjmSxt0PskST13CSdBUFx', '6olS0TmHmsGr0hXtcBsiVM']

#Maneiras, Quem É Ela, Se Eu Encontrar Com Ela, A Semente
sambinha = ['1eQpKqH1sEecyiTKEXuErI', '2U2o8eV1nNakQ5h8Jkb17C', '5gZP6CS1CvDK9xGShd1fDv', '7mKFzy9cFV6fbIIVD3rSp9']

# Festa de Camdomblé, Ponto do Caveira, Insumbu ê
macumba = ['26DdzdTwXHOAC0rBO0EqVs', '42FtlJ79dsZjMd1yFFfnoB', '7ETJYnm4I35rHyQhxXiHeV']

#Capítulo 4, Versículo 3, Nego Drama, Marighella
racionais = ['6Wt61AZLG0bN2KasopE2sj', '3ytXzEJFeVydFfmUhHvti8', '5MYKqp6J8rstffAQBCE2nl']

# Rase Your Horns, Are You Dead Yet?, Under Black Flags We March
death_metal = ['5gNyrx8elXaXXs3vFC1ufZ', '52s05aBQd2LVc6EWIQCQI1', '3w9DBYm53qG0dnVdXit9nr']

#Disposable Heroes, Set the World Afire, People of the Lie
thrash_metal = ['4tPHBRIPsB55nssjvKDbjj', '2TLNPA3qCpcVor2cuMZ3RA', '4YgUZqOat2UyeHjLCJJ8tr']

#In Nomine Dei Nostri, Χ Ξ Σ - 666, The Deathless Sun
black_metal_nervoso = ['4bAHMUnHX1jMoLOpMSUF4w', '3P4Vcz7MhJngRf8WUAaoA0','6b0HdwX9k0RtOUHRvWYl4J']


lista = [leninista, rockista_comunista, rockista_corna, fa_de_diva_pop, suicida, sambinha, macumba, racionais, death_metal, thrash_metal, black_metal_nervoso]
lista_selecionada = random.choice(lista)
musica = random.choice(lista_selecionada)
# Defina a URI da música que deseja reproduzir
vai = 'spotify:track:' + str(musica)
print(vai)

# Defina o horário de despertar
hora_despertar = datetime.datetime(2023, 10, 6, 7, 0)  #ano, mes, dia, hora e min

# Loop até o horário de despertar ser alcançado 

while True:
    agora = datetime.datetime.now()
    if agora >= hora_despertar:
        reproduzir_musica(vai)
        break
    else:
        print("Amimir")
        time.sleep(180)  # 3 min e ele verifica de novo
=======
import datetime
import time
from spotify import reproduzir_musica
import os
import random

# Obter as credenciais do Spotify das variáveis de ambiente
client_id = os.getenv('SPOTIPY_CLIENT_ID')
print(os.getenv('SPOTIPY_CLIENT_SECRET'))
client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')


leninista = ['0JRoo5kkeboyTWVdMEU3pw', '19RdiPkl18jXVfnvMaZBQV', '1dGaFOpHvz5fm45rQSYeKC', '5rRAOgZOAqHwUMwVAXkUYU', '4m7p2dejJrMiiA1vg8LDPK', '5ndylO3VZAhTRIARJFD0a5', '1CY57Jb3btf0qYXSqRC9Dm']
rockista_comunista = ['712ukvLX20rwHuTWg7Gcjb', '59WN2psjkt1tyaxjspN8fp', '2SR0CHOWgkVt0nLI9YwYti'] 
rockista_corna = ['6XimI1O15wpfwUdrCnlrxo', '5emb8RDOZtpXlw6D0eEQbz', '7eRG7KNDIgjIk3nvykmhOT'] 
fa_de_diva_pop = ['1Hohk6AufHZOrrhMXZppax', '30XU4suKzCeoCK9YFzdufg', '1Bx0zEdVjkFlV27iKaePug']
suicida = ['5DayxZpAgBVDCNFjQHWi4g', '3fjmSxt0PskST13CSdBUFx', '6olS0TmHmsGr0hXtcBsiVM']
sambinha = ['']
macumba = ['']
racionais = ['']
death_metal = ['']
thrash_metal = ['']
black_metal_nervoso = ['4bAHMUnHX1jMoLOpMSUF4w', '3P4Vcz7MhJngRf8WUAaoA0','6b0HdwX9k0RtOUHRvWYl4J']


lista = [leninista, rockista_comunista, rockista_corna, fa_de_diva_pop, suicida, sambinha, macumba, racionais, death_metal, thrash_metal, black_metal_nervoso]
lista_selecionada = random.choice(lista)
musica = random.choice(lista_selecionada)
# Defina a URI da música que deseja reproduzir
vai = 'spotify:track:' + str(musica)
print(vai)

# Defina o horário de despertar
hora_despertar = datetime.datetime(2023, 10, 6, 7, 0)  #ano, mes, dia, hora e min

# Loop até o horário de despertar ser alcançado 

while True:
    agora = datetime.datetime.now()
    if agora >= hora_despertar:
        reproduzir_musica(vai)
        break
    else:
        print("Amimir")
        time.sleep(180)  # 3 min e ele verifica de novo
>>>>>>> dea7fc3c04e5b894aadbe8d51f2be9f94d57ca82
