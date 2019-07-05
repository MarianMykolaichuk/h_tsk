import random

print('''
         ПАЛИЧКИ
                   ...форт Буаяр едіШн



Правила ГРИ:
         Кожен з гравців витягає від 1 до 3 паличок.
         Програє той, хто останнім робить хід.


''')
while True:
    player_or_computer = input("Обери суперника: Комп'ютер ( cpu ) чи гравець ( p2 ) ??\n")
    if player_or_computer == "cpu" or player_or_computer=="p2":
        break
    print("ей..! Так не спрацює. ")
    
# обираємо кількість паличок

while True:
    number_of_sticks = int(input("Оберіть кількість паличок (від 10 до 50) \n"))
    if number_of_sticks>=10 and number_of_sticks<=50:
        print("Гра почалась!" )
        print('" ' * 7)
        break
    print("Не коректний вибір")

if player_or_computer=="cpu":
    cpu = random.randint(1,3)
       

# початок гри
while number_of_sticks>0:
    # ходи         
    for whose_turn in range(1,3):
        if whose_turn ==1:
            print(" Гравець 1")
        elif whose_turn ==2:
            print("Гравець 2")
        if number_of_sticks==2:
            max_sticks=2
        if number_of_sticks==1:
            max_sticks=1
        if number_of_sticks>2:
            max_sticks=3

       
        while True:         
            
            sticks_taken = int(input("Ваш вибір: "))
            if sticks_taken>=1 and sticks_taken<=max_sticks:
                print("Ви обрали", sticks_taken)
                break
            else:
                print ("Сорі, не правильний вибір .")
                

        number_of_sticks-=sticks_taken
        print("Залишилось", number_of_sticks,)
        print('"' * 7)
        if number_of_sticks==0:
            break
            
if whose_turn==1:
    print("Переміг гравець 2 !")
if whose_turn==2:
    print("Переміг гравець 1 !")
    
    
