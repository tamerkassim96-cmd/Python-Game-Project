import sys
import time
from func import slow_text
from colorama import Fore

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

print(Fore.LIGHTRED_EX)
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
slow_text(f'But there is {Fore.LIGHTMAGENTA_EX} hope...')
time.sleep(1)
print()

print()
slow_text('one soul that could change')
time.sleep(0.2)
print()
print()
slow_text(Fore.GREEN + 'everything.')
time.sleep(1)
print()

print()
slow_text(Fore.LIGHTMAGENTA_EX + 'That could stand against the darkness,')
time.sleep(1)
print()

print()
slow_text('someone with the willpower and heart to defy the Shadow King himself.')
time.sleep(1)
print()

print()
slow_text('You are the only one left amongst the rubble')
time.sleep(1)
print()

print()
slow_text('The only one that can fight...')
time.sleep(1)
print()


print()
time.sleep(1)
while True:
    user_input = input(


     f"Will you help us...{Fore.YELLOW} warrior?{Fore.RED} (yes/no): "
    ).strip().lower()

    if user_input == 'yes' or user_input == 'y':
        print()
        slow_text('Thank you so much for helping us warrior')
        time.sleep(1)
        slow_text(' we now have a glimpse of hope!')
        print()
        time.sleep(1)
        break

    elif user_input == 'no' or user_input == 'n':
        slow_text('Then im afraid our world is doomed... farewell,')
        print()
        time.sleep(1)

        print()
        slow_text('Please exit the game.')
        print()
        time.sleep(1)

        print()
        input('Press ENTER to exit...')
        print()
        sys.exit(0)



    else:
        print()
        slow_text('Sorry I dont understand, please try again.')
        print()
        time.sleep(1)



print()
time.sleep(0.5)
print()

if user_input == 'yes' or user_input == 'y':
    name = input('Please enter your name: ')

print()
time.sleep(1)
name = name.strip()
print()
slow_text(f'{name} Eh? a fine name for a warrior... We need you!')
time.sleep(1)
print()
print()

print()
slow_text(f'Before we begin {name}, choose your class!')
print()
time.sleep(1)
print()
print()
slow_text(f'{Fore.RESET}1. {Fore.LIGHTCYAN_EX}Vanguard - Front line attacker, Deals medium-high damage, Medium defense')
time.sleep(1)
print()
print()
slow_text(f'{Fore.RESET}2. {Fore.LIGHTMAGENTA_EX}Wraith - Magic user, Ranged attack, low-medium damage, low defense')
time.sleep(1)
print()
print()
slow_text(f'{Fore.RESET}3. {Fore.LIGHTYELLOW_EX}Phantom - Speedy attacker, Stealthy, Medium damage, Medium-low defense')
print()

print()

while True:
    print()
    choice = input(f'{Fore.LIGHTWHITE_EX}Enter your choice: ').strip().lower()
    print()


    if choice == '1' or choice == 'vanguard':
        slow_text(f'{Fore.LIGHTCYAN_EX}Vanguard, I see you are a brave warrior. An excellent choice {name}!{Fore.RESET}')
        print()
        break



    elif choice == '2' or choice == 'wraith':
        slow_text(f'{Fore.LIGHTMAGENTA_EX}Wraith, a wise decision {name}! I see you like to keep distance in battle.{Fore.RESET}')
        print()
        break


    elif choice == '3' or choice == 'phantom':
        slow_text(f'{Fore.LIGHTYELLOW_EX}Phantom, a great choice {name}! a sneaky aggressor I see eh?{Fore.RESET}')
        print()
        time.sleep(1)
        break

    else:
        print()
        slow_text(f'{Fore.LIGHTWHITE_EX}Invalid input, please try again.')
        print()
        print()
        time.sleep(1)




print()
print()

#Introduction to the story line:

time.sleep(1)

slow_text(f'{Fore.LIGHTRED_EX}Now that you have chosen your class.')
print()
time.sleep(1)

print()
slow_text(f'Listen closely {name}...')
print()

time.sleep(1)

print()
slow_text('our land has fallen into the darkness')
print()

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
slow_text('but beware... this is not an easy journey,')
print()

print()
slow_text('You will need serious training...')
print()
time.sleep(1)


#Training Arc
