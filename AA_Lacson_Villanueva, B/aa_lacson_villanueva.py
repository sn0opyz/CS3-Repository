class Plant:
    def __init__ (self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def attack (self, zombie):
        print (f"{self.name} attacks {zombie.name} with {self.damage} damage.")
        
    def take_damage (self, amount):
        self.take_damage -= self.health
        if self.health < 0:
            self.health = 0
        print (f"{self.name} takes {self.amount} damage.")
        
class Zombie:
    def __init__ (self, name, health, damage, distance):
        self.name = name
        self.health = health
        self.damage = damage
        self.distance = distance

    def move (self, distance):
        self.distance = distance
        print(f"{self.name} moves {self.distance} towards the plants.")

    def attack (self, plant):
        print(f"{self.name} attacks {plant.name} with {self.damage}.")
        self.take_damage(self.damage)
        

    def take_damage (self, amount):
        if self.health > 0:
            self.health - self.take_damage == self.health
        print (f"{self.name} takes {self.amount} damage.")
      

def run_game():
    plant1 = Plant("Charles_Cabbage", 100, 15)
    plant2 = Plant("Peter Peashooter", 100, 35)

    zombie = Zombie("Barney", 100, 50, 2)

    turn = 1

    while True:
        print(f"Turn {turn}")

        if plant1.health > 0:
            plant1.attack(zombie)

        if zombie.health == 0:
            print(f"{zombie.name} was defeated!")
            return

        if plant2.health > 0:
            plant2.attack(zombie)

        if zombie.health == 0:
            print("The plants saved the day!")
            return

        if plant1.health > 0:
            target = plant1
        else:
            target = plant2

        if zombie.distance > 0:
            zombie.move()
        else:
            zombie.attack(target)

        if plant1.health == 0 and plant2.health == 0:
            print("Both plants were eliminated. Zombie rules! >:)")
            return

    turn += 1

if __name__ == "__main__":
    run_game()