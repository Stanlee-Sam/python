class Human: 
    #properties 
    def __init__(self, n, o, i): #will initialize the properties
        self.name = n
        self.occupation = o
        self.interest = i

    #methods
    def do_work(self):
        if self.occupation == "tennis player":
            print(self.name, "plays tennis")
        elif self.occupation == "actor":
            print(self.name, "shoots a film")

    def hobbies(self):
        if self.interest == "watching movies":
            print(self.name, "watches movies")
        elif self.interest == "bike riding":
            print(self.name, "rides a bike")

    def speaks(self):
        print(self.name, "says how are you?")

#object/instances
tom = Human("tom cruise", "actor", "watching movies")
tom.do_work()
tom.hobbies()
tom.speaks()