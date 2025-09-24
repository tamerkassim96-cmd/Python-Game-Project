import sys
import time
from func import slow_text
from colorama import Fore

print(Fore.GREEN + 'This is green text')
print(Fore.BLUE + 'This is blue text')
print(Fore.CYAN + 'This is cyan text')
print(Fore.YELLOW + 'This is yellow text')
print(Fore.RESET + 'This is light blue text')
print()


slow_text('Loading...')
time.sleep(0.3)
print()
print()
slow_text('25%...')
time.sleep(0.2)
print()
print()
slow_text('50%...')
time.sleep(0.1)
print()
print()
slow_text('75%...')
time.sleep(0.05)
print()
print()
slow_text('100%...')
print()
time.sleep(0.01)
print()
print()
slow_text('Welcome player to the...')
time.sleep(1)
print()

print(Fore.YELLOW + """
███████╗ ██████╗██╗  ██╗ ██████╗ ███████╗███████╗     ██████╗ ███████╗
██╔════╝██╔════╝██║  ██║██╔═══██╗██╔════╝██╔════╝    ██╔═══██╗██╔════╝
█████╗  ██║     ███████║██║   ██║█████╗  ███████╗    ██║   ██║█████╗
██╔══╝  ██║     ██╔══██║██║   ██║██╔══╝  ╚════██║    ██║   ██║██╔══╝
███████╗╚██████╗██║  ██║╚██████╔╝███████╗███████║    ╚██████╔╝██║
╚══════╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝     ╚═════╝ ╚═╝

████████╗██╗  ██╗███████╗
╚══██╔══╝██║  ██║██╔════╝
   ██║   ███████║█████╗
   ██║   ██╔══██║██╔══╝
   ██║   ██║  ██║███████╗
   ╚═╝   ╚═╝  ╚═╝╚══════╝

███████╗ ██████╗ ██████╗  ██████╗  ██████╗ ████████╗████████╗███████╗███╗   ██╗
██╔════╝██╔═══██╗██╔══██╗██╔════╝ ██╔═══██╗╚══██╔══╝╚══██╔══╝██╔════╝████╗  ██║
█████╗  ██║   ██║██████╔╝██║  ███╗██║   ██║   ██║      ██║   █████╗  ██╔██╗ ██║
██╔══╝  ██║   ██║██╔══██╗██║   ██║██║   ██║   ██║      ██║   ██╔══╝  ██║╚██╗██║
██║     ╚██████╔╝██║  ██║╚██████╔╝╚██████╔╝   ██║      ██║   ███████╗██║ ╚████║
╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝    ╚═╝      ╚═╝   ╚══════╝╚═╝  ╚═══╝
""")

print(Fore.RESET)

print()
input('Press ENTER to continue...')
print()

print(Fore.RED)
print()
slow_text('We have been defeated...')
time.sleep(1)
print()

print()
slow_text('our armies shattered')
time.sleep(1)
print()

print()
slow_text('our cities burned.')
time.sleep(1)
print()

print()
slow_text('The Shadow Kings guards hunting us down like heartless creatures.')
time.sleep(1)
print()

print()
slow_text('Families torn apart... hope slowly fading.')
time.sleep(1)
print()

print()
slow_text('Our lives now lie in ruins, and we will soon become nothing but forgotten echoes in the dark.')
time.sleep(1)
print()

print()
slow_text('But there is hope...')
time.sleep(1)
print()

print()
slow_text('one soul that could change')
slow_text(Fore.GREEN + ' everything')
slow_text(Fore.RED + ',')
time.sleep(1)
print()

print()
slow_text('that could stand against the darkness.')
time.sleep(1)
print()

print()
slow_text('A warrior...')
time.sleep(1)
print()

print()
slow_text('someone with the willpower and heart to defy the Shadow King himself.')
time.sleep(1)
print()

print()
time.sleep(1)
while True:
    print()
    user_input1 = input('Will you help us...')

    slow_text(Fore.YELLOW + 'warrior? (yes/no): ')
    print()

    if user_input1.strip().lower() == 'yes' or user_input1.strip().lower() == 'y':
        slow_text('Thank you so much for helping us warrior, we now have a glimpse of hope!')
        print()
        time.sleep(1)
        break

    elif user_input1.strip().lower() == 'no' or user_input1.strip().lower() == 'n':
        slow_text('Then im afraid our world is doomed... farewell,')
        print()
        time.sleep(1)

        print()
        slow_text('Please Exit The Game.')
        print()
        time.sleep(1)

        print()
        input('Press ENTER to exit...')
        print()
        sys.exit(0)



    else:
        slow_text('Sorry I dont understand, please try again.')
        print()
        time.sleep(1)



print()
time.sleep(0.5)
print()

if user_input1.strip().lower() == 'yes' or user_input1.strip().lower() == 'y':
    name = input('Please enter your name: ')

print()
time.sleep(1)
name = name.strip()
print()
slow_text(f'{name} eh? a fine name for a warrior... We need you!')
time.sleep(1)
print()
print()

print()
slow_text(f'Before we begin {name}, choose your class!')
print()
time.sleep(1)
print()
print()
slow_text('1. Vanguard - Front line attacker, Deals medium-high damage, Medium defense')
time.sleep(1)
print()
print()
slow_text('2. Wraith - Magic user, Ranged attack, low-medium damage, low defense')
time.sleep(1)
print()
print()
slow_text('3. Phantom - Speedy attacker, Stealthy, Medium damage, Medium-low defense')
print()

print()

while True:
    print()
    user_input = input('Enter your choice: ')
    print()


    if user_input == '1' or user_input.lower() == 'vanguard':
        slow_text(f'Vanguard, I see you are a brave warrior. An excellent choice {name}!')
        print()
        break



    elif user_input == '2' or user_input.lower() == 'wraith':
        slow_text(f'Wraith, a wise decision {name}! I see you like to keep distance in battle. ')
        print()
        break


    elif user_input == '3' or user_input.lower() == 'phantom':
        slow_text(f'Phantom, a great choice {name}! a sneaky aggressor I see eh?')
        print()
        time.sleep(1)
        break

    else:
        print()
        slow_text('Invalid input, please try again.')
        print()
        print()
        time.sleep(1)




print()
print()

#Introduction to the story line:

time.sleep(1)

slow_text(f'Now that you have chosen your class.')
print()
time.sleep(1)

print()
print()
slow_text(f'Listen closely {name}...')
print()

time.sleep(1)

print()
(slow_text('our land has fallen into the'), slow_text(Fore.RED + ' darkness'),
slow_text(Fore.LIGHTBLUE_EX + ','))
print()

print(Fore.LIGHTBLUE_EX)
print()
time.sleep(1)
slow_text('The Dark King rules with fear.')
print()
time.sleep(1)

print()
slow_text(f'You are the only one capable {name} to be able to reclaim the light taken from us,')
print()
time.sleep(1)

print()
slow_text('but beware... this is not an easy journey.')
print()
time.sleep(1)
