class Animal():
    def __init__(self, ctype):
        self.type = ctype
        self.size = ""
        self.age = 0
        self.name = ""

        if self.type == "cat":
            self.name = "Seymour"

        if self.type == "dog":
            self.name = "Spot"

        
#WORK ON THIS
    def speak(self):
        #if is cat
        if self.type == cat:
            print("MEOW")
            if self.size == "small":
                print("meow")
            #if is small
            if self.size == "small":
                print("meow") 
                #return meow
            return self.speak(self)
        #elif is ....
        pass
    
    def describe(self):
        pass