inp = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
turns = 1
total = []
dic = {'13': 0, '23': 1, '33': 2, '12': 3, '22': 4, '32': 5, '11': 6, '21': 7, '31': 8}


def printing():
    print("---------")
    for i in range(0, 9, 3):
        print(f'| {inp[i]} {inp[i+1]} {inp[i+2]} |')
    print("---------")


def check_status():
    global total
    first = [inp[0] + inp[1] + inp[2], inp[3] + inp[4] + inp[5], inp[6] + inp[7] + inp[8]]
    second = [inp[0] + inp[3] + inp[6], inp[1] + inp[4] + inp[7], inp[2] + inp[5] + inp[8]]
    third = [inp[2] + inp[4] + inp[6]]
    fourth = [inp[0] + inp[4] + inp[8]]
    total = first + second + third + fourth
    if 'OOO' in total:
        print('O wins')
        exit()
    elif 'XXX' in total:
        print('X wins')
        exit()
    elif ' ' not in inp:
        print('Draw')
        exit()


def user_input():
    try:
        input2 = [int(i) for i in input('Enter the coordinates: > ').split()]
        coord = ''.join([str(i) for i in input2])
        try:
            if inp[dic[coord]] != ' ':
                print('This cell is occupied! Choose another one!')
                return user_input()
            else:
                return game(coord)
        except KeyError:
            print('Coordinates should be from 1 to 3!')
            return user_input()
    except ValueError:
        print('You should enter numbers!')
        return user_input()


def game(coord):
    global turns
    if turns % 2:
        inp[dic[coord]] = 'X'
    else:
        inp[dic[coord]] = 'O'
    turns += 1
    printing()
    check_status()
    user_input()


printing()
user_input()
