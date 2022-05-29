pc_plays.py
from words import word_list as wd
from words import alphabet as ab
import random
import cowsay 
import time 


i = 0
for i in range(len(wd)):
    print(wd[i] + "\n")                                         #emfanizi oles tis leksis sto database tin mia kato apo tin alli 
    i = i+1
print("\n")
print("Διαλεξε μια λεξη απο τις παραπανω ή βαλε μια απο το μυαλο σου")
print("\n")




def play1(word1):
    print(word1)
    word_completion = "_" * len(word1) 
    guessed = False
    guessed_letters = []                            #emfanizete h kremala kai oi thesis gia ta grammata 
    guessed_words = []
    tries = 6
    print(display_hangman_pc(tries))
    print(word_completion)
    print("\n")
    
    while not guessed and tries > 0:
        time.sleep(4)
        guess = random.choice(ab)         #dialegi ena tixeo gramma apo tin abc
        if len(guess) == 1 and guess.isalpha():                 #elegxi ama o xaraktiras pou vazei o pektis aniki sthn alfavito 
            if guess in guessed_letters:   
                print("Για να δοκιμασω το " + guess)
                time.sleep(2)
                print("το ξεχασα οτι το ξαναειπα")               # elegxi ama to gramma pou evale exei ksanabei 
            elif guess not in word1:  
                print("Για να δουμε το " + guess)
                time.sleep(2)
                reactions1 = ["Αμα συνεχισω ετσι θα χασω", "κατι μου λεει οτι η λεξη σου ειναι δυσκολη", "Καποιο hint σε παρακαλω"]         
                print(random.choice(reactions1))                                                                                        # opote xanei leei mia frash 
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Για να δουμε το " + guess)
                time.sleep(2)
                reactions2 = ["Ειμαι οσο εξυπνος οσο ενας υπολογιστης", "Δεν το εβαλα στην τυχη, αληθεια λεω", "Παμεεεεεεεεεε Λιγοοο"]
                print(random.choice(reactions2))      
                guessed_letters.append(guess)
                word_as_list = list(word_completion)                    # ama to gramma pou evale einai mesa stin leksi to emfanizni stin analogi thesi 
                indices = [i for i, letter in enumerate(word1) if letter == guess]    
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:                          # elegxi ama to grama pou evale oloklironi tin leksi h oxi 
                    guessed = True
        elif len(guess) == len(word1) and guess.isalpha():
            if guess in guessed_words:
                print("το ξεχασα οτι το ξαναειπα")
            elif guess != word1:
                print(random.choice(reactions1))              # elegxi ama to gramma den einai stin leksi kai aferei mia prospathia kai emfanizi to anologo minima 
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word1
        else:
            print("Κατι πατισα λαθος sorry")             # parametros pou den se afinei na valeis kati allo ektos apo enan xarakthra 
        print(display_hangman_pc(tries))
        print(word_completion)
        print("\n")
    if guessed:
        cowsay.tux("Οριστε το πραγματικο μου πρωσοπο")
        
    else:
        cowsay.ghostbusters("Αυτοκτονια")
         
def display_hangman_pc(tries):                         
    stages = [  # olo to soma 
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \
                  ---
                """,
                # xeria kefali kai 1 podi
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / 
                  ---
                """,
                # xeria kai kefali
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |      
                  ---
                """,
                # kefali kai ena xeri 
                """
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |     
                  ---
                """,
                # kefali kai soma 
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                  ---
                """,
                # kefali
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                  ---
                """,
                # proto level
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                  ---
                """
    ]
    return stages[tries]

    def start():
        word1 = player_word     #trexei to programma 
        play1(word1)
