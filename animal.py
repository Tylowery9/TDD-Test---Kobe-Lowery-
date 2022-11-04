class Animal():
    def init(self, ctype):
        self.type = ctype
        self.size = ""
        self.age = 0
        self.name = ""

        if self.type == "cat":
            self.name = "Seymour"

    def speak(self):
        pass
    
    def describe(self):
        pass