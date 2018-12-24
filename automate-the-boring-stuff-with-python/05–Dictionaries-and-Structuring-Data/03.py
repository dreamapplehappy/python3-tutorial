def tictactoe():
    board = {}
    playero = 'O'
    playerx = 'X'
    for i in ['a', 'b', 'c']:
        for j in ['1', '2', '3']:
            board.setdefault(i + j, ' ')

    def printboard():
        for i in ['a', 'b', 'c']:
            if i != 'a':
                print('-+-+-')
            row = []
            for j in ['1', '2', '3']:
                row.append(board[i + j])
            print('|'.join(row))

    def checkwinner():
        win = [['a1', 'a2', 'a3'],
               ['b1', 'b2', 'b3'],
               ['c1', 'c2', 'c3'],
               ['a1', 'b1', 'c1'],
               ['a2', 'b2', 'c2'],
               ['a3', 'b3', 'c3'],
               ['a1', 'b2', 'c3'],
               ['a3', 'b2', 'c1']]
        for first, second, third in win:
            # print(first, second, third)
            if board[first] != ' ' and board[first] == board[second] and board[first] == board[third]:
                print(board[first], 'is winner')
                return board[first]

    current = playero
    for i in range(9):
        if current == playerx:
            current = playero
        else:
            current = playerx
        location = input('current player is ' + current + ' please input location:\n')
        board[location] = current
        if checkwinner():
            break
        printboard()


tictactoe()
