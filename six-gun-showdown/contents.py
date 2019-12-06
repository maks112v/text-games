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
        if False:
            print(f'You are back at the {self.name}')
        else:
            print(f"\n{self.description}")
        self.visited


locations = {
    "main_street": Location("Main Street", "", []),
    "rundown_shack": Location("Rundown Shack", "You stagger back home to your shack. Home sweet home. Pa’s pistol and holster are here, hanging on a hook. There’s a broken whiskey bottle on the floor.", []),
    "saloon": Location("Saloon", "", ["bottle"])

}

locations["main_street"].actions = {
    "examine": {
        "pockets": "You find your pa’s old silver sheriff’s badge and a copper penny. Your hands are shakin’ like the devil—seems a little hair of the dog is required. Fortunately, you still have that bottle back at home.",
        "penny": "Quite literally your last cent. That, plus a dwindling line of credit at Cooper’s General Store, is the sum of your worldly fortune. "
    },
    'wear': {
        "badge": "The tremor in your hands makes even this simple task impossible."
    },
    "move": {
        "north": locations['saloon'],
        "west": locations['rundown_shack']
    }
}
