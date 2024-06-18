import random

def win(user, comp):
    """
    Return all game play that is a win.
    """
    # r > s | p > r | s > p
    if (user == "r" and comp == "s") or (user == "p" and comp == "r") or (user == "s" == comp == "p"):
        return True
def play():
    """
    Return the number of ties, wins and losses of a Rock (r), Paper (p), and Scissors (s) game.

    Determine the final winner of the game round.
    """
    wins = 0
    losses = 0
    ties = 0
    
    while True:
        user = input("Pick a choice out of: 'r' for rock, 'p' for paper,"
                    " 's' for scissors. Enter 'q' to quit anytime: ")
        user = user.lower()
        comp = random.choice(["r", "p", "s"])

        if user in ("r", "p", "s", "q"):
            if user == "q":
                print("Thank you for playing\n")
                break
            elif user == comp:
                ties += 1
                print("It's a tie")
            elif win(user, comp):
                print("You win!")
                wins += 1
            else:
                losses += 1
                print("You lost")
        else:
            print("Wrong choice. Enter one of 'r', 's', 'p', or 'q'")
    
    print(f"\nThe game result is:\n\t- Wins = {wins}\n\t- Losses = {losses}\n\t- Ties = {ties}")
    if wins > losses:
        print("\nYou won the game round")
    elif (wins == 0) and (losses == 0) and (ties == 0):
        print("\nYou've not played")
    elif wins == losses:
        print("\nThe game is a tie")
    else:
        print("You lost the game round")   
        
play()