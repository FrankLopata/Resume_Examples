import socket
import gamefunc as gf
import connectfour as game

sock = socket.socket()
connect_adress = ('circinus-32.ics.uci.edu', 4444)
sock.connect(connect_adress)
input_stream = sock.makefile('r')
output_stream = sock.makefile('w')
def begin_the_game(columns: str, rows: str):
    print("please input username")
    username = input()
    output_stream.write("I32CFSP_HELLO " + username + "\r\n")
    output_stream.flush()
    print(input_stream.readline())
    output_stream.write("AI_GAME " + columns+ " " + rows+ "\r\n")
    output_stream.flush()
    print(input_stream.readline())

def make_move(input: str):
    print("SEND: " + input)
    output_stream.write(input.strip() + "\r\n")
    output_stream.flush()

def retrieve_move(state: game.GameState):
    print(input_stream.readline())
    move = input_stream.readline()
    print(move)
    move = move.split()
    state = gf.new_turn(state,move[0],move[1])
    print(input_stream.readline())
    return state
    





