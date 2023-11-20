import os 

os.system('cls')

def tictactoe():
    print('''Welcome to my Tic Tac Toe game!!!

              1            2          3
       XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
       XXX         XXX         XXX         XXX  
     A XXX   ''',dict['A1'],'''   XXX   ''',dict['A2'],'''   XXX   ''',dict['A3'],'''   XXX
       XXX         XXX         XXX         XXX
       XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
       XXX         XXX         XXX         XXX  
     B XXX   ''',dict['B1'],'''   XXX   ''',dict['B2'],'''   XXX   ''',dict['B3'],'''   XXX
       XXX         XXX         XXX         XXX
       XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
       XXX         XXX         XXX         XXX  
     C XXX   ''',dict['C1'],'''   XXX   ''',dict['C2'],'''   XXX   ''',dict['C3'],'''   XXX
       XXX         XXX         XXX         XXX
       XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX''')

dict = {'A1':' ','A2':' ','A3':' ','B1':' ','B2':' ','B3':' ','C1':' ','C2':' ','C3':' '}
tictactoe()

count = 0
while not ((dict['A1'] == 'X' and dict['A2'] == 'X'and dict['A3'] == 'X') or 
          (dict['B1'] == 'X' and dict['B2'] == 'X'and dict['B3'] == 'X') or
          (dict['C1'] == 'X' and dict['C2'] == 'X'and dict['C3'] == 'X') or
          (dict['A1'] == 'X' and dict['B1'] == 'X'and dict['C1'] == 'X') or 
          (dict['A2'] == 'X' and dict['B2'] == 'X'and dict['C2'] == 'X') or
          (dict['A3'] == 'X' and dict['B3'] == 'X'and dict['C3'] == 'X') or
          (dict['A1'] == 'X' and dict['B2'] == 'X'and dict['C3'] == 'X') or
          (dict['C1'] == 'X' and dict['B2'] == 'X'and dict['A3'] == 'X') or
          (dict['A1'] == 'O' and dict['A2'] == 'O'and dict['A3'] == 'O') or
          (dict['B1'] == 'O' and dict['B2'] == 'O'and dict['B3'] == 'O') or
          (dict['C1'] == 'O' and dict['C2'] == 'O'and dict['C3'] == 'O') or
          (dict['A1'] == 'O' and dict['B1'] == 'O'and dict['C1'] == 'O') or
          (dict['A2'] == 'O' and dict['B2'] == 'O'and dict['C2'] == 'O') or
          (dict['A3'] == 'O' and dict['B3'] == 'O'and dict['C3'] == 'O') or
          (dict['A1'] == 'O' and dict['B2'] == 'O'and dict['C3'] == 'O') or
          (dict['C1'] == 'O' and dict['B2'] == 'O'and dict['A3'] == 'O') or
          count == 9):
    print("")
    if count % 2 == 0:
        choice = input("Player X, please choose your location:")
        choice = choice.upper()
        try:
            if dict[choice] == " ":
                dict[choice] = 'X'
                count += 1
                winner = 'X'
                os.system('cls')
                tictactoe()
            else:
                print("Not a valid choice or space taken!  Try Again!")
        except:
            if choice == 'quit':
                quit()
            print("Not a valid choice or space taken!  Try Again!")
    else:
        choice = input("Player O, please choose your location:")
        choice = choice.upper()
        try:
            if dict[choice] == " ":
                dict[choice] = 'O'
                count += 1
                winner = 'O'
                os.system('cls')
                tictactoe()
            else:
                print("Not a valid choice or space taken!  Try Again!")
        except:
            if choice == 'quit':
                quit()
            print("Not a valid choice or space taken!  Try Again!")
if count == 9:
    winner = 'the cat'
print("")
print('GAME OVER - The winner is',winner,'!!!!!')
print("")