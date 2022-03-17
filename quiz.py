
#Fragen
question1 = "Welches Tier ist das größte Tier auf der Welt?"
question2 = "Wofür steht IPA?"
question3 = "Wer hat die Mona Lisa gemalt?"
question4 = "Welche Abkürzung hat der Flughafen in Los Angeles (L.A. International Airport)"
question5 = "In welchem Jahr wurde Abraham Lincoln geboren?"

#Punktestand
score = 1

#intro
print("Wilkommen zum Quiz!")
name = input("Wie ist dein Name? ")
print("Vielen Dank, Wilkommen", name)
choice = input("Möchtest du mit oder ohne multiple choice spielen? (y/n)")

#fragen Multiple Choice
def frage1():
    print("Hier ist die erste Frage:")
    print(question1)
    print("1. Löwe\n2. Elefant\n3. Wal\n4. Giraffe")
    answer1 = input("Bitte gib hier deine Antwort ein: ")
    if answer1.lower() == "wal" or answer1.lower() == "3":
        print("Das ist Korrekt!")
        print(" ")
        score == 1
        
    else:
        print("Das ist leider nicht richtig.")
        print(" ")
   

def frage2():
    print("Hier ist die zweit Frage:")
    print(question2)
    print("1. Israel Pale Ale\n2. Internationales Phonetisches Alphabet\n3. International Police Academy\n4. Isopropanalkohol")
    answer2 = input("Bitte gib hier deine Antwort ein: ")
    if answer2.lower() == "internationales phonetisches alphabet" or answer2.lower() == "2":
        print("Das ist richtig!")
        print(" ")
        score == score+1
        
    else:
        print("Das ist leider nicht richtig.")
        print(" ")
    
    

def frage3():
    print("Hier ist die dritte Frage:")
    print(question3)
    print("1. Leonardo Davinci\n2. Leonardi DiCaprio\n3. Julius Caesar\n4. Vincent van Gogh")
    answer3 = input("Bitte gib hier deine Antwort ein: ")
    if answer3.lower() == "leonardo davinci" or answer3.lower() == "1":
        print("Das ist korrekt!")
        print(" ")
        score == score+1
        
    else:
        print("Das ist leider nicht richtig.") 
        print(" ")   
    

def frage4():
    print("Hier ist die vierte Frage:")
    print(question4)
    print("1. LAA\n2. LAIA\n3. LAI\n4. LAX")
    answer4 = input("Bitte gib hier deine Antwort ein: ")
    if answer4.lower() == "lax" or answer4.lower() == "4":
        print("Das ist korrekt!")
        print(" ")
        score == score+1
        
    else:
        print("Das ist leider nicht richtig.")
        print(" ")
    

def frage5():
    print("Hier ist die fünfte Frage:")
    print(question5)
    print("1. 1853\n2. 1807\n3. 1912\n4. 1763")
    answer5 = int(input("Bitte gib hier deine Antwort ein: "))
    if answer5 == 1807 or answer5 == 2:
        print("Das ist korrekt!")
        print(" ")
        score == score+1
        
    else:
         print("Das ist leider nicht richtig.")
         print(" ")


#Fragen ohne Multiple Choice

def qst1():
    print("Hier ist die erste Frage:")
    print(question1)
    answer1 = input("Bitte gib hier deine Antwort ein: ")
    if answer1.lower() == "wal":
        print("Das ist Korrekt!")
        print(" ")
        score == score+1
        
    else:
        print("Das ist leider nicht richtig.")
        print(" ")
    

def qst2():
    print("Hier ist die zweit Frage:")
    print(question2)
    answer2 = input("Bitte gib hier deine Antwort ein: ")
    if answer2.lower() == "internationales phonetisches alphabet":
        print("Das ist richtig!")
        print(" ")
        score == score+1
        
    else:
        print("Das ist leider nicht richtig.")
        print(" ")
   

def qst3():
    print("Hier ist die dritte Frage:")
    print(question3)
    answer3 = input("Bitte gib hier deine Antwort ein: ")
    if answer3.lower() == "leonardo davinci":
        print("Das ist korrekt!")
        print(" ")
        score == score+1
        
    else:
        print("Das ist leider nicht richtig.") 
        print(" ")   
    

def qst4():
    print("Hier ist die vierte Frage:")
    print(question4)
    answer4 = input("Bitte gib hier deine Antwort ein: ")
    if answer4.lower() == "lax":
        print("Das ist korrekt!")
        print(" ")
        score == score+1
        
    else:
        print("Das ist leider nicht richtig.")
        print(" ")
    

def qst5():
    print("Hier ist die fünfte Frage:")
    print(question5)
    answer5 = int(input("Bitte gib hier deine Antwort ein: "))
    if answer5 == 1807:
        print("Das ist korrekt!")
        print(" ")
        score == score+1
        
    else:
         print("Das ist leider nicht richtig.")
         print(" ")

#Ausführung
if choice.lower() == "y":
    frage1()
    frage2()
    frage3()
    frage4()
    frage5()

elif choice.lower() == "n":
    qst1()
    qst2()
    qst3()
    qst4()
    qst5()

#Punktestand
score == score-1
print("Dein Punktestand beträgt:", score)

print("Vielen Dank fürs spielen, ", name, "!")

