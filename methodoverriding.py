from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def speak(self):
        print("I am a animal i make the sound") 
               
class Dog(Animal):
    def speak(self):
        super().speak()
        return"Woof!"
class Cat(Animal):
    def speak(self):
        return"Meow"   

animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak()) 
    
         

         
    
