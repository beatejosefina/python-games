# Importerar random för att kunna slumpa fram alternativ med .choice metoden
import random as r

print('\n-------- 🐍 Welcome to Paper-Rock-Scissor! 🐍 --------\n')
user_name = input('What do you want to call yourself? ').capitalize()
print(f"Nice to meet you, {user_name}!")

# while-loop, forsätter tills seplaren anger ett giltigt antal rundor (1-10)
user_rounds = 0
while user_rounds <= 0 or user_rounds > 10:
    user_rounds = input('How many rounds are you up for? ')
    try:
        # Verifierar att användaren matat in en int
        user_rounds = int(user_rounds)
        if user_rounds <= 0:
            print("Hmm that's no fun, please give me a number between 0-10")
        elif user_rounds <= 10:
            print(f"Ok, {user_name}, that's fine by me! Let's play {user_rounds} rounds.")
        else:
            print (f"WOW, {user_name}, {user_rounds}?? That's a bit too much for me, sorry! Maybe we can settle for somwhere between 0-10 instead?")
    except ValueError:
        # Hanterar exception, sätter user_rounds = 0 för att fortsätta uppfylla while-villkoret 
        user_rounds = 0
        print('Please enter a number')

# Poäng-score, räknas upp inuti for-loopen 
computer_score = 0
user_score = 0

# For-loop, pågår upp till det av spelaren bestämda antalet omgångar. Startart räkningen från 1 vilket medför att rangen måste förskjutas med ett för att det ska bli rätt antal tot omgångar får spelaren. 
for round in range(1, user_rounds + 1):

    # [X] Datorn slumpar vilken av sten, sax eller påse den ska välja.
    mylist = ["📄", "🪨", "✂️"] 
    computer_choice = r.choice(mylist)

    # [X] Spelaren väljer också sten, sax eller påse.
    # While-loop forttgår tills användaren anger korrekt input 
    user_choice = ""
    while user_choice == "":
        user_choice = input('\nChoose your weapon: Paper(P), Rock(R), Scissors(S) > ')
        # mappning av str-input till motsvarande emoji
        if user_choice.upper() == 'P':
            user_choice = "📄"
        elif user_choice.upper() == 'R':
            user_choice = "🪨"
        elif user_choice.upper() == 'S':
            user_choice = "✂️"
        else:
            user_choice =""
            print("Interesting choice, but that's not how you play this game.")

    # [X] Datorn och spelaren visar sedan upp sina val samtidigt.
    print(f'\nRound {round}:\nComputer: {computer_choice} - {user_name}: {user_choice}')

    # [X] Reglerna är enligt följande: sten vinner över sax, sax vinner över påse, och påse vinner över sten. Om båda väljer samma alternativ blir det oavgjort.
    if computer_choice == user_choice:
        print("Tie!")
    elif (computer_choice == "📄" and user_choice == "🪨") or (computer_choice == "🪨" and user_choice == "✂️") or (computer_choice == "✂️" and user_choice == "📄"):
        computer_score += 1
        print('Computer wins!')
    else:
        user_score += 1
        print(f'{user_name} wins!')
        
    print(f'Computer: {computer_score} - {user_name}: {user_score}')
    
    # Upräkning av for-vilkoret, används även för att dynamisk meddela användaren om vilket omgång som pågår och hur många omgångar det är kvar.
    round += 1
    rounds_left = (user_rounds + 1) - round

    if rounds_left > 1:
        print(f'\n{rounds_left} rounds to go!')
    elif rounds_left == 1:
        print('\nFinal round!')

# [X] Spelaren spelar tills hen vinner eller förlorar mot datorn.
print('\nGame over!')
if computer_score > user_score:
    print('Computer is the champion! 🏆')
elif computer_score < user_score:
    print(f'{user_name} is the champion! 🏆')
else:
    print("Wow, tie. I guees everyone's a winner then 🏆")
    
print(f'\n-------- 🐍 Thanks for playing, see you soon, {user_name} 🐍 -------- \n')






