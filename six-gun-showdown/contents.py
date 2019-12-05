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
        print(subject)
        # print(self.actions[action])
        if action not in self.actions:
            print('Not an Action')
        elif getattr(self.actions[action], 'pockets', None) is not None:
            print('Allowed')
        else:
            print("Invalid Input")


locations = {
    "main_street": Location("Main Street", "", ["bottle"])
}

locations["main_street"].actions = {
    "examine": {
        "pockets": "You find your pa’s old silver sheriff’s badge and a copper penny. Your hands are shakin’ like the devil—seems a little hair of the dog is required. Fortunately, you still have that bottle back at home."
    }
}
