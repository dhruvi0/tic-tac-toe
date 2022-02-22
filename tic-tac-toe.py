import numpy as np

board = np.full((3,3), " ")

board_dict = {"one": (0, 0), "two": (0, 1), "three": (0, 2), "four": (1, 0), 
              "five": (1,1), "six": (1,2), "seven": (2,0), "eight": (2,1),
              "nine": (2,2)}

def update_board(move):
     
    board_place = board_dict.get(move)
       
    if tracker % 2 != 0:
        board[board_place] = "X"
        
    elif tracker % 2 == 0:
        board[board_place] = "O"
              
    return board
    
def check_win(board):
        
    if board[board_dict.get("one")] == board[board_dict.get("two")] and board[board_dict.get("two")] == board[board_dict.get("three")]:
        outcome = board[board_dict.get("one")]        
    elif board[board_dict.get("four")] == board[board_dict.get("five")] and board[board_dict.get("five")] == board[board_dict.get("six")]:
        outcome = board[board_dict.get("four")]       
    elif board[board_dict.get("seven")] == board[board_dict.get("eight")] and board[board_dict.get("nine")] == board[board_dict.get("six")]:
        outcome = board[board_dict.get("seven")]  
    elif board[board_dict.get("one")] == board[board_dict.get("five")] and board[board_dict.get("five")] == board[board_dict.get("nine")]:
        outcome = board[board_dict.get("one")] 
    elif board[board_dict.get("three")] == board[board_dict.get("five")] and board[board_dict.get("five")] == board[board_dict.get("seven")]:
        outcome = board[board_dict.get("three")]
    elif board[board_dict.get("one")] == board[board_dict.get("four")] and board[board_dict.get("four")] == board[board_dict.get("seven")]:
        outcome = board[board_dict.get("one")]  
    elif board[board_dict.get("one")] == board[board_dict.get("four")] and board[board_dict.get("four")] == board[board_dict.get("seven")]:
        outcome = board[board_dict.get("one")] 
    elif board[board_dict.get("three")] == board[board_dict.get("six")] and board[board_dict.get("six")] == board[board_dict.get("nine")]:
        outcome = board[board_dict.get("three")]          
    else:
        outcome = "None"
    
    if "O" in outcome:
        winner = "Player 2"
        print("Player 2 wins")
        
    elif "X" in outcome:
        winner = "Player 1"
        print("Player 1 wins")        
        
    else:
        winner = "None"
    
    return winner
 
    
tracker = 1

while check_win(board) == "None":

    if tracker % 2 != 0:
        move = input("Player 1 enter space (one - nine): ")
        
    elif tracker % 2 == 0:
        move = input("Player 2 enter space (one - nine): ")
    
    while move not in board_dict.keys():    
        move = input("Pick a letter representation of one - nine: ")
        
    board_place = board[board_dict.get(move)]
    
    while board_place != ' ':
        move = input("Pick an unmarked spot: ")
        board_place = board[board_dict.get(move)]
        
    update_board(move)
    
    print(board)
    
    tracker += 1
    
