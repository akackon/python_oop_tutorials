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

class Boys(HumanBeing):
    def __repr__(self):
        return f"{self.name} is ugly: {self.sexy}"
    


def main():
    person1 = HumanBeing("David","blue")  # person1 is an instance of HumanBeing() class
    print(person1)
    person1.blink("blink")
    person1.attract()
    person2 = Boys("Qhouamy","Asian")
    person2.blink("blink")
    person2.attract()
    print(person2)



# The code to be run
if __name__ == "__main__":
    print("I'm about to run the code\n")
    main()