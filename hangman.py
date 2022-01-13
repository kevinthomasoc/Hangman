import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    
    
    inFile = open(WORDLIST_FILENAME, 'r')
    
    line = inFile.readline()
    
    wordlist = line.split()
    return wordlist

def chooseWord(wordlist):
    
    return random.choice(wordlist)





wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    
    
    wordlist = []   
    for char in secretWord:
        wordlist.append(char.lower())
    wordlistset = set(wordlist)
    finallist = []
    for word in wordlistset:
        finallist.append(word)


        
    for char in lettersGuessed:        
        for letter in finallist:
            if str(char) == str(letter):
                finallist.remove(letter)
                
    if len(finallist) == 0:
        return True
    elif len(finallist) != 0:
        return False
  




def getGuessedWord(secretWord, lettersGuessed):
    
    
    word = []
    for char in secretWord:
        word.append(char)

    for i in range(len(word)):
        if (word[i] in lettersGuessed) == False:
            word[i] = "_"
    emp = ""
    for char in word:
        emp += char
            
        
    return emp
    



def getAvailableLetters(lettersGuessed):
    
    
    word = "abcdefghijklmnopqrstuvwxyz"
    wordlist = []
    for char in word:
        wordlist.append(char)
    for char in lettersGuessed:
        if (char in wordlist) == True:
            wordlist.remove(char)
    emp = ""
    for char in wordlist:
        emp += char
  
    return emp




def hangman(secretWord):
    
    
    listofguesses = []
    count = 0
    listofgoodletters = []
    for char in secretWord:
        count += 1
    print("The secret word has " + str(count) + " letters.")
    guesscount = 0
    totalcount = 8


        


    while isWordGuessed(secretWord, listofguesses) == False:
        
        validletters = []
        HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''','''
               
  +---+
  |   |
  O   |
 /|\  |
 / \_  |
      |
=========''','''
               
  +---+
  |   |
  O   |
 /|\  |
_/ \_ |
      |
=========''']

        for char in secretWord:
            validletters.append(char)

        guess = (input("Enter a letter:")).lower()
        while ((guess.isalpha()) == False):
            guess = input("Enter a letter:")

    
        if (guess in listofguesses) == True:
            print("You have already guessed this")
            continue
        if (guess not in validletters) == True:
            totalcount -= 1
            if totalcount == (-1):
                print("Sorry, you have lost :C the word was, " + secretWord)
                return
            print("That is incorrect, you have " +str(totalcount) + " guesses left")
            guesscount += 1


        print(HANGMANPICS[(guesscount)])
        
            
        
        

        listofguesses.append(guess)


        print(getGuessedWord(secretWord, listofguesses))

    if isWordGuessed(secretWord, listofguesses) == True:
        print("Congradulations, you have won!")
        






secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
