from colorama import init, Fore, Back, Style
init()
from libs import swapi_client
import msvcrt

class Player:
    def __init__(self, player_id, name, gender, power, lives, gems = 0): #Constructor de Python
        self.player_id = player_id
        self.name = name
        self.gender = gender
        self.power = power
        self.lives = lives
        self.gems = gems

class FightGame:
    DEFAULT_LIVES = 3
    DEFAULT_POWER = 10

    def __init__(self, author):
        self.author = author
        self.swapi = swapi_client.Swapi()
        self.players = [] #Lista vacia de los players que tendremos en nuestro juego
        self.last_player_id = 0

    def run(self):
        print(Fore.CYAN + """___________.__       .__     __      ________                       
\_   _____/|__| ____ |  |___/  |_   /  _____/_____    _____   ____  
 |    __)  |  |/ ___\|  |  \   __\ /   \  ___\__  \  /     \_/ __ \ 
 |     \   |  / /_/  >   Y  \  |   \    \_\  \/ __ \|  Y Y  \  ___/ 
 \___  /   |__\___  /|___|  /__|    \______  (____  /__|_|  /\___  >
     \/      /_____/      \/               \/     \/      \/     \/  by {}""".format(self.author))
        print(Fore.WHITE)
        self.__get_players()
        print('Pulsa 0 para obtener ayuda')

        while True:
            option = msvcrt.getch() #Voy a leer que tecla pulsa el usuario con la libreria msvcrt
            print(option) #b'\x1b' codigo de la tecla escape
            if option == b'\x1b':
                print('Shutting down..')
                break
            #Python no tiene switch, asi que hay que usar if's
            if option == b'0':
                self.__menu()
            elif option == b'1': #else if
                self.__add_player()
            elif option == b'2':
                self.__status()
            elif option == b'3':
                self.__fight()
        
    def __menu(self):
        print("Hi!, I'm the menu")
        print("\n\n Choose an option:\n")
        print(" 0. Show menu")
        print(" 1. Add New Player")
        print(" 2. Status")
        print(" 3. Fight!")
        print(" 4. Press Esc to exit")
    
    def __add_player(self):
        print('Add a player')

    def __status(self):
        for a in self.players:
            print(a.player_id, a.name, a.gender, a.power, a.lives, a.gems)

    def __fight(self):
        print("Let's fight!!")
    
    def __get_players(self):
        print('Obteniendo jugadores desde la api de Star Wars...')
        people = self.swapi.get_people()
        for character in people:
            self.last_player_id += 1
            player = Player(
                player_id = self.last_player_id,
                name = character[0],
                gender = character[1],
                power = FightGame.DEFAULT_POWER,
                lives = FightGame.DEFAULT_LIVES
            )
            self.players.append(player)        
        print('Players list ready!')    
        self.__status()

FightGame('Raúl').run()
#Forma larga de lo de arriba
#game = FightGame('Raúl')
#game.run()