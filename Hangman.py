'''
GIVEN THAT PREVIOUSLY I HAVE NOT HAD AN EXPIRIENCE IN PROGRAMMING, THAT IS WHY I HAVE PERFORMED A GAME - HANGMAN.
IN PROCESS OF CREATING THIS GAME I HAVE USED ANOTHER TAMPLATE OF THE GAME WHICH I HAVE MODIFIED BY USING THOSE SKILLS THAT I RECEIVED DURING THIS COURSE.
CODE THAT WAS TAKEN FROM INTERNET IS SEPERATELY MARKED IN MY PROGRAMM. ANOTHER CODE IS CREATED BY MYSELF. 
IN THIS GAME THERE IS AN OPPORTUNITY TO PLAY WITH HUMAN AND WITH COMPUTER.
'''
import requests
import random
import sys
import getpass # So that second player can not see the word that typed in 1 player
 

# THE FUNCTION BELOW IS A MAIN FUNCTION THAT GIVES US AN OPPORTUNITY TO PLAY WITH HUMAN OR COMPUTER 

def choise():
    marker = ''
    marker = input('Play with COMPUTER press C \nPlay with HUMAN press H ')
    if marker == 'c':
        return main_list_internet()
    elif marker == 'h':
        return main_human()
    else:
        return choise()

# THIS FUNCTION (BELOW) TAKES THE LIST OF WORDS FROM THE INTERNET
    
def list_from_internet():
    word_github = requests.get("https://gist.githubusercontent.com/deekayen/4148741/raw/98d35708fa344717d8eee15d11987de6c8e26d7d/1-1000.txt").text.split('\n')
    word_list = list(word_github) # HERE WE ADD WORDS FROM INTERNET TO THE LIST IN OUR PROGRAMM
    wordlist_good = []
    for i in word_list:
        if len(i)>3:
            wordlist_good.append(i) # IF THE WORD FROM INTERNET IS LONGER THAN 3 LETTERS WE ADD IT TO PROGRAMM LIST
    word_random = random.choice(wordlist_good) # THE COMPUTER RANDOMLY CHOOSE THE WORD FOR THE GAME
    return word_random.upper()

# THE GAME WITH THE SECOND PLAYER - HUMAN

def get_word():
    word = getpass.getpass("Enter the word: ") # HUMAN INPUT THE WORD (ALREADY HIDDEN BY "GETPASS") MANUALLY
    return word.upper()

# Game function

def play(word):
    word_completion = "_" * len(word) # REEPLACE THE LETTERS FOR THE SYMBOL " _ "
    guessed = False
    guessed_letters = []
    guessed_word = []
    tries = len(word) # NUMBER OF TRIES DEPENDS ON THE LENGTH OF WORD
    print("Let`s play Hangman") 
    print(word_completion)
    
    while not guessed and tries > 0: # COUNTER
        print("Number of tries is: ",tries)
        guess = input("Please guess the letter: ").upper()
        
        if guess.isalpha(): # THE INPUT SYMBOLS CAN BE ONLY LETTERS NOT NUMBERS
            
            if guess in guessed_letters:
                print("You have already guessed this letter", guess)
                print("Guessed letters: ",guessed_letters)
            
            elif guess not in word:
                print(guess, "Letter is not in the word")
                print("Guessed letters: ",guessed_letters)
                tries -= 1 # COUNTER - 1
                guessed_letters.append(guess)
            
            else:
                print("Good Job! ", guess, "is in the word")
                guessed_letters.append(guess)
                
                # THE PART OF THIS "ELSE" (LINES 76-82) BLOCK BELOW HAS BEEN TAKEN FROM THE INTERNET
                
                word_as_list = list(word_completion)        
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
                
                # THE CODE BELOW IS SELF MADE CODE AGAIN =)))
        
        
        elif len(guess) == len(word): 
            guessed = True
            word_completion = word
           
        
        else:
            print("Incorrect")
        print(word_completion)
        print("\n")
    
    if guessed:
        print("Congrats, you won!")
    else:
        print("Game over! The word was: ", word)
    
# THE GAME FUNCTION AGAINST THE HUMAN

def main_human():
    word = get_word()
    play(word)
    repeat()

# THE GAME FUNCTION AGAINST THE HUMAN
            
def main_list_internet():
    word1 = list_from_internet()
    play(word1)
    repeat()
                
# FUNCTION WHICH ALLOWS US TO PLAY AGAIN OR TO EXIT THE PROGRAMM
        
def repeat():
    while True:
        if input("Play Again? (Y/N) ").upper() == "Y":
            return choise()
        else:
            print("GOOD BUY")
            sys.exit() # EXIT THE PROGRAMM

# THE PROGRAMM CODE

while True:
    choise()
    break
