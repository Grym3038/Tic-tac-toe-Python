class Minimax:
    def __init__(self):
        self.board = [["" for _ in range(9)]]
        
    def fillPos(self, TakenPos, turn):
            match TakenPos:
                case "b1":
                    self.board[0] = turn
                case "b2":
                    self.board[1] = turn
                case "b3":
                    self.board[2]= turn
                case "b4":
                    self.board[3] = turn
                case "b5":
                    self.board[4] = turn
                case "b6":
                    self.board[5] = turn
                case "b7":
                    self.board[6] = turn
                case "b8":
                    self.board[7] = turn
                case "b9":
                    self.board[8] = turn





    def getAvailPos(self):
        for i in range(9):
                if self.board[i] == "":
                    return self.board[i]

    def evaluate(self):
        # Check rows
        for row in range(3):
            if self.board[3*row] == self.board[3*row+1] == self.board[3*row+2] != "":
                return 10 if self.board[3*row] == "X" else -10
        # Check columns
        for col in range(3):
            if self.board[col] == self.board[col+3] == self.board[col+6] != "":
                return 10 if self.board[col] == "X" else -10
        # Check diagonals
        if self.board[0] == self.board[4] == self.board[8] != "":
            return 10 if self.board[0] == "X" else -10
        if self.board[2] == self.board[4] == self.board[6] != "":
            return 10 if self.board[2] == "X" else -10
        return 0

    def is_moves_left(self):
        return "" in self.board

        
    


    def minimax(self, depth, is_maximizing):
        score = self.evaluate()
        if score == 10 or score == -10:
            return score
        if not self.is_moves_left():
            return 0  # draw

        if is_maximizing:
            best = -1000
            for i in range(9):
                if self.board[i] == "":
                    self.board[i] = "X"
                    best = max(best, self.minimax(depth+1, False))
                    self.board[i] = ""
            return best
        else:
            best = 1000
            for i in range(9):
                if self.board[i] == "":
                    self.board[i] = "O"
                    best = min(best, self.minimax(depth+1, True))
                    self.board[i] = ""
            return best


    def find_best_move(self):
        best_val = -1000
        best_move = -1
        for i in range(9):
            if self.board[i] == "":
                self.board[i] = "X"
                move_val = self.minimax(0, False)
                self.board[i] = ""
                if move_val > best_val:
                    best_val = move_val
                    best_move = i
        return best_move
