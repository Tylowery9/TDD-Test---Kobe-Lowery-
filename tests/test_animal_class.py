import unittest
from animal import Animal 

class Test_animal(unittest.TestCase):
    def test_animal_cat(self):
        animal1 = Animal("cat")
        if animal1.type == "cat":
            self.assertEqual(animal1.type, "Seymour")

    def test_animal_dog(self):
        animal2 = Animal("dog")
        if animal2 == "dog":
            self.assertEqual(animal2.type, "Spot")

    def test__animal_smallcat(self):
        animal3 = Animal("cat")
        if animal3 == "cat" and animal3 =="small":
            self.assertEqual( self.speak,"meow")

        else: 
            self.assertEqual(self.speak, "MEOW")


    def test_animal_smalldog(self):
        animal4 = Animal("dog")
        if animal4 == "dog" and animal4 =="small":
            self.assertEqual( self.speak, "bow wow")
        elif animal4 == "dog" and animal4 =="medium":
            self.assertEqual( self.speak, "ruff ruff")

        else: 
            self.assertEqual( self.speak,"arf arf")


    def test_animal_age(self):
        animal5 = Animal("dog")
        if animal5 < 10:
            self.assertEqual( self.describe,"name is young")

        else: 
            self.assertEqual( self.describe,"name is old")

    def test_animal_inputValue(self):
        animal6 = Animal("cat")
        if animal6 =="cat" and self.name == input():
            self.assertEqual(self.name, input())



    

