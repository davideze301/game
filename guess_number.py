import sys
import random


def guess_number(name='Playerone'):
    game_count = 0
    player_wins = 0
    
    def player_guess_number():
        nonlocal name
        nonlocal player_wins
        Playerchoice = input(
            f"\n{name}, guess which number I am thinking of... 1, 2, 3, or 4\n\n"
        )
        if Playerchoice not in ["1", "2", "3", "4"]:
            print(f"{name}, please enter 1, 2, 3, or 4.")
            return player_guess_number()
        
        computerchoice = random.choice("1234")
        print(f"\n{name}, You chose {Playerchoice}.")
        print(f"I was thinking about the number {computerchoice}.\n")
        
        Player = int(Playerchoice)
        computer = int(computerchoice)
        
        def decide_winner(Player, computer):
            nonlocal name
            nonlocal player_wins
            if Player == computer:
                player_wins += 1
                return f"🎉 {name}, Congratulation You won!👏👏👏👏"
            else:
                return f"{name}, Sorry you lose. Try again next time!"
        
        game_result = decide_winner(Player, computer)
        print(game_result)
        
        nonlocal game_count
        game_count += 1
        
        print(f"\nGame count: {game_count}")
        print(f"\n{name}'s wins: {player_wins}")
        print(f"\nYour winning percentage: {player_wins/game_count:.2%}")
        print(f"\nPlay again, {name}?")
        
        while True:
            playagain = input("\nY for yes\nQ for quit\n")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break
        if playagain.lower() == "y":
            return player_guess_number()
        else:
            print("\n🎉🎉🎉🎉")
            print("Thank you for playing!\n")
            if __name__ == "__main__":
                sys.exit(f"Bye {name}! 👋👋👋")
            else:
                return
    
    return player_guess_number()


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )
    
    parser.add_argument(
        '-n', '--name', metavar="name",
        required=True, help='The name of the person playing the game.'
    )
    args = parser.parse_args()
    guess_my_number = guess_number(args.name)
    guess_my_number()