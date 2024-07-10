"""We are going to write a program that generates a random number and asks the user to 
guess it. 
If the player’s guess is higher than the actual number, the program displays “Lower 
number please”. Similarly, if the user’s guess is too low, the program prints “higher 
number please” When the user guesses the correct number, the program displays the 
number of guesses the player used to arrive at the number."""

from random import randint

def guess(a):
    count = 0
    while True:
        b = int(input("Guess a number from 1 - 100: "))
        if b == a:
            print("You got it right!")
            count += 1
            break
        elif b > a:
            print("Your guess is too high.")
            print("Please guess a number less than that.")
            count += 1
        elif b < a:
            print("Your guess is too low.")
            print("Please guess a number greater than that.")
            count += 1
        else:
            print("You must enter an integer value between 1 and 100.")
    return count

if __name__ == "__main__":
    user1_count = guess(randint(1, 100))
    user2_count = guess(randint(1, 100))
    if user1_count < user2_count:
        print(f"User 1 wins with {user1_count} guesses!")
    elif user2_count < user1_count:
        print(f"User 2 wins with {user2_count} guesses!")
    else:
        print("It's a tie!")
    print (f"The number of guesses made by user1 is {user1_count} and user 2 is {user2_count} ")
