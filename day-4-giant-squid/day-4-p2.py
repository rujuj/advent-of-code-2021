def boardWinner (board):
    columns = [0] * (len(board[0]))
    for row in board:
        if all (x == 'x' for x in row):
            return True
        for i, num in enumerate(row):
            if num == 'x':
                columns[i] += 1
    for column in columns:
        if column == 5:
            return True
    return False

# takes board (5x5 list of strings) and justcalled (the number that was just called, in the form of a string)
def findFinalScore (board, justcalled):
    score = 0
    for row in board:
        for num in row:
            if num != 'x':
                score += int(num)
    return score * int(justcalled)

# open file 
input = open("input.txt")
lines = input.read()

# parse input 
inputboards = lines.split("\n\n")
bingonumbers = inputboards[0].split(",")
inputboards = inputboards[1:]
boards = []

# parse the input, store the numbers appropriately, strip spaces
for board in inputboards:
    rows = board.split("\n")
    addBoard = []
    for row in rows:
        numbers = row.split(" ")
        addRow = []
        for num in numbers:
            if num != '':
                num = num.strip(" ")
                addRow.append(num)
        addBoard.append(addRow)
    boards.append(addBoard)

winningBoards = []
     
# go through each drawn number 1 by 1 (first 5 can be done together though)
for num in bingonumbers:
    for i, board in enumerate(boards):
        # don't bother looking at the boards who won already 
        if board not in winningBoards:
            for j, row in enumerate(board):
                for k, entry in enumerate(row):
                    if entry == num:

                        # replace numbers with 'x' marking that spot 
                        boards[i][j][k] = 'x'

                        # calculate for all rows and columns if there is a bingo 
                        if boardWinner(board):
                            # track which boards win
                            winningBoards.append(board)
                            if len(winningBoards) == len(boards):
                                print("last to win!")
                                print(board)
                                print("final score: ", findFinalScore(board, num))
                                exit()

# first attempt: 2634 - correct
# i was getting this weird empty board and realized upon looking at my input file that i just needed to delete 
    # the last 2 empty lines and that fixed my issue 