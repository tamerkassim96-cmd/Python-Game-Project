import time
import sys

from func import slow_text,slow_print
from colorama import Fore
from colorama import init
init()

# - Intro Loading Screen -
def loading_screen():

    slow_print('Loading...', delay=0.5)

    slow_print('25%...', delay=0.4)

    slow_print('50%...', delay=0.3)

    slow_print('75%...', delay=0.2)

    slow_print('100%...', delay=0)

    slow_print('Initializing...',)

    print()
    slow_print('Welcome player to the...')


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

loading_screen()

# Introduction To The Storyline

def introduction():

    print(Fore.LIGHTBLUE_EX)

    slow_text(f'''Welcome to Asgiaburn,

A land that was once flourished with peace and prosperity,

Where communities gathered, where villages thrived in celebration.

Beneath golden skies and sparkling stars, 

A land once joyous, turned to''')
    print()

    print()
    slow_print(f'{Fore.LIGHTRED_EX}ruin.')

    slow_print('We have been defeated...')

    slow_print('our armies shattered,')

    slow_print('our cities burned.')

    slow_print('The Shadow Kings guards hunting us down like heartless creatures.')

    slow_print('Families torn apart... each day we fall further into despair.')

    slow_print('Our lives now lie in ruins, and we will soon become nothing but forgotten echoes in the dark.')

    slow_print('But there is', delay=0.2)

    slow_print(f'{Fore.LIGHTMAGENTA_EX}hope...')


    slow_print('one soul that could change ', delay=0.2)

    slow_print('everything.')

    slow_print(Fore.LIGHTMAGENTA_EX + 'Some could say he is labelled the')

    slow_print(f'{Fore.LIGHTYELLOW_EX}Radiant')

    slow_print(f'{Fore.LIGHTMAGENTA_EX}someone with the willpower and heart to defy the Shadow King himself.')

    slow_print('You are the only one left amongst the rubble')

    slow_print('The only one that can fight...')

    print()
    time.sleep(1)

introduction()

def ask_help():

    while True:
        user_input = input(

            f"Will you help us...{Fore.LIGHTYELLOW_EX} warrior?{Fore.RESET} (yes/no): "
        ).strip().lower()

        print(Fore.BLUE)
        if user_input == 'yes' or user_input == 'y':
            print()
            slow_print('Thank you so much for helping us warrior')

            slow_print('we now have a glimpse of hope!')
            break

        elif user_input == 'no' or user_input == 'n':
            slow_print(f'{Fore.RED}Then im afraid our world is doomed... farewell,')

            slow_text(f'{Fore.RESET}Please exit the game.')
            print()
            time.sleep(1)

            print()
            input('Press ENTER to exit...')
            print()
            sys.exit(0)



        else:
            print()
            slow_print('Sorry I dont understand, please try again.')


print()
time.sleep(0.5)
print()

ask_help()

def get_player_name():

    global name
    name = input(f'{Fore.RESET}Please enter your name: ')

    print()
    name.strip()
    print()
    slow_print(f'{Fore.LIGHTBLUE_EX}{name} Eh? a fine name for a {Fore.LIGHTYELLOW_EX}Radiant{Fore.LIGHTBLUE_EX} I mean warrior')

get_player_name()


#Class Selection

