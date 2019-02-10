'''
Day - 4
Link : https://www.hackerrank.com/challenges/30-class-vs-instance/problem

'''

#  Accepted Solution :

class Person:
    teen_max = 17
    young_max = 12
    teen_min = 13


    def __init__(self,initialAge):
        if initialAge < 0:
            print("Age is not valid, setting age to 0.")
            self.age = 0
        else:
            self.age = initialAge

    def amIOld(self):
        response = ""
        if self.age in range(Person.young_max + 1):
            response = "You are young."
        elif self.age in range(Person.teen_min,Person.teen_max+1):
            response = "You are a teenager."
        else:
            response = "You are old."
        print(response)


    def yearPasses(self):
        self.age += 1


#############################################################################
#----------------------------- begin locked code ---------------------------#
t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")
