import random;

LIST_WORDS = ['Elephant', 'Python', 'Anaconda', 'Jazz', 'Keyboard'];

def chooseWords():
    return random.choice(LIST_WORDS);


def guessWord(letter, word, blank):   #fill the blank with the guess word
    new_string = [];
    
    for index in range(len(word)):
        if word[index].lower() == letter.lower():
            if word[index].isupper():
                new_string.append(letter.upper());
            else:
                new_string.append(letter);
        elif blank[index] == '_':
            new_string.append('_');
        else:
            new_string.append(blank[index]);
    
    return new_string; #return blanks with new letters


def rightLetter(let, word, blank):   #execute if the player guess the correct letter
    count = word.lower().count(let.lower());
    print(f'There are {count} letters in the word.');
    blank = guessWord(let, word, blank);
    
    return blank; #return blanks with new letters

    

def wrongLetter(let):       #execute if the player guess the wrong letter
    print(f'There is no {let} in the word.'); 


def gamestart():
    live = 5;
    word = chooseWords();
    isBlank = True;

    blank_string = [];
    for x in range(len(word)):
        blank_string.append('_');  #create blank string for user to know how long is the word
    
    print(f'{blank_string}\n');

    while live != 0 and isBlank:
        guessLetter = input('Please enter the guess letter: ');

        if guessLetter == 'exit':
            exit();

        if guessLetter.lower() in word.lower(): #check if the guess letter is in the word in any form
            blank_string = rightLetter(guessLetter, word, blank_string);
            print(f'Lives: {live}');
            print(f'{blank_string}\n');
        else:
            wrongLetter(guessLetter);
            live -= 1;
            print(f'Lives: {live}')
            print(f'{blank_string}\n');

        if '_' not in blank_string:
            isBlank = False;

    if isBlank and live == 0:
        print('You Lose!');
    else:
        print('You Win!');

if __name__ == "__main__":
    gamestart();