#Name: Nhat Tran, Alice Quaye, Andrea Bernal
#Date: 11/15/2024
#Project Name: Hangman Game


import random;

LIST_WORDS = ['Elephant', 'Python', 'Anaconda', 'Jazz', 'Keyboard', 'Dictionary', 'Length', 'Pixel', 'Quiz', 'Quest'];      #Constant list of words

STAGES = [          #Constant list of stages using triple quotation
        """
           ------
           |    |
           |    
           |   
           |   
           |   
        --------
        """,  #stage 0
        """
           ------
           |    |
           |    O
           |   
           |   
           |   
        --------
        """,  #stage 1
        """
           ------
           |    |
           |    O
           |    |
           |   
           |   
        --------
        """,  #stage 2
        """
           ------
           |    |
           |    O
           |   /|
           |   
           |   
        --------
        """,  #stage 3
        """
           ------
           |    |
           |    O
           |   /|\\
           |   
           |   
        --------
        """,  #stage 4
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / 
           |   
        --------
        """,  #stage 5
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |   
        --------
        """   #stage 6 
    ]

def chooseWords():
    return random.choice(LIST_WORDS);


def drawHangman(lives):     # draw hangman using with lives argument to determine which stage to show
    print(STAGES[-(lives)-1]);


def guessWord(let, word, blank):   #fill the blank with the guess word
    
    for index in range(len(blank)):
        if word[index].lower() == let:
            blank[index] = let;
    
    return blank; #return blanks with new letters


def rightLetter(let, word, blank):   #execute if the player guess the correct letter
    count = word.lower().count(let.lower());
    print(f'There are {count} letters in the word.');
    guessWord(let, word, blank);
    
    return guessWord(let, word, blank); #return blanks with new letters


def wrongLetter(let):       #execute if the player guess the wrong letter
    print(f'There is no \'{let}\' in the word.'); 


def gamestart():
    lives = 6;       #lives
    word = chooseWords();  #choose word from guesslist
    isBlank = True;         #if there is any blank of the guess string

    blank_string_list = ['_'] * len(word);           #initialize blank string for player to guess
    
    drawHangman(lives);
    print(f'{blank_string_list}\n');
    

    while lives != 0 and isBlank:            #loop until no lives left or the word has been guessed
        guessLetter = input('Please enter the guess letter: ');
 #       if guessLetter == 'exit':   #test for exit the program
 #           exit();
 #       if guessLetter == 'guess word':
 #           print('The guess word is',word);
 #           continue;

        if (guessLetter.lower() not in blank_string_list) and (guessLetter.lower() in word.lower()): #check if the guess letter is in the word in any form
            blank_string_list = rightLetter(guessLetter, word, blank_string_list);
            drawHangman(lives);
            print(f'Lives: {lives}');
            print(f'{blank_string_list}\n');
        
        elif guessLetter.lower() in blank_string_list:       #check if the letter has already been guessed
            drawHangman(lives);
            print(f"You already guessed the letter \'{guessLetter}\'");
            print(f'Lives: {lives}');
            print(f'{blank_string_list}\n');
        
        else:                           #execute if the player guesses the wrong letter
            lives -= 1;
            drawHangman(lives);
            wrongLetter(guessLetter);
            print(f'Lives: {lives}')
            print(f'{blank_string_list}\n');

        if '_' not in blank_string_list:     #check if there is no blank in the blank_list
            isBlank = False;
        

    if isBlank and lives == 0:       #determine if the player wins or loses
        print('You Lose! The word was', word);
    else:
        print('You Win! The word was', word);


if __name__ == "__main__":
    gamestart();