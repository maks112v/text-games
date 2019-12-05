class Location:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items
        self.visited = False

    def examine(self, item):
        if getattr(self.actions["examine"], item):
            print('Allowed')


locations = {
    "main_street": Location("Main Street", "", ["bottle"])
}

locations["main_street"].actions = {
    "examine": {
        "pockets": "You find your pa’s old silver sheriff’s badge and a copper penny. Your hands are shakin’ like the devil—seems a little hair of the dog is required. Fortunately, you still have that bottle back at home."
    }
}
