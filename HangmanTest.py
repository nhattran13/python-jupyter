import random;

LIST_WORDS = ['Elephant', 'Python', 'Anaconda', 'Jazz', 'Keyboard'];

def chooseWords():
    return random.choice(LIST_WORDS);

     
def drawHangman(lives):     # draw hangman using list with triple quotes
    stages = [
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
    print(stages[-(lives)-1]);



def guessWord(letter, word, blank):   #fill the blank with the guess word
    
    for index in range(len(blank)):
        if word[index].lower() == letter:
            blank[index] = letter;
    
    return blank; #return blanks with new letters

def rightLetter(let, word, blank):   #execute if the player guess the correct letter
    count = word.lower().count(let.lower());
    print(f'There are {count} letters in the word.');
    blank = guessWord(let, word, blank);
    
    return blank; #return blanks with new letters

    

def wrongLetter(let):       #execute if the player guess the wrong letter
    print(f'There is no {let} in the word.'); 


def gamestart():
    live = 6;       #lives
    word = chooseWords();  #choose word from guesslist
    isBlank = True;         #if there is any blank of the guess string

    blank_string = ['_'] * len(word);           #initialize blank string for player to guess
    
    
    drawHangman(live);
    print(f'{blank_string}\n');
    

    while live != 0 and isBlank:            #loop until no lives left or the word has been guessed
        guessLetter = input('Please enter the guess letter: ');
 #       if guessLetter == 'exit':   #test for exit the program
 #           exit();

        if (guessLetter.lower() not in blank_string) and (guessLetter.lower() in word.lower()): #check if the guess letter is in the word in any form
            blank_string = rightLetter(guessLetter, word, blank_string);
            drawHangman(live);
            print(f'Lives: {live}');
            print(f'{blank_string}\n');
        
        elif guessLetter.lower() in blank_string:       #execute if the letter has already guessed
            drawHangman(live);
            print('You already guessed the letter', guessLetter);
            print(f'Lives: {live}');
            print(f'{blank_string}\n');
        
        else:                           #execute if the player guesses the wrong letter
            live -= 1;
            drawHangman(live);
            wrongLetter(guessLetter);
            print(f'Lives: {live}')
            print(f'{blank_string}\n');

        if '_' not in blank_string:
            isBlank = False;
        


    if isBlank and live == 0:       #determine if the player wins or loses
        print('You Lose! The word was', word);
    else:
        print('You Win! The word was', word);

if __name__ == "__main__":
    gamestart();