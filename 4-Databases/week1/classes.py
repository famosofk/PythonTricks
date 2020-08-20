class PartyAnimal:
    x = 0
    name = ''
    def party(self):
        self.x = self.x + 1
        print('so far', self.x)

    def __init__(self, nam):
        self.name = nam
        print("ola")
    def __del__(self):
        print('tchau')

class FootballFan(PartyAnimal):
    tochdowns = 0

an = PartyAnimal("Fabin")
an.party()
ff = FootballFan("Cleiton")


    