# .../Dev/character_creation_module/main.py

class Character:
    # Объявляем конструктор класса.
    def __init__(self, name):
        self.name = name
    
   # Объявляем метод атаки
    def attack(self):
        ...
    
    # Объявляем метод защиты.
    def defence(self):
        ...
    
    # Объявляем метод специального умения.
    def special(self):
        ...

class Warrior(Character):
    ...

class Mage(Character):
    ...

class Healer(Character):
    ...