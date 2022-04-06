from pet import Pet
from components.paw import Paw
from components.nose import Nose

# L5-6 shows that we are imp an Inheritance
class Dog(Pet): 
    def __init__(self, name, age, color, vaccinated=True):
        super().__init__(name, age)
        self.color = color
        self.vaccinated = vaccinated
        # L11 is an example of Composition
        self.paw = Paw()
        self.nose = Nose()
        
    def beg(self):
        return "Bark, bark!"