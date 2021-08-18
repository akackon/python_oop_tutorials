class HumanBeing():
    def __init__(self,name,race, tall = True):
        self.name = name
        self.race = race
        self.tall = tall
        self.sexy = True
        

    def __repr__(self):
        return f"{self.name} is sexy: {self.sexy}"

    def blink(self, action):
        print(f"To {action}:")
        print("Close your eyes.")
        print("Open them")

    def attract(self):
        self.blink("attract")


def main():
    person1 = HumanBeing("David","blue")
    print(person1)
    person1.blink("blink")
    person1.attract()



# The code to be run
if __name__ == "__main__":
    print("I'm about to run the code\n")
    main()