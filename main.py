Main.py
import random
from words import word_list
import cowsay



def get_word():
    word = random.choice(word_list)  # dialego mia tixea leksi apo tin lista 
    return word.upper()


def play(word):
    name = input("Πως σε λενε: ")
    print("Γεια σου " + name)
    print("\n")

    choice = str(input("Θεσ να δοκιμασεις τις ικανοτητες σου και να βρεις την λεξη μου ή θες να βρω εγω την λεξη σου? (1 ή 2): "))   # dialegi o pektis gamemode
    print("\n")

    if choice == "2":
        import pc_guesser
        player_word = str(input("βαλε μια λεξη: ").upper())
        word1 = player_word
        pc_guesser.play1(word1)
        while input("Play Again? (Y/N) ").upper() == "Y":    #rotaei ama thes na ksanapeksis
             word = get_word()
             play(word)
        
    word_completion = "_" * len(word) 
    guessed = False
    guessed_letters = []                            #emfanizete h kremala kai oi thesis gia ta grammata 
    guessed_words = []
    tries = 6
    print("Ετοιμος να παιξεις")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Βαλε ενα γραμμα: ").upper()              # emfanizete to input gia na isagi o paiktis ena gramma kai to metatrepi se kefaleo 
        if len(guess) == 1 and guess.isalpha():                 #elegxi ama o xaraktiras pou vazei o pektis aniki sthn alfavito 
            if guess in guessed_letters:                        
                print("Εχεις ξαναπει το ", guess)               # elegxi ama to gramma pou valame exei ksanabei 
            elif guess not in word:                             #ama den to exoyme ksanavalei kai den iparxi stin leksi tote mas to leei kai mas aferei mia prospathia 
                print( "το " + guess +  " δεν ειναι στην λεξη.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Μπραβο το " + guess+ " ειναι στην λεξη")      
                guessed_letters.append(guess)
                word_as_list = list(word_completion)                    # ama to gramma pou valame einai mesa stin leksi to emfanizni stin analogi thesi 
                indices = [i for i, letter in enumerate(word) if letter == guess]    
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:                          # elegxi ama to grama pou vlame oloklironi tin leksi h oxi 
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("Εχεις ξαναπει το γραμμα ", guess)
            elif guess != word:
                print("το " + guess +  "δεν ειναι στην λεξη.")      # elegxi ama to gramma den einai stin leksi ,aferei mia prospathia kai emfanizi to anologo minima 
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Κατι πατισες λαθος")             # parametros pou den se afinei na valeis kati allo ektos apo enan xarakthra 
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        cowsay.cheese("Μπραβο βρηκες την λεξη ")
    else:
        cowsay.daemon("Συγγνωμη σε κρεμασαμε, αλλα η λεξη ηταν " + word + ". Maybe next time!")


def display_hangman(tries):                         
    stages = [  # olo to soma 
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \
                   -
                """,
                # xeria kefali kai 1 podi
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / 
                   -
                """,
                # xeria kai kefali
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |      
                   -
                """,
                # kefali kai ena xeri 
                """
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |     
                   -
                """,
                # kefali kai soma 
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # kefali
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # proto level
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


def main():
    word = get_word()     #trexei to programma 
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":    #rotaei ama thes na ksanapeksis
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()




