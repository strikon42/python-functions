#!/usr/bin/env python
# coding: utf-8

# In[2]:


from IPython.display import clear_output
def display_board(board):
    clear_output()

    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
   
    print('-----------')
  
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])

    print('-----------')

    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])


# In[3]:


test_board= ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)
display_board(test_board)
display_board(test_board)


# In[4]:


def player_input():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


# In[5]:


player1_marker ,player2_marker = player_input() 


# In[6]:


player1_marker


# In[7]:


def place_marker(board,marker,position):
    board[position] = marker


# In[8]:


test_board


# In[9]:


place_marker(test_board,'$',9 )
display_board(test_board)


# In[10]:



def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal


# In[11]:


win_check(test_board, 'X')


# In[12]:


import random

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


# In[13]:


def space_check(board, position):
    return board[position] == ''


# In[14]:


def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True


# In[15]:


def player_choice(board):
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Choose a position: (1-9)'))
    return position


# In[16]:



def replay():
    
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


# In[ ]:


print('wecome to Tic Tac Toe')

while True:
    
    the_board = ['']*10
    player1_marker,playe2_marker= player_input()
    
    turn = choose_first()
    print(turn + 'will go first')
    
    play_game = input ('Ready to play? y or n?')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
    
    while game_on:
        if turn == 'Player 1':
            
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board,player1_marker,position)
            
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('Player 1 has WON!!')
                game_on = False
            else: 
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie Game!!')
                    game_on = False
                else:
                    turn = 'Player 2'
        else: 
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board,player2_marker,position)
            
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('Player 2 has WON!!')
                game_on = False
            else: 
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie Game!!')
                    game_on = False
                else:
                    turn = 'Player 1'
    if not replay():
        break
         


# ###### 

# In[ ]:




