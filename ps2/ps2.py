# -*- coding: utf-8 -*-
"""
Created on Sat Aug  9 13:21:38 2025

@author: pam
"""
import string

#Determine whether the word has been guessed - Part 1A
def is_word_guessed (secret_word, letters_guessed):
    """
    This function takes in two parameters: 
        secret_word - a string 
        list of letters - letters_guessed
    It returns a boolean. 
    If all the letters in the secret word are in letters guessed: True
    Otherwise: False
    
    Parameters
    ----------
    secret_word : STRING.
    letters_guessed : LIST.

    Returns
    -------
    returnstring : BOOLEAN.
    
    """
    for char in secret_word: #run through each letter in the secret word
        if (char in letters_guessed) == False:  
            return False    # if a letter hasn't been guessed, then the word hasn't been guessed
    return True             # if not letter pops up as false, all the letters have been guessed
        
    
#Getting the user's guess - Part 1B
def get_guessed_word(secret_word, letters_guessed):
    """
    This function takes in two parameters: 
        secret_word - a string 
        list of letters - letters_guessed
    It returns a string the is comprised of letters and underscores, 
    based on what letters in letters_guessed are in secret_word. 

    Parameters
    ----------
    secret_word : STRING.
    letters_guessed : LIST.

    Returns
    -------
    returnstring : STRING.

    """
    returnstring = ""  # Initializes the string
    for char in secret_word: #run through each letter in the secret word
        if char in letters_guessed:
            returnstring = returnstring + char #adds the letter to the string
        else:
            returnstring = returnstring + "_ "  #adds a space to the string
    return returnstring
        

 

#Getting all available letters - Part 1C
def get_available_letters(letters_guessed):
    """
    This function takes in one parameter - a list of letters, letters_guessed, 
    and returns a string that is comprised of lowercase English letters - 
    all lowercase letters that are not in .

    Parameters
    ----------
    letters_guessed : LIST.

    Returns
    -------
    letters_string : STRING.

    """
    
    letters_string = ""
    for letter in string.ascii_lowercase:  # For uppercase, use string.ascii_uppercase  # For uppercase, use 'A' and 'Z'
        if letter not in letters_guessed:
            letters_string += letter
    return letters_string
            


def hangman(secret_word):
    guesses = 6
    word_length = len(secret_word)
    
    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {word_length} letters long.")
    print("------------------------")
    print(f"You have {guesses} guesses left.")
    letters_guessed = []
    available_letters = get_available_letters(letters_guessed)
    print(f"Available letters: {available_letters}")
    guess = input("Please guess a letter: ")
    guesses -= 1
    #puts guess in list of letters guessed:
    letters_guessed.append(guess)
    if guess in secret_word:
        print("Good guess: ", get_guessed_word(secret_word, letters_guessed))
    elif:
        print("Oops! That is not a valid letter. ")
    
