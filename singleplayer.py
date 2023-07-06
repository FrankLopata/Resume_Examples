import connectfour as game
import gamefunc as gf

if __name__ == '__main__': 
    print("Welcome to Connect 4, The red player will move first")
    print("Please enter your row length:")
    row = input()
    print("please enter Column length:")
    column = input()
    Gamestate = gf.game_setup(row,column)
    gf.print_board(Gamestate)
    while(game.winner(Gamestate) == game.EMPTY): 
        gf.turn_display(Gamestate)        
        try:
            print("please enter drop/pop and your column number")
            inpt = input()
            move = inpt.split(" ")
            Gamestate = gf.new_turn(Gamestate,move[0],move[1])
            gf.print_board(Gamestate)
        except Exception as e:
            print(e)
            print("Invalid Input")

    if(game.winner(Gamestate) == game.YELLOW):
        print("The winner is Yellow")
    if(game.winner(Gamestate) == game.RED):
        print("The winner is Red")