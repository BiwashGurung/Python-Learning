from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def move(self):
        pass
class Human(Animal):
    def move(self):
        print("Move with legs")
class Snake(Animal):
    def move(self):
        print("Crawl") 

animals = [Human(),Snake()]
for animal in animals:
    print(animal.move())                   