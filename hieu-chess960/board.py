class Board:
    # called when you call `b = Board()`
    def __init__(self):
        # self.board = [[''] * 8] * 8
        # TODO fill in pieces
        self.board = [
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
            ['p'] * 8,
            [' '] * 8,
            [' '] * 8,
            [' '] * 8,
            [' '] * 8,
            ['P'] * 8,
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
        ]
        # self.board[0][0] means A8

    def print(self):
        # print representation of the 8x8 board.
        # Questions: what does self.board[0][0] represent?
        for rank in self.board:
            print(rank)

    def get_moving_piece(self, move_notation):
        # e4
        # Bb5
        # Nf6
        # Kh7
        # gxh7
        # Qg2
        # a8 = Q
        # O-O
        # O-O-O
        '''
        If first letter is lowercase, it's a pawn move
        Else, first letter represents moving piece
        Unless it's O-O or O-O-O
        '''
        if move_notation == 'O-O' or move_notation == 'O-O-O':
            return 'king'
        if move_notation[0].islower():
            return 'pawn'
        else:
            name_conversion = {
                'B': 'bishop',
                'N': 'knight',
                'Q': 'queen',
                'K': 'king',
                'R': 'rook',
            }
            # TODO is the letter even in name_conversion?
            return name_conversion[move_notation[0]]

    def execute_move(self, move_notation):
        print('executing_move with', move_notation)
        piece = self.get_moving_piece(move_notation)
        '''
        TODOS
        - What the piece is
        - Is the move valid:
            - Is that a square the piece can move to?
            - Is destination square occupied?
            - Am I in check?
                - Am I taking the piece giving check? Then it's valid.
                - Blocking check = valid
            - Is the piece pinned to the king?
            - Is it that color's turn?
            - If castling:
                - Has the king or rook moved? Moved EVER, cos they could be on valid squares.
                - Is another piece in the way?
            - If moving king:
                - Am I going into, out of, or through check?
        - Am I taking a piece?
        '''
        pass

b = Board() # calls __init__
# b is an instance
# Move validity
# b.execute_move('Ke7')
p = b.get_moving_piece('Ke2')
# we call the function of the instance and assign it to p
print(p)