class Person:
    nationality = "Brazilian"
    def set_name(self, new_name):
        self.name = new_name
    def set_age(self, new_age):
        self.age = new_age

def split_title_and_name(person):
    title = person.name.split()[0]
    lastname = person.name.split()[-1]
    return '{} {}'.format(title, lastname)

p = Person()
p.set_name("Dr. Fabiano Gomes")

print(split_title_and_name(p))