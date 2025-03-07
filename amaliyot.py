
class Person:
    def __init__(self,age, name,gender,weight):
        self.age=age
        self.name=name
        self.gender=gender
        self.wieght=weight
    def speak(self,word):
        print(f"{self.name} odam gapirdi >>> {word} <<<")
person1=Person(25,"Berdishukur",True,83)
person2=Person(14,"Bahodir",True,60)
person1.speak("Salom")
# print(person1.name)
# print(person2.name)
