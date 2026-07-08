import random
choices= ["rock", "paper", "scissors"]




player_score = 0
computer_score = 0
while True:
    
    player= input("Choose rock, paper, and scissors: ").lower()
    if player not in choices:
        print("Invalid choice")
        continue
    computer= random.choice(choices)

    
    print(f"\nYou chose: {player}")
    print(f"Computer chose: {computer}")

    

    if player==computer:
        print("it's a tie")
    elif (player=="rock" and computer=="scissors") or (player=="paper" and computer=="rock") or (player=="scissors" and computer=="paper"):
        print("You Win")
        player_score += 1
    else: 
        print("Computer Win")
        computer_score += 1
    if player not in choices:
        print("Invalid choice")
        continue
    print("\nScore")
    print(f"You: {player_score}")
    print(f"Computer: {computer_score}")
    again= input("\n Play again? (yes/no)").lower()
    if again!="yes":
        print("Thanks for playing")
        break





