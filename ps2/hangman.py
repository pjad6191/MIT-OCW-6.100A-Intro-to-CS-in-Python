# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for char in secret_word: #run through each letter in the secret word
        if (char in letters_guessed) == False:  
            return False    # if a letter hasn't been guessed, then the word hasn't been guessed
    return True             # if not letter pops up as false, all the letters have been guessed
        



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    returnstring = ""  # Initializes the string
    for char in secret_word: #run through each letter in the secret word
        if char in letters_guessed:
            returnstring = returnstring + char #adds the letter to the string
        else:
            returnstring = returnstring + "_ "  #adds a space to the string
    return returnstring
        



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    letters_string = ""
    for letter in string.ascii_lowercase:  # For uppercase, use string.ascii_uppercase  # For uppercase, use 'A' and 'Z'
        if letter not in letters_guessed:
            letters_string += letter
    return letters_string
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
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


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
