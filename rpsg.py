import sys
import random
from enum import Enum

def rpsg(name='Playerone'):
    game_count=0
    player_wins=0
    python_wins=0
    def play_rpsg():
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins
        
        class RPSG(Enum):
           ROCK =1
           PAPER =2
           SCISSORS =3
           GUM=4
        playerchoice=input(f"\n{name},please enter...\n1 for rock,\n2 for paper,\n3 for scissors\n4 for gum:\n\n")
        if playerchoice not in ["1","2","3","4"]:
            print(f"{name},Please you must enter 1,2,3or4.")
            return play_rpsg()
        player=int(playerchoice)
        if player <1 or player>4:
            sys.exit()
    
        computerchoice=random.choice("1234")
        computer=int(computerchoice)
        print(f"\n{name},you choose{str(RPSG(player)).replace('RPSG.','').title()}.")
        print(f"Python choose {str(RPSG(computer)).replace('RPSG.','').title()}.\n")
        def decide_winner(player,computer):
            nonlocal name
            nonlocal player_wins
            nonlocal python_wins
            if player == 1 and computer == 4:
                player_wins+=1
                return f"🎉{name},you win!"
            elif player == 3 and computer == 2:
                player_wins +=1
                return f"🎉{name},you win!"
            elif player == 1 and computer == 4:
                player_wins +=1
                return f"🎉{name},you win!"
            elif player == computer:
                return"😲Tie  game!"
            else:
                python_wins +=1
                return f"🐍 python wins!\n Sorry,{name}..😓😓😓😓"
        game_result=decide_winner(player,computer)
        print(game_result)
        nonlocal game_count
        game_count += 1
        print(f"\n Game count:  {str(game_count)}")
        print(f"\n {name}'s wins:  {str(player_wins)}")
        print(f"\n python wins:  {str(python_wins)}")
        print(f"\nPlay again.{name}?")
        while True: 
            playagain=input("\nY for yes or\nQ to quit\n")
            if playagain.lower() not in ["y","q"]:
              continue
            else:
                break
        if playagain.lower() == "y":
            return play_rpsg()
        else:
            print("\n🎉🎉🎉🎉🎉")
            print("Thank you for playing !\n")
            if __name__ == "__main__":
                 sys.exit(f"Bye {name}!👋👋👋👋👋 ")
            else:
                 return
    return play_rpsg

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
    play_rpsg = rpsg(args.name)
    play_rpsg()