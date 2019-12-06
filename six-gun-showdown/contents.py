class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description


items = {
    'badge': Item("Pa’s badge", " Your pa’s badge. He was a good man who kept the peace in this town. You still remember the day a cattle rustler shot him in the back and took his life. ")
}


class Location:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items
        self.visited = False

    def roomEntered(self):
        if self.visited:
            print(f'You are back at the {self.name}')
        else:
            print(f"\n{self.description}")
        self.visited = True

    def printDesc(self):
        print(self.description)


locations = {
    "main_street": Location("Main Street", "You are back at Main Street", []),
    "rundown_shack": Location("Rundown Shack", "You stagger back home to your shack. Home sweet home. Pa’s pistol and holster are here, hanging on a hook. There’s a broken whiskey bottle on the floor.", []),
    "saloon": Location("Saloon", "Drinking in public was never your style, but desperate times call for desperate measures. You belly up to the bar. The bartender gives you a polite nod and continues to polish a shot glass. “What’ll it be?”", ["bottle"])

}

locations["main_street"].actions = {
    "examine": {
        "pockets": "\nYou find your pa’s old silver sheriff’s badge and a copper penny. Your hands are shakin’ like the devil—seems a little hair of the dog is required. Fortunately, you still have that bottle back at home.",
        "badge": "\nYour pa’s badge. He was a good man who kept the peace in this town. You still remember the day a cattle rustler shot him in the back and took his life.",
        "penny": "\nQuite literally your last cent. That, plus a dwindling line of credit at Cooper’s General Store, is the sum of your worldly fortune. "
    },
    'wear': {
        "badge": "\nThe tremor in your hands makes even this simple task impossible."
    },
    "move": {
        "north": locations['saloon'],
        "west": locations['rundown_shack']
    }
}

locations["rundown_shack"].actions = {
    "examine": {
        "pistol": "\nThat’s as fine a piece of steel as there ever was. You check the cylinder... and it’s still loaded, for old times’ sake. But your gunslinger days are far behind you.",
        'bottle': '\nYep, that might explain last night’s sleeping arrangements.'
    },
    "move": {
        "east": locations['main_street'],
        "out": locations['main_street']
    }
}

locations["saloon"].actions = {
    "examine": {
        'bottle': "\nNot the kind of drink you were after..."
    },
    "order": {
        "drink": "\nThe bartender says, “Sarsaparilla’s one cent, friend.” He won’t sell anything harder to a drunk like you.",
        'sarsaparilla': "\nYou pay, and the bartender slides the bottle down to you. You now have a bottle of sarsaparilla."
    },
    "drink": {
        "bottle": "\nMmm... refreshing. The bottle is now empty.",
        "sarsaparilla": "\nMmm... refreshing. The bottle is now empty.",
    },
    "move": {
        "south": locations['main_street']
    }
}
