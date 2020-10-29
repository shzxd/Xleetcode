class Animal(object):
    def run(self):
        print('running')

class Dog(Animal):
    def run(self):
        print('Dog running')

class Cat(Dog):
    def run(self):
        print('Cat running')

Dog().run()
Cat().run()

a = Animal()
b = Dog()
print(isinstance(a, object))
print(isinstance(b, object))
print(isinstance(b, Animal))
print(isinstance(a, Dog))

'%s%s'%('Tik','Test')

