class GameObject:
    def __init__(self, name):
        self.name = name
        self.position = (0, 0)
        self.rotation = 0

    def update(self):
        pass

    def render(self):
        pass


class Prop(GameObject):
    def __init__(self, name, position, rotation):
        super().__init__(name)
        self.position = position
        self.rotation = rotation

    def update(self):
        # Update logic specific to the prop
        pass

    def render(self):
        # Render prop on the screen
        pass


class GameEngine:
    def __init__(self):
        self.props = []

    def add_prop(self, prop):
        self.props.append(prop)

    def update(self):
        for prop in self.props:
            prop.update()

    def render(self):
        for prop in self.props:
            prop.render()


# Create the game engine
engine = GameEngine()

# Create props
prop1 = Prop("Prop1", (100, 100), 0)
prop2 = Prop("Prop2", (-50, 200), 45)

# Add props to the game engine
engine.add_prop(prop1)
engine.add_prop(prop2)

# Game loop
running = True
while running:
    # Update the game logic
    engine.update()

    # Render the game
    engine.render()

    # Handle user input and events

# Exit the game
