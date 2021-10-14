import random
#list of possible choices
choice = ["rock" , "paper" , "scissors"]
while True:
    print("Rock, paper or scissors?\n")
    player_choice = input()
    if player_choice in choice:
        computer_choice = random.choice(choice)
        print("Computer choose: \n",computer_choice )
        print ("Player choose: ",player_choice)
    else:
        print("You did not make a valis choice")

    if player_choice == computer_choice:
        print("Tie!")
    elif player_choice == "rock":
        if computer_choice == "paper":
            print("You lost!")
        if computer_choice == "scissors":
            print("You win!")
    elif player_choice == "paper":
        if computer_choice == "rock":
            print("You win!")
        if computer_choice == "scissors":
            print("You lost!")
    elif player_choice == "scissors":
          if computer_choice == "rock":
            print("You win!")
          if computer_choice == "paper":
            print("You lost!")
      
print("\nGoodbye")
