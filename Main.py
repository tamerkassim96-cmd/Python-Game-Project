import time
import sys

from func import slow_text
from colorama import Fore
from colorama import init
init()

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
print()
print()
time.sleep(0.75)
slow_text('Welcome player to the...')
time.sleep(1)
print()

print(Fore.LIGHTYELLOW_EX + """

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
time.sleep(1)
print()

# Introduction To The Storyline

print(Fore.LIGHTBLUE_EX)

slow_text(f'''Welcome to Asgiaburn,

A land that was once flourished with peace and prosperity,

Where communities gathered, where villages thrived in celebration.

Beneath golden skies and sparkling stars, 

A land once joyous, turned to''')

time.sleep(1)
print()

print()
slow_text(f'{Fore.LIGHTRED_EX}ruin.')
print()
time.sleep(1)
print()
slow_text('We have been defeated...')
time.sleep(1)
print()

print()
slow_text('our armies shattered,')
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
slow_text('Families torn apart... each day we fall further into despair.')
time.sleep(1)
print()

print()
slow_text('Our lives now lie in ruins, and we will soon become nothing but forgotten echoes in the dark.')
time.sleep(1)
print()

print()
slow_text('But there is')
print()
print()
time.sleep(0.2)
slow_text(f'{Fore.LIGHTMAGENTA_EX}hope...')
time.sleep(1)
print()

print()
slow_text('one soul that could change')
time.sleep(0.2)
print()
print()
slow_text('everything.')
print()
time.sleep(1)
print()
slow_text(Fore.LIGHTMAGENTA_EX + 'Some could say he is labelled the')
print()
time.sleep(1)

print()
slow_text(f'{Fore.LIGHTYELLOW_EX}Radiant')
print()
time.sleep(1)

print()
slow_text(f'{Fore.LIGHTMAGENTA_EX}someone with the willpower and heart to defy the Shadow King himself.')
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

        f"Will you help us...{Fore.LIGHTYELLOW_EX} warrior?{Fore.RESET} (yes/no): "
    ).strip().lower()

    print(Fore.BLUE)
    if user_input == 'yes' or user_input == 'y':
        print()
        slow_text('Thank you so much for helping us warrior')
        time.sleep(1)
        print()
        print()
        slow_text('we now have a glimpse of hope!')
        print()
        time.sleep(1)
        break

    elif user_input == 'no' or user_input == 'n':
        slow_text(f'{Fore.RED}Then im afraid our world is doomed... farewell,')
        print()
        time.sleep(1)

        print()
        slow_text(f'{Fore.RESET}Please exit the game.')
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
    name = input(f'{Fore.RESET}Please enter your name: ')

print()
time.sleep(1)
name.strip()
print()
slow_text(f'{Fore.LIGHTBLUE_EX}{name} Eh? a fine name for a {Fore.LIGHTYELLOW_EX}Radiant{Fore.LIGHTBLUE_EX} I mean warrior')
time.sleep(0.5)
print()
print()

print()
slow_text(f'{Fore.RESET}Before we begin training {name}, choose your class!')
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
time.sleep(2)
print()
slow_text(f'{Fore.LIGHTRED_EX}...??? eRrOr, Unauthorised class detected, ADMIN ACCESS ONLY!, ACCESS OVERRIDE: SECRET CLASS{Fore.LIGHTYELLOW_EX} [???????]')

print()

attack = f'{Fore.LIGHTRED_EX}\nAttack'
health = f'{Fore.LIGHTGREEN_EX}\nHealth'
defense = f'{Fore.LIGHTBLUE_EX}\nDefense'
speed = f'{Fore.YELLOW}\nSpeed'
magic = f'{Fore.LIGHTMAGENTA_EX}\nMagic'

vanguard = f'{Fore.LIGHTCYAN_EX}Vanguard'
wraith = f'{Fore.LIGHTMAGENTA_EX}Wraith'
phantom = f'{Fore.LIGHTYELLOW_EX}Phantom'
radiant = f'{Fore.LIGHTYELLOW_EX}Radiant'

class_stats = {
'vanguard': {
    attack: 23,
    health: 150,
    defense: 10,
    speed: 8,
    magic: 0
},
'wraith': {
    attack: 17,
    health: 120,
    defense: 10,
    speed: 8,
    magic: 20
},
'phantom': {
    attack: 20,
    health: 130,
    defense: 10,
    speed: 15,
    magic: 5,
},
'radiant': {
    attack: 48,
    health: 200,
    defense: 100,
    speed: 70,
    magic: 40,
    }

}

while True:
    print()
    choice = input(f'{Fore.RESET}Enter your choice: ').strip().lower()
    print()

    if choice == '1' or choice == 'vanguard':
        slow_text(
            f'{Fore.LIGHTCYAN_EX}Vanguard. So you arent afraid of being on the front lines, A trait of a true fighter destined for victory. An excellent choice {name}!')
        print()
        break



    elif choice == '2' or choice == 'wraith':
        slow_text(
            f'{Fore.LIGHTMAGENTA_EX}Wraith, a wise decision {name}! I see you like to keep distance in battle.{Fore.RESET}')
        print()
        break


    elif choice == '3' or choice == 'phantom':
        slow_text(f'{Fore.LIGHTYELLOW_EX}Phantom, a great choice {name}! a sneaky aggressor I see eh? {Fore.RESET}')
        print()
        time.sleep(1)
        break

    elif choice == 'radiant' or choice == 'the radiant':
        slow_text('ACCESS OVERRIDE ACCEPTED... Classified class unlocked: Radiant')
        print()
        time.sleep(1)
        break

    else:
        print()
        slow_text('That class doesnt exist, try again.')
        print()
        print()
        time.sleep(1)
        continue



player_stats = class_stats[choice]

print()
slow_text(f'{Fore.LIGHTCYAN_EX}--- PLAYER CLASS ---')
time.sleep(0.5)
print()
slow_text(f'{Fore.LIGHTYELLOW_EX}Class: {choice.capitalize()}{Fore.RESET}')
time.sleep(0.2)

for stat, value in player_stats.items():
    slow_text(f'{stat.capitalize()}: {value}')
    time.sleep(0.2)

print()
slow_text(f'{Fore.LIGHTCYAN_EX}---------------------{Fore.RESET}')
time.sleep(1)
print()

print()
print()

# Introduction to the story line:

time.sleep(1)

slow_text(f'{Fore.LIGHTMAGENTA_EX}Now that you have chosen your class, you are ready for battle... but,')
print()
time.sleep(1)

print()
slow_text(f'{Fore.LIGHTRED_EX}Listen closely {name}...')
print()

time.sleep(1)

print()
slow_text('our land has fallen into the darkness')
print()

print()
time.sleep(1)
slow_text('The Shadow King rules with fear.')

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

# Training Arc