def class_selection():

    print()
    slow_print(f'{Fore.RESET}Before we begin training {name}, choose your class!')

    slow_print(f'{Fore.RESET}1. {Fore.LIGHTCYAN_EX}Vanguard - Front line attacker, Deals medium-high damage, Medium defense')

    slow_print(f'{Fore.RESET}2. {Fore.LIGHTMAGENTA_EX}Wraith - Magic user, Ranged attack, low-medium damage, low defense')

    slow_print(f'{Fore.RESET}3. {Fore.LIGHTYELLOW_EX}Phantom - Speedy attacker, Stealthy, Medium damage, Medium-low defense',delay=2)

    slow_print(f'{Fore.LIGHTRED_EX}...??? eRrOr, Unauthorised class detected, ADMIN ACCESS ONLY!, ACCESS OVERRIDE: SECRET CLASS{Fore.LIGHTYELLOW_EX} [???????]')

    attack = f'{Fore.LIGHTRED_EX}\nAttack'
    health = f'{Fore.LIGHTGREEN_EX}\nHealth'
    defense = f'{Fore.LIGHTBLUE_EX}\nDefense'
    speed = f'{Fore.YELLOW}\nSpeed'
    magic = f'{Fore.LIGHTMAGENTA_EX}\nMagic'

    class_stats = {
    'vanguard': {
        attack: 23,
        health: 150,
        defense: 10,
        speed: 8,
        magic: 0,
        'colour': Fore.LIGHTCYAN_EX
    },
    'wraith': {
        attack: 17,
        health: 120,
        defense: 10,
        speed: 8,
        magic: 20,
        'colour': Fore.LIGHTMAGENTA_EX
    },
    'phantom': {
        attack: 20,
        health: 130,
        defense: 10,
        speed: 15,
        magic: 5,
       'colour': Fore.LIGHTYELLOW_EX
    },
    'radiant': {
        attack: 48,
        health: 200,
        defense: 100,
        speed: 70,
        magic: 40,
        'colour': Fore.LIGHTYELLOW_EX
    }

    }

    while True:
        print()
        choice = input(f'{Fore.RESET}Enter your choice: ').strip().lower()
        print()

        if choice == '1' or choice == 'vanguard':
            choice = 'vanguard'
            slow_print(f'{Fore.LIGHTCYAN_EX}Vanguard. So you arent afraid of being on the front lines, A trait of a true fighter destined for victory. An excellent choice {name}!')
            break

        elif choice == '2' or choice == 'wraith':
            choice = 'wraith'
            slow_print(f'{Fore.LIGHTMAGENTA_EX}Wraith, a wise decision {name}! I see you like to keep distance in battle.{Fore.RESET}')
            break

        elif choice == '3' or choice == 'phantom':
            choice = 'phantom'
            slow_print(f'{Fore.LIGHTYELLOW_EX}Phantom, a great choice {name}! a sneaky aggressor I see eh? {Fore.RESET}')
            break

        elif choice == 'radiant' or choice == 'the radiant':
            slow_print('ACCESS OVERRIDE ACCEPTED... Classified class unlocked: Radiant')
            break

        else:
            print()
            slow_print('That class doesnt exist, try again.')
            print()
            continue



    player_stats = class_stats[choice]
    colour = player_stats['colour']

    print()
    slow_text(f'{Fore.LIGHTCYAN_EX}--- PLAYER CLASS ---')

    slow_text(f'{Fore.LIGHTYELLOW_EX}Class: {colour}{choice.capitalize()}{Fore.RESET}')
    time.sleep(0.2)

    for stat, value in player_stats.items():
        if stat == 'colour':
            continue
        slow_text(f'{stat.capitalize()}: {value}')
        time.sleep(0.2)

    print()
    print()
    slow_print(f'{Fore.LIGHTCYAN_EX}---------------------{Fore.RESET}')

    print()
    print()

    return choice, player_stats

class_selection()

#Training Arc

def training():

    time.sleep(0.5)

    slow_print(f'{Fore.LIGHTCYAN_EX}Now that you have chosen your class,')

    slow_print(f'Listen closely {name}...')

    slow_print(f'You are the only one capable {name} to be able to reclaim the light taken from us,')

    slow_print('but beware... this will not be an easy journey,')

    slow_print('You will need serious training...')

    slow_print(f'Follow me {name} to the training grounds...', delay=1.5)

    print()
    slow_print(f'{Fore.LIGHTBLUE_EX}~ Gusts of wind howl as you step into the courtyard... ~')

    slow_print('An ancient warrior awaits you... ')

    slow_print('His name... Eldric,')

    slow_print(f'Eldric The First {Fore.LIGHTYELLOW_EX}Radiant')

    slow_print(f'{Fore.LIGHTBLUE_EX}A man that once defied and banished the Shadow King centuries ago...')

training()
