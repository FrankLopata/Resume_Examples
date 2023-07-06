import gamefunc as gf
import Network
import connectfour as game

if __name__ == '__main__':
    print("Please input an amount of columns")
    columns = input()
    print("Please input an amount of rows")
    rows = input()
    Network.begin_the_game(columns,rows)
    Gamestate = gf.game_setup(rows,columns)
    gf.print_board(Gamestate)
    while(game.winner(Gamestate) == game.EMPTY):    
        try:
            print("please enter drop/pop and your column number")
            inpt = input()
            move = inpt.split(" ")
            Gamestate = gf.new_turn(Gamestate,move[0],move[1])
            gf.print_board(Gamestate)
            Network.make_move(inpt.upper())
            Gamestate = Network.retrieve_move(Gamestate)
            gf.print_board(Gamestate)
        except Exception as e:
            print(e)
            print("Invalid Input")
        

    if(game.winner(Gamestate) == game.YELLOW):
        print("The winner is Yellow")
    if(game.winner(Gamestate) == game.RED):
        print("The winner is Red")