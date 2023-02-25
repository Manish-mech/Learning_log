class Dog():
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"My dog name is {self.name.title()} ")

    def rollover(self,miles):
        print(f"My dog age is {self.age}, and he can {miles}")

class Pet(Dog):
    def __init__(self,name, age):
        super().__init__(name,age)
        self.name = name
        self.age = age

    def cat(self):
        return f"I have a cat her name is {self.name} and she is {self.age}"

p= Pet('tom',45)
p.sit()
p.rollover('rolly')

c = Pet('swetty',12)
print(c.cat())