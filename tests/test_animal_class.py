import unittest
from animal import Animal 

class Test_animal(unittest.TestCase):
    
    def test_animal_cat(self):
        #Given - If type is cat and no name, It's name is seymour 
        animal1 = Animal()
        animal1.type = "cat"
        #When 
        pass
        #Then - Assert that the blank cat property is named seymour 
        self.assertEqual(animal1.name, "Seymour")


    
    def test_animal_dog(self):
        #Given - If type is dog and no name, It's name is spot
        animal2 = Animal()
        animal2.type = "dog"
        #When
        pass
        #Then - Assert that the blank dog property is named spot
        self.assertEqual(animal2.name, "Spot")

    def test__animal_smallcat(self):
        #Given - If the type is cat and is it small, it will say meow 
        animal3 = Animal("cat")
        animal3.size = "small"
        #when - we call speak 
        words1 = animal3.speak()
        #Then - Assert that the small cat will say meow and now MEOW
        self.assertEqual(words1, "meow")

        #Given - If the type is cat and it is NOT small, it will say MEOW
        animal3_1 = Animal("cat")
        animal3_1.size = "medium"
        #when - We call speak
        words2 = animal3_1.speak()
        #Then - Assert that the medium cat will say MEOW 
        self.assertEqual(words2, "MEOW")


    def test_animal_smalldog(self):
       #Given - If the type is dog and it is small, it will say bow bow
       animal4 = Animal("dog")
       animal4.size = "small"
       #When - We call speak
       words3 = animal4.speak()
       #Then - Assert that the small dog will say bow bow
       self.assertEqual(words3, "bow wow")

       #Given - If the type is dog and it is medium, it will say ruff ruff
       animal4_1 = Animal("dog")
       animal4_1.size = "medium"
       #When - We call speak
       words4 = animal4_1.speak()
       #Then - Assert that the medium dog will say ruff ruff
       self.assertEqual(words4, "ruff")

       #Given - If the type is dog and it is NOT small OR medium, it will say arf arf
       animal4_2 = Animal("dog")
       animal4_2 = "large"
       #When - We call speak
       words5 = animal4_2.speak()
       #Then - Assert that the large dog will say arf arf 
       self.assertEqual(words5, "arf arf")

       




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



    

