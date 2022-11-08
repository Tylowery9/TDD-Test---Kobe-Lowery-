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
        if self.type =="cat":
            if self.size =="small":
                return "meow"

            else: 
                return "MEOW!"

        
        if self.type =="dog":
            if self.size == "small":
                return "bow wow"
            
            elif self.size =="medium":
                return "Ruff ruff"
            
            else:
                return"arf arf"
            #if is small
                #return meow

        #I THINK THE PROBLEM IS HERE BECAUSE IT DOESN"T RETURN THE VALUE CORRECTLY
        
            
        #elif is ....
    
    def describe(self):
        if self.age < 10:
            return f"{self.name} is young"
        
        elif self.age >= 10:
            return f"{self.name} is old"

        #I think the issue is here because it is stuck in a repeating loop
        
                