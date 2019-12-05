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

    def __str__(self):
        return self.name

    def act(self, action, subject):
        print(action + subject)
        if action not in self.actions:
            print('Not an Action')
        elif getattr(self.actions[action], subject, None) is not None:
            print(self.actions[action][subject])
        else:
            print("Invalid Input")


locations = {
    "main_street": Location("Main Street", "", []),
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
        "north": locations['saloon']
    }
}
