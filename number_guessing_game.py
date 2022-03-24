import random

random_number = random.randint(0, 101)
guess_number = 0

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

def guessing(guess_number):
    print(f"You have {guess_number} attempts remaining to guess the number.")
    guess = int(input("Make a guess. "))
    while guess_number > 0:
        if guess_number == 1:
            print(f"You ran out of guess attempts. The number was {random_number}. Game over.")
            break
        elif guess < random_number:
            print("Too low.")
            guess_number -= 1
            print(f"You have {guess_number} attempts remaining to guess the number.")
        elif guess > random_number:
            print("Too high.")
            guess_number -= 1
            print(f"You have {guess_number} attempts remaining to guess the number.")
        elif guess == random_number:
            print(f"{guess} was the number! You won!")
            break
        guess = int(input("Make a guess. "))

def easy():
    guessing(10)
    
def hard():
    guessing(5)

if difficulty == "easy":
    easy()
elif difficulty == "hard":
    hard()
else:
    print("That is not an option. Try again.")
