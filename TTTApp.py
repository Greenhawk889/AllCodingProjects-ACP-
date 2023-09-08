
# Tonight, I'm going to be making a very boring but easy to make tic-tac-toe game

#use it however you like


def bboard(board): #I called it bboard because for some dumb reason, Python wants to give me an error for calling it board because it gets confused betweent the defintion board and the variable board, ugh.
    for rows in board:
        
        print(" | ".join(rows))
        
        print("-" * 9)

def win(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False #If none of these were to be true 

def full(board):
    return all(item != " " for row in board for item in row)

def ttt():
    board = [[" " for _ in range(3)] for _ in range(3)]
    
    player = "X"
    turns = 0

    while True:
        bboard(board)
        
        print(f"Player {player}'s turn.")
        
        rows = int(input("Enter row (0, 1, 2): "))
       
        cols = int(input("Enter column (0, 1, 2): "))

        if board[rows][cols] == " ":
            board[rows][cols] = player
            turns += 1

            if win(board, player):
                bboard(board)
                print(f"Player {player} wins!")
                break

            elif turns == 9:
                bboard(board)
                print("Tie.")
                
                break
            
            player = "O" if player == "X" else "X"
        else:
            print("Postion already taken.")

if __name__ == "__main__":
    ttt()
