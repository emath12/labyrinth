from GridLink import *

maze = GridLink()

print("Welcome to the Labyrinth.")
print("This is meant to be a brief demonstration of the functionality of my squarely linked list. It exists purely for example purposes.")
print("You have 4 options. You may go forward, left, right or back. Find the randomly placed treasure")
length = int(input("How many rooms would you like the maze to be?"))


maze.generate_labyrinth(length)

cur_room = maze.head
while cur_room:
    if cur_room.treasure == True:
        print("you found the treasure!")
        break

    print(f"You are in room {cur_room.id}")
    user_guess = input("Which way do you want to go?")

    if user_guess.lower() == "left":
        cur_room = cur_room.left
    elif user_guess.lower() == "right`":
        cur_room = cur_room.right
    elif user_guess.lower() == "forward":
        cur_room = cur_room.next
    elif user_guess.lower() == "back":
        cur_room = cur_room.prev
    else:
        print("invalid entry!, Try again")

print("you died! you entered an invalid room")





