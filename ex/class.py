class Person:
    nationality = "Brazilian"
    def set_name(self, new_name):
        self.name = new_name
    def set_age(self, new_age):
        self.age = new_age

person = Person()
person.set_name("fabin")
person.set_age(22)

dados = "Meu nome é {} e eu tenho {} anos.".format(person.name, person.age)
print(dados)

people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
    title = person.split()[0]
    lastname = person.split()[-1]
    return '{} {}'.format(title, lastname)

list(map(split_title_and_name, people))
