class Paw():
    foo = "bar"
    def __init__(self, nail=True, color=None):
        self.nail = nail
        self.color = color

    def swipe_for_food(self):
        return "Attempts to swipe!"