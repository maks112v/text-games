from contents import locations
from contents import items


class Game:
    def __init__(self):
        self.active = True
        self.moves = 0
        self.score = 0
        print("\nWelcome to 6 Gun Showdown!\n")
        print('You’re fresh out of the drunk tank, down to a pair of worn leather boots and whatever’s left in your pockets. The saloon and general store are here. Your shack is to the west. A road leads south to the edge of town.')
        self.waitToContinue()
        print('You have a badge, a penny and a pair of leather boots.\n')
        print('Exits are north, south, east, and west.')
        print('To travel type `move [direction]` or type `help`')

    def endGame(self):
        self.active = False
        print(
            f"Your score was {self.score}\nYou survived for {self.moves} moves")

    def incrementMoves(self):
        self.moves = self.moves + 1

    def getHelp(self):
        print(
            "\nmove [direction]: Help you move around the map.\nexamine [object]: Used to look at objects around you.\nme: Get more info about your progress\nType exit to leave at any time\n")

    def waitToContinue(self):
        input('\nPress Enter to continue...\n')


class Player(Game):
    def __init__(self, name, current_room, inventory):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory
        super().__init__()

    def __str__(self):
        print(
            f'You are at {self.current_room.__str__()} with a score of {self.score}')


name = ""
while len(name) < 1:
    name = input('\nWhat is your name?\n> ')

current_player = Player(name, locations["main_street"], [items["badge"]])

commands = {
    'me': current_player.__str__,
    "help": current_player.getHelp,
    "exit": current_player.endGame
}

actions = ['move', "examine"]

while current_player.active:
    command = [x for x in input('\n> ').split(' ') if x]
    print(command)
    current_player.incrementMoves()
    if command[0] in commands:
        commands[command[0]]()
    elif command[0] in actions:
        if len(command) > 1:
            current_player.current_room.act(command[0], command[1])
        else:
            print("Try to give a full command")
    else:
        print("Invalid Action.\nYou can type `help` to get more options")
    # if action == "exit":
    #     current_player.endGame()
