import sys
from rpsg import rpsg
from guess_number import guess_number
def play_game(name='PlayerOne'):
    welcome_back='False'
    while True:
        if welcome_back ==True:
            print(f"\n{name},Welcome back to the arcade menu.")
            playerchoice=input(
                "\nPlease choose a game:\n1=Rock Papper Scissors Gum\n2=Guess My Number\n\n Or press\"x\"to exit Arcade\n\n"
            )             
            
                        
            if playerchoice not in ["1","2","x"]:
                print(f"\n{name},Please enter 1,2,or x.")
                return play_game(name)
            
            
            welcome_back=True
            
            if playerchoice=="1":
                rock_paper_scissors_gum=rpsg(name)
                rock_paper_scissors_gum()
                
            elif playerchoice=="2":
                guess_my_number=guess_number(name)
                guess_my_number()
            else:
                print("\n See you next time!\n")
                sys.exit(f"Bye{name}!👋👋👋👋")
                
                
                
if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(
    description="Provides a personalized game experience."
    )
    
    parser.add_argument(
        '-n', '--name', metavar="name",
        required=True, help='The name of the person playing the game.'
    )
    args=parser.parse_args()
    print(f"\n{args.name},Welcome to the arcade!🐻")
    play_game(args.name)
            
            
            
            
        


