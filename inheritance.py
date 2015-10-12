class Animal(object):
    def __init__(self,name):
        self.name = name

    def running(self):
        print "Animal is running"

class Dog(Animal):
    pass

class Cat(Animal):

    def __init__(self, name, length):
        self.name = name
        self.length = length

    def running(self):
        print 'Cat %s is running' % self.name


def runtwice(Animal):
    Animal.running()
    Animal.running()

dog = Dog('Sam')
dog.running()

cat = Cat('Lisa', 10)
cat.running()

runtwice(dog)
runtwice(cat)

