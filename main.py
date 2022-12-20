from tkinter import *

import random

def next_turn(row, column):
    global player                                   #adding global player to check whos turn it is

    if buttons[row][column]['text']  == "" and check_winner() is False:          #checking if pressed button is empty and start check winner

        if player == players[0]:                 #all for player x

            buttons[row][column]['text'] = player

            if check_winner() is False:                   #checking if after placing button if no winner then we swap players, and turns label of whos turn it is
                player = players[1]
                label.config(text = (players[1]+ ' turn'))

            elif check_winner() is True:
                label.config(text = (players[0]+ ' wins'))

            elif check_winner() == 'Tie':
                label.config(text = ('Tie!'))


        else:
            # same as above but for next player checks
            buttons[row][column]['text'] = player

            if check_winner() is False:  # checking if after placing button if no winner then we swap players, and turns label of whos turn it is
                player = players[0]
                label.config(text=(players[0] + ' turn'))

            elif check_winner() is True:
                label.config(text=(players[1] + ' wins'))

            elif check_winner() == 'Tie':
                label.config(text=('Tie!'))





def check_winner():
    for row in range(3):                   #checking if all buttons is the same and is not empty in each row
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] !="":
            buttons[row][0].config(bg = 'yellow', fg = 'red')
            buttons[row][1].config(bg='yellow', fg='red')         #high light the winning option
            buttons[row][2].config(bg='yellow', fg='red')
            return True

    for column in range(3):      #checking if all buttons is the same and is not empty in each column
        if buttons[0][column]['text'] ==  buttons[1][column]['text'] == buttons[2][column]['text'] !='':
            buttons[0][column].config(bg='yellow', fg='red')
            buttons[1][column].config(bg='yellow', fg='red')
            buttons[2][column].config(bg='yellow', fg='red')
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != '':     #checking 1st diagonal
        buttons[0][0].config(bg='yellow', fg='red')
        buttons[1][1].config(bg='yellow', fg='red')
        buttons[2][2].config(bg='yellow', fg='red')
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != '':     #checking symmetric diagonal
        buttons[0][2].config(bg='yellow', fg='red')
        buttons[1][1].config(bg='yellow', fg='red')
        buttons[2][0].config(bg='yellow', fg='red')
        return True

    elif empty_spaces() is False:    #checking if buttons is pressed and as above no winner then tie
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg = 'grey', fg = 'black')
        return 'Tie'

    else:
        return False     #if no winner and still free spaces then game on



def empty_spaces():

    spaces = 9

    for row in range(3):                 #counting how much spaces is free still if 0 and no winner then tie
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -=1

    if spaces == 0:
        return False

    else:
        return True


def new_game():
    global player

    player = random.choice(players)
    label.config( text = player + ' turn')
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text = '', bg = 'light blue', fg ='blue')


window = Tk()

window.title('Tic Tac Toe')

players = ['x','o']
player = random.choice(players)

buttons = [[0,0,0],                           #setting initial buttons
          [0,0,0],
          [0,0,0]]


label = Label(text = player + ' turn', font= ('Stolzl',40))                                                                 #adding a label to the game
label.pack(side = 'top')

reset_button = Button(text= 'Restart', font = ('Stolzl',20), command = new_game)                                            #button to start new game

reset_button.pack(side= 'top', pady =5)

frame = Frame(window)                                                                                                     #creating frame to add button at special grid
frame.pack()

for row in range(3):                                                                                                      #setting each button in out frame by 2 for loop for 2d
    for column in range(3):
        buttons[row][column] = Button(frame, text = '' ,font = ('Stolzl',45), width = 5, height = 2, bg = 'light blue', fg ='blue',
                                      command = lambda row = row, column = column : next_turn(row,column))              #adding command to each button, so each action start next turn
        buttons[row][column].grid(row = row, column = column)       #packing buttons



window.mainloop()