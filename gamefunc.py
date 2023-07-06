#Patrick M Lopata
#31036957
import connectfour as game
import os
import sys
def print_board(state : game.GameState):
    try:
        indx = 0
        while indx < game.columns(state):
            print(str(indx +1),end="  ")
            indx += 1
        print("")

        for i in range(game.rows(state)):
            for x in range(game.columns(state)):
                assert state.board[x][i] == 0  or state.board[x][i] ==1 or state.board[x][i]==2
                if(state.board[x][i]==0):
                    print( ".", end = "  ")
                if(state.board[x][i]==1):
                    print( "R", end = "  ")
                if(state.board[x][i]==2):
                    print( "Y", end = "  ")
            print('\n')
        
    except Exception as e:
        print(e) 

def new_turn(state : game.GameState, want : str, column : str):
    while want.lower() != "drop" and want.lower() != "pop":
        print("Invalid input")
        want = input()
    while(want.lower() == "pop"):
        ace = 0
        for i in range(game.rows(state)):
            if( state.board[i][game.rows(state) - 1] != 0 ):
                ace = 1
                break
        if(ace == 1):
            break
        print("You cannot pop this turn")
        want = input()
    if(want.lower() == "drop"): 
            column = int(column)
            return game.drop(state, column-1)

    if(want.lower() == "pop"):
            column = int(column)
            return game.pop(state, column-1)
        

def game_setup(row: str, column: str):
    if(row.isdigit()):
        row = int(row)
        if(row>20 or row<4):
            print("Invalid input")
            os.execl(sys.executable, sys.executable, *sys.argv)
    else:
        print("Invalid input")
        os.execl(sys.executable, sys.executable, *sys.argv)
    assert type(row) == int and row < 21 and row > 3
    if(column.isdigit()):
        column = int(column)
        if(column>20 or column<4):
            print("Invalid input")
            os.execl(sys.executable, sys.executable, *sys.argv)
    else:
        print("Invalid input")
        os.execl(sys.executable, sys.executable, *sys.argv)
    assert type(column) == int and column < 21 and column > 3

    return game.new_game(column,row)

def turn_display(state : game.GameState):
        if(state.turn == game.YELLOW):
            turn = "Yellow"
        else:
            turn = "Red"

        print("Your turn " + turn, end = '\n' )

    


