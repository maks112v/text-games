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
        print('Hint: Use the `examine [object]` to take a closer look\n')
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

    def __getattr__(self, name):
        if name in self:
            return self[name]
        else:
            raise AttributeError("No such attribute: " + name)

    def __str__(self):
        print(
            f'You are at {self.current_room.name} with a score of {self.score} out of 100')

    def act(self, action, subject):
        try:
            selectedAction = self.current_room.actions[action] if action in self.current_room.actions else None
            if selectedAction is None:
                print('Invalid Action')
            elif subject not in selectedAction:
                print(
                    f'{action} {subject} is not a valid action try: {action} {commandHelp[action]}')
            elif action == "move":
                self.moveRooms(selectedAction[subject])
                self.current_room.roomEntered()
            else:
                print(selectedAction[subject])
        except:
            print("Invalid Action")

    def moveRooms(self, room):
        self.current_room = room


name = ""
while len(name) < 1:
    name = input('\nWhat is your name?\n> ')

current_player = Player(name, locations["main_street"], ["badge"])

commands = {
    'me': current_player.__str__,
    "help": current_player.getHelp,
    "exit": current_player.endGame
}

actions = ['move', "examine", "wear", "order", "drink"]

commandHelp = {
    "move": "[direction]",
    'examine': '[object]',
    'wear': '[object]',
    'order': '[item]',
    "drink": '[item]'
}

while current_player.active:
    command = [x.lower() for x in input('\n> ').split(' ') if x]
    current_player.incrementMoves()
    if len(command) > 0 and command[0] in commands:
        commands[command[0]]()
    elif len(command) > 0 and command[0] in actions:
        current_player.incrementMoves()
        if len(command) > 1:
            current_player.act(
                command[0], command[1])
        else:
            print(f"Try Again: {command[0]} {commandHelp[command[0]]}")
    else:
        print("Invalid Action.\nYou can type `help` to get more options")
