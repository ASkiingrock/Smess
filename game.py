import fen_setup
import board
import ai

# Start setup is 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'

exports = fen_setup.setup_fen('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')
chessBoard = exports[0]
whosMove = exports[1]
# castling = exports[2]
EnPassant = exports[3]
stop = False
move = False

while not stop:
    print(board.print_board(chessBoard))
    legalMoves = board.find_moves(chessBoard,whosMove,EnPassant)
    # Computer plays black
    if whosMove == "b":
        move = ai.ai(legalMoves,chessBoard)
    else:
        while move == False:
            move = board.convert_user_coords(input('>> '),chessBoard,whosMove,EnPassant)
            if move not in legalMoves:
                move = False
            if move == False:
                print("That's an illegal move. Try again.")
    for moves in move:
        chessBoard, EnPassant = board.make_move(chessBoard[moves[0][0]][moves[0][1]],moves[1],chessBoard)
    move = False
    # if castling != '':
    #     castling = board.castling_rights(chessBoard,whosMove,castling)
    whosMove = "w" if whosMove == "b" else "b" # Swap
    if board.checkmate(chessBoard,whosMove) != False:
        print(board.print_board(chessBoard))
        winner = 'White' if board.checkmate(chessBoard,whosMove) == "w" else 'Black'
        print(f'{winner} has won the game!')
        stop = True