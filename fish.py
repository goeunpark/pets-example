from pet import Pet

class Fish(Pet):
    def __init__(self, name, age, size):
        super().__init__(name, age)
        self.size = size

    def beg(self):
        return "Glub, glub!"