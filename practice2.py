class Human:
    def __init__(self, n, o, i):
        self.name = n
        self.occupation = o
        self.interests = i

        #methods
    def do_work(self):
            if self.occupation == "engineer":
                print(self.name, "is an engineer")
            elif self.occupation == "doctor":
                print(self.name, "treats people")

    def hobbies(self):
            if self.interests == "watching anime":
                print(self.name, "watches animix play")
            elif self.interests == "watching movies":
                print(self.name, "watches flixwave")


    def speaks(self):
            print("says hello ")


#objects/instance
sam = Human("stanlee", "engineer", "watching anime")
sam.do_work()
sam.hobbies()
sam.speaks()