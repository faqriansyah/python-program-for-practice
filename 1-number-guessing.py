import random

class Chance:
    
    def __init__(self):
        self.chance = 10
        
    def resetChance(self):
        self.chance = 10
    
    def reduceChance(self):
        self.chance -= 1
        
    def getChance(self):
        return self.chance
    
    def checkChance(self):
        if self.chance <= 1:
            return False
        else:
            return True
    
class Randomizer:

    def getNumber(self):
        return self.number
    
    def randomize(self):
        self.number = random.randint(1, 100)

def checkAnswer(number: int, answer: int):
    
    if number != answer:
        
        if number > answer:
            return 2
        else:
            return 0
        
    else:
        return 1

# Play In Cli
def mainCli():
    
    chance = Chance()
    randomizer = Randomizer()
    
    # Init
    randomizer.randomize()

    print("Welcome to Number Guess Game\nWe generate random number for you!, guess from 1 to 100! You Have 10 Chance!")
            
    print("Games Begin!")
    
    while True:

        print("Guess the number!  ")
        answer = int(input("> "))
        

        if chance.checkChance():
            if answer > randomizer.getNumber():
                chance.reduceChance()
                print(f"To Large! Try Again! Chance {chance.getChance()}")

            elif answer < randomizer.getNumber():
                chance.reduceChance()
                print(f"To Low! Try Again! Chance {chance.getChance()}" )

            elif answer == randomizer.getNumber():
                print(f"Congratulations! You Are Right, Game restarted!")
                randomizer.randomize()
                chance.resetChance()

        else:
            print(f"Game over! the correct answer is {randomizer.getNumber()}, Game restarted!")
            randomizer.randomize()
            chance.resetChance()
            
    
if __name__ == "__main__":
    mainCli()
        
        
        
        
        
        
        