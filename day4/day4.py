with open("day4.txt") as f:
    content = f.read().split("\n\n")

get_first = True

draws = [int(i) for i in content[0].split(",")]
boards = [[[int(i) for i in line.split()] for line in board.split("\n")] for board in content[1:]]

def run_game(board, draw):
    return [["X" if i == draw else i for i in line] for line in board]

def won(board):
    return (any(all(i == "X" for i in line) for line in board) or
            any(all(line[id] == "X" for line in board) for id in range(len(board[0]))))

def score(board, draw):
    return sum(sum(i for i in line if i != "X") for line in board) * draw

for draw in draws:
    boards = [run_game(board, draw) for board in boards]

    for board in boards:

        if won(board) and get_first:
            print("Solution to Part 1:", score(board, draw))
            get_first = False
        elif len(boards) == 1:
            print("Solution to Part 2:", score(board, draw))

    boards = [board for board in boards if not won(board)]
