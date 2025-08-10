
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
    
    
    print("**Game Rules**")
    print("1. The user starts with 3 warnings and 6 guesses.")
    print("2. If the user inputs anything besides one letter, they get a warning.\
          If the user enters a letter that has already been guessed, they get a warning.\
          After 3 warnings, the user will begin losing turns for every wrong input.")
    print("3. If the user guesses a letter correctly, they do not lose a guess.")
    print("4. If the user guesses a consonant that is not in the word, they lose one guess.\
          If the user guesses a vowel that is not in the word, they lose two guesses.")
    print("If the user guesses the correct word, the score is totaled as the number of guesses left\
          times the number of unique letters in the word. ")
    print("Good luck!")
    print("")
    
    
    guesses = 6
    word_length = len(secret_word)
    
    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {word_length} letters long.")
    print("------------------------")
    print("Choose one letter at a time. If you enter a character that is not a letter or a letter that was already chosen, you will get a warning.")
    print("You get 3 warnings. After 3 warnings, you lose a guess.")
    print(f"You have {guesses} guesses left.")
    letters_guessed = []
    available_letters = get_available_letters(letters_guessed)
    print(f"Available letters: {available_letters}")
    
      
    """    
    Use calls to the input function to get the user’s guess.  
    a. Check that the user input is an alphabet
    b. If the user does not input an uppercase or lowercase alphabet letter,
    subtract one warning or one guess. 
    Hint #2:​ you may find the string functions str.isalpha(‘your string’) and
    str.lower(‘Your String’) h
    """
    vowels = ["a", "e", "i", "o", "u"]
    
    warnings = 3
    while guesses >= 1 and is_word_guessed(secret_word, letters_guessed) == False:
        guess = input("Please guess a letter: ")
        print("")
        if str.isalpha(guess):
            guess = guess.lower()
            
        if not str.isalpha(guess) or len(guess) !=1:
            if warnings >= 1:
                warnings -= 1
                print(f"Oops! That is not a letter. You now have {warnings} warning(s) left:", get_guessed_word(secret_word, letters_guessed))  
            else:
                guesses -=1
                print("Oops! That is not a letter. You are out of warnings. You lost a guess", get_guessed_word(secret_word, letters_guessed))  
        
            
        elif guess in secret_word and guess in letters_guessed:
            
            if warnings >= 1:
                warnings -= 1
                print(f"Oops! You've already guessed that letter. You now have {warnings} warning(s) left:", get_guessed_word(secret_word, letters_guessed))
            else:
                guesses -=1
                print("Oops! You've already guessed that letter. You lost a guess.", get_guessed_word(secret_word, letters_guessed))
        
        
        
        elif guess not in secret_word and guess not in letters_guessed:
            #puts guess in list of letters guessed:
            letters_guessed.append(guess)
            print("Oops! That is not a valid letter.", get_guessed_word(secret_word, letters_guessed))
            if guess in vowels:
                guesses = guesses - 2
            else:
                guesses -= 1
        
        
        
        elif guess in secret_word:
            #puts guess in list of letters guessed:
            letters_guessed.append(guess)
            print("Good guess: ", get_guessed_word(secret_word, letters_guessed))
            
            
        available_letters = get_available_letters(letters_guessed)            
        print("-------------------------------------------------\n")
        print(f"You have {guesses} guesses and {warnings} warning(s) left.")
        print(f"Available letters: {available_letters}")
        
        
        
        
        
    #The total score is the number of guesses_remaining once the user has guessed the secret_word times the number of unique letters in secret_word.     
    secret_word_list = []
    for char in secret_word:
        if char not in secret_word_list:
            secret_word_list.append(char)
    letter_score = len(secret_word_list) #Determine the number of unique letters
    
    total_score = letter_score * guesses
    
    
    if is_word_guessed (secret_word, letters_guessed) == False:
        print(f"Sorry. You lost the game. The word I was thinking of is {secret_word}.")
    else: 
        print("Congratulations, you won!")
        print(f"Your total score for this game is {total_score}.")
hangman("apple")
