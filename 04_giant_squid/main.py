

class Board:

    def __init__(self, matrix):
        self.positions = {}
        self.rows = {}
        self.cols = {}
        self.sum = 0

        for r, row in enumerate(matrix):
            for c, x in enumerate(row):
                self.sum += x
                if r not in self.rows:
                    self.rows[r] = set()
                self.rows[r].add(x)
                if c not in self.cols:
                    self.cols[c] = set()
                self.cols[c].add(x)
                self.positions[x] = (r, c)

    def is_winner(self, number):
        if number not in self.positions:
            return
        r, c = self.positions[number]
        self.rows[r].remove(number)
        self.cols[c].remove(number)
        self.sum -= number
        if len(self.rows[r]) == 0 or len(self.cols[c]) == 0:
            return number * self.sum


def main():
    boards = set()
    with open('input.txt') as f:
        numbers = next(f)
        numbers = [int(x) for x in numbers.strip().split(',')]
        next(f)
        matrix = []
        for line in f:
            line = line.strip()
            if len(line) == 0:
                boards.add(Board(matrix))
                matrix = []
            else:
                row = [int(x) for x in line.split()]
                matrix.append(row)
        if len(matrix) > 0:
            boards.add(Board(matrix))

    called = set()
    num_boards = len(boards)
    for n in numbers:
        if n in called:
            continue
        else:
            called.add(n)
        to_remove = []
        for board in boards:
            x = board.is_winner(n)
            if x:
                if len(boards) == num_boards:
                    print("First Winner", x)
                if len(boards) == 1:
                    print("Last Winner", x)
                to_remove.append(board)
        for b in to_remove:
            boards.remove(b)


if __name__ == "__main__":
    main()
