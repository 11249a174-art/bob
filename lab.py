class Animal:
    def speak(self):
        print("Animals can make sounds")

class Dog(Animal):
    def bark(self):
        print("Dog bark")
class puppy(Dog):
    def weep(self):
         print("puppy weeps")
obj =puppy()

obj.speak()
obj.bark()
obj.weep()