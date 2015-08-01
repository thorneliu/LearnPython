#fisrt class defination

class Student(object):
    
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print '%s: %s' %(self.__name, self.__score)

    def getname(self):
        return self.__name

    def getscore(self):
        return self.__socre

    def getheight(self):
        return self.__height
    def setheight(self,height):
        self.__height = height

q9liu = Student('q9liu', 88)
h23wang = Student('h23wang', 22)

q9liu.setheight(160)

print q9liu.getheight()

q9liu.print_score()
h23wang.print_score()
