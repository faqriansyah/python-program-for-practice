# This Python program is a simple number-guessing game, where the user tries to guess a random number
# between 1 and 100 within a limited number of attempts. Two main classes, `Chance` and `Randomizer`, 
# are used to manage the game state, including the user's remaining attempts and the random number generation.

# Import the random module to generate a random number
import random
import kivy

# Define the Chance class to manage the number of attempts (or chances) a player has to guess correctly
class Chance:
    
    def __init__(self):
        # Initialize the default number of chances to 10
        self.chance = 10
        
    def setChance(self, chance):
        # Method to explicitly set the number of chances, allowing for flexibility in adjusting the game difficulty
        self.chance = chance
    
    def reduceChance(self):
        # Method to reduce the number of chances by 1 each time the player makes an incorrect guess
        self.chance -= 1
        
    def getChance(self):
        # Method to retrieve the current number of remaining chances
        return self.chance
    
    def checkChance(self):
        # Method to check if the player has any chances left.
        # Returns False when chances reach 0, otherwise returns True
        return self.chance > 0

# Define the Randomizer class to handle the random number generation for the game
class Randomizer:

    def getNumber(self):
        # Method to retrieve the generated random number for comparison with the player's guess
        return self.number
    
    def randomize(self):
        # Method to generate a random integer between 1 and 100, setting it as the number to be guessed
        self.number = random.randint(1, 100)

# Function to check if the player's guess matches the random number
def checkAnswer(number: int, answer: int):
    # This function returns:
    # - 2 if the guess is too low
    # - 0 if the guess is too high
    # - 1 if the guess is correct
    if number != answer:
        if number > answer:
            return 2
        else:
            return 0
    else:
        return 1

# Main function to play the game in the Command Line Interface (CLI)
def mainCli():
    
    # Create instances of Chance and Randomizer to manage attempts and random number generation
    chance = Chance()
    randomizer = Randomizer()

    # Initialize the number of chances to 10 and generate a random number
    chance.setChance(chance=10)
    randomizer.randomize()

    # Infinite loop to keep the game running until the correct answer is guessed or chances run out
    while True:

        # Define various messages to be displayed based on the player's guess
        yourChance = f"Your Chance Remaining {chance.getChance() - 1}"
        toHigh = f"To High! {yourChance}"
        toLow = f"To Low! {yourChance}"
        correctAnswer = f"Congratulations! The Answer is {randomizer.getNumber()}"
        noChance = f"Game Over! The Correct Answer is {randomizer.getNumber()}"

        # Check if there are chances left to continue playing
        if chance.checkChance():

            # Prompt the player to enter their guess
            answer = int(input("> "))

            # Check if the guess is higher than, lower than, or equal to the generated number
            if answer > randomizer.getNumber():
                chance.reduceChance()    # Reduce chance if guess is too high
                print(toHigh)
            
            elif answer < randomizer.getNumber():
                chance.reduceChance()    # Reduce chance if guess is too low
                print(toLow)

            elif answer == randomizer.getNumber():
                # Reset the game if the guess is correct, setting chances to 10 and generating a new number
                chance.setChance(10)
                randomizer.randomize()
                print(correctAnswer)
        
        else:
            # If chances are exhausted, reset the game with a new random number and chance count
            chance.setChance(10)
            randomizer.randomize()
            print(noChance)

def main():
    ...

# Entry point of the program; the game starts if the script is run directly
if __name__ == "__main__":
    mainCli()
