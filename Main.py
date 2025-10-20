import time
import random
import sys

from func import slow_text, slow_print
from colorama import Fore
from colorama import init

init()


# Character Dialogue Functions

def narrator(text, delay=0.05):  # A typewriter effect that also prints out 'narrator: ' then the text
    print(Fore.LIGHTWHITE_EX, end='')
    slow_text(f'Narrator: {text}', delay)
    time.sleep(delay)
    print(Fore.RESET)
    print()


def eldric(text, delay=0.05):  # A typewriter effect that also prints out 'eldric: ' then the text
    print(Fore.LIGHTYELLOW_EX, end='')
    slow_text(f'Eldric: {text}', delay)
    time.sleep(delay)
    print(Fore.RESET)
    print()


def player(text, delay=0.05):  # A typewriter effect that also prints out 'player: ' then the text
    print(Fore.LIGHTCYAN_EX, end='')
    slow_text(f'Player: {text}', delay)
    time.sleep(delay)
    print(Fore.RESET)
    print()


# - Intro Loading Screen -
def loading_screen():
    print()
    slow_print('Loading...', delay=0.5)

    slow_print('25%...', delay=0.4)

    slow_print('50%...', delay=0.3)

    slow_print('75%...', delay=0.2)

    slow_print('100%...', delay=0)

    slow_print('Initializing...', )

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

A land that was once filled with tranquility and peace.

Where communities gathered, where villages thrived in celebration.

Below the endless skies and shimmering stars, 

A land once that was once joyous, turned to''')
    print()

    print()
    slow_print(f'{Fore.LIGHTRED_EX}ruin.')

    slow_print('We have been defeated...')

    slow_print('our armies shattered,')

    slow_print('our cities burned.')

    slow_print('The Shadow King, his guard and their forces hunting us down like heartless creatures.')

    slow_print('Families torn apart... each day we fall further into despair.')

    slow_print('Our lives now lie in ruins, and we will soon become nothing but forgotten echoes in the dark.')

    slow_print('But there is', delay=0.2)

    slow_print(f'{Fore.LIGHTMAGENTA_EX}hope...')

    slow_print('one soul that could change ', delay=0.2)

    slow_print('everything.')

    slow_print(Fore.LIGHTMAGENTA_EX + 'Some could say he is labelled the class,')

    slow_print(f'{Fore.LIGHTYELLOW_EX}Radiant.')

    slow_print(f'{Fore.LIGHTMAGENTA_EX}Someone with the willpower and heart to defy the Shadow King himself.')

    slow_print('You are the only one left amongst the rubble')

    slow_print('The only one that can fight...')

    time.sleep(1)


introduction()


def ask_for_help():
    while True:
        ask_help = input(

            f"Will you help us...{Fore.LIGHTYELLOW_EX} warrior?{Fore.RESET} (yes/no): "
        ).strip().lower()

        print(Fore.BLUE)
        if ask_help == 'yes' or ask_help == 'y':
            print()
            slow_print('Thank you so much for helping us warrior')

            slow_print('we now have a glimpse of hope!')
            print()
            break

        elif ask_help == 'no' or ask_help == 'n':
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

ask_for_help()

name = ''


def input_name():
    while True:
        name = input('Please enter your name: ')
        if not name.isalnum():  # This makes sure if the user enters special characters or any empty spaces then it would say the name is invalid and to try again
            slow_print('\nInvalid input, no special characters or spaces. Try again.')
            continue
        else:
            slow_print(f'\n{name} Eh? a fine name for a {Fore.LIGHTYELLOW_EX}Radiant{Fore.LIGHTBLUE_EX} I mean warrior')
            return name


name = input_name()


# Class Selection

def class_selection():
    print()
    narrator(f'Before we begin training {name}, choose your class!')

    slow_print(
        f'{Fore.RESET}1. {Fore.LIGHTCYAN_EX}Vanguard - Front line attacker, Deals medium-high damage, Medium defense')

    slow_print(
        f'{Fore.RESET}2. {Fore.LIGHTMAGENTA_EX}Wraith - Magic user, Ranged attack, low-medium damage, low defense')

    slow_print(
        f'{Fore.RESET}3. {Fore.LIGHTYELLOW_EX}Phantom - Speedy attacker, Stealthy, Medium damage, Medium-low defense',
        delay=2)

    slow_print(f'{Fore.LIGHTRED_EX}...??? eRrOr, Unauthorised class detected, ADMIN ACCESS ONLY!,')

    slow_print(f'ACCESS OVERRIDE: SECRET CLASS{Fore.LIGHTYELLOW_EX} [???????]')

    '\n'
    print()
    slow_print(f'{Fore.RESET}Hint: type "4" or "5" or "warrior"')

    # Dictionary for class selection stats

    class_stats = {
        'vanguard': {
            'Attack': 38,   # Having an uppercase for the stats is very important because i made the uppercase 'Attack' or 'Health'
            'Health': 150,  # display with their assigned colour on the player class and stats part which is lines
            'Defense': 50,
            'Speed': 20,
            'Magic': 0,
            'colour': Fore.LIGHTCYAN_EX
        },
        'wraith': {
            'Attack': 27,
            'Health': 120,
            'Defense': 70,
            'Speed': 30,
            'Magic': 40,
            'colour': Fore.LIGHTMAGENTA_EX
        },
        'phantom': {
            'Attack': 32,
            'Health': 130,
            'Defense': 30,
            'Speed': 50,
            'Magic': 10,
            'colour': Fore.LIGHTYELLOW_EX
        },
        'radiant': {
            'Attack': 52,
            'Health': 200,
            'Defense': 100,
            'Speed': 70,
            'Magic': 40,
            'colour': Fore.LIGHTYELLOW_EX
        }

    }

    while True:
        print()
        choice = input(f'{Fore.RESET}Enter your choice: ').strip().lower()
        print()

        if choice == '1' or choice == 'vanguard':
            choice = 'vanguard'
            slow_print(
                f'{Fore.LIGHTCYAN_EX}So you have chosen the path of Vanguard, you arent afraid of being on the front lines. A trait of a brave fighter. An excellent choice {name}!')
            break

        elif choice == '2' or choice == 'wraith':
            choice = 'wraith'
            slow_print(
                f'{Fore.LIGHTMAGENTA_EX}So you have chosen the path of Wraith, a range based attacker. A wise decision {name}! I see you value intellect over strength.{Fore.RESET}')
            break

        elif choice == '3' or choice == 'phantom':
            choice = 'phantom'
            slow_print(
                f'{Fore.LIGHTYELLOW_EX}So you have chosen the path of Phantom, a great choice {name}! a sneaky aggressor I see eh? {Fore.RESET}')
            break

        elif choice == '4':
            slow_print(f'{Fore.LIGHTWHITE_EX}No mortal dares try to label the forbidden class by a number.')
            slow_print(f'Indeed, it has a {Fore.LIGHTYELLOW_EX}name...')
            continue

        elif choice == '5':
            slow_print(
                f'{Fore.LIGHTWHITE_EX}Do not insult the forbidden class {Fore.LIGHTWHITE_EX}by applying a number to it.')
            slow_print(f'{Fore.LIGHTWHITE_EX}The {Fore.LIGHTYELLOW_EX}title {Fore.LIGHTWHITE_EX}lies in past text...')
            continue


        elif choice == 'warrior' or choice == 'the warrior':
            choice = 'warrior'
            slow_print(f'{Fore.LIGHTYELLOW_EX}You are close to unlocking the forbidden class, look back...  ')
            slow_print('There was once a title greater than warrior - one born of light and radiance.')
            continue

        elif choice == 'radiant' or choice == 'the radiant':
            choice = 'radiant'
            slow_print(f'{Fore.LIGHTWHITE_EX}So, the light of Eldric burns once more... I see.', delay=1.5)
            slow_print(f'{Fore.RESET}ACCESS OVERRIDE ACCEPTED... Classified class unlocked: Radiant')
            break

        else:
            print()
            slow_print('That class doesnt exist, try again.')
            print()
            continue

    player_stats_colour = class_stats[choice]
    colour = player_stats_colour['colour']

    player_stats = {}
    for key, value in player_stats_colour.items():
        if key != 'colour':
            player_stats[key.lower()] = value

    # This displays the player's class along with their stats

    print()
    slow_text(f'{Fore.LIGHTCYAN_EX}--- PLAYER CLASS ---')

    slow_text(f'{Fore.LIGHTYELLOW_EX}\nClass: {colour}{choice.capitalize()}{Fore.RESET}')
    time.sleep(0.2)

    for stat, value in player_stats_colour.items():
        if stat == 'colour':
            continue

        colour_prefix = ''
        if stat == 'Attack':
            colour_prefix = Fore.LIGHTRED_EX
        elif stat == 'Health':
            colour_prefix = Fore.LIGHTGREEN_EX
        elif stat == 'Defense':
            colour_prefix = Fore.LIGHTBLUE_EX
        elif stat == 'Speed':
            colour_prefix = Fore.LIGHTYELLOW_EX
        elif stat == 'Magic':
            colour_prefix = Fore.LIGHTMAGENTA_EX

        slow_text(f'\n{colour_prefix}{stat.capitalize()}: {value}{Fore.RESET}')
        time.sleep(0.2)

    print()
    slow_print(f'{Fore.LIGHTCYAN_EX}---------------------{Fore.RESET}')

    print()
    print()

    return choice, player_stats_colour, player_stats


# Introduction to training

def training(choice, class_stats):
    time.sleep(0.5)

    slow_print(f'{Fore.LIGHTCYAN_EX}Now that you have chosen your class,')

    narrator(f'Listen closely {name}...')

    narrator(f'You are the only one capable {name} to be able to reclaim the light taken from us,')

    narrator('but beware... this will not be an easy journey,')

    narrator('You will need serious training...')

    narrator(f'Follow me {name} to the training grounds, I have someone I want you to meet..', )

    print()
    narrator(f'{Fore.LIGHTBLUE_EX}~ Gusts of wind howl as you step into the courtyard... ~')

    narrator('An ancient warrior awaits you... ')

    narrator('His name, Eldric...')

    print(f'''{Fore.LIGHTBLUE_EX}                                                                                                                                                                                                        
                     ▒▒                                                                                 
                    ▒▒░▒                                                                                
                    ▒▒░▒▓                                                                               
                   ▒▒░░▒▒                            ▓▓▓▓▒▓▓▓█                                          
                   ▒▒▒░░▒█                        ▓▒▒▒▒▒▒▒▒▒▒▓▓▓                                        
                   ▒▒░░░▒▓                       ▓▒░▒▒▒▒▒▒▒▓▒▒▒▓▒▓                                      
                   ▒▒░░░▒▓ █                    ▓▒▓▒▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓                                     
                   ▒▒░░░▒▒▓▓                    ▓▓░░░▒▒▒▒▒▒▓▓▓▒▓▓▓▓▓█         ██▒▓▓▓                    
                ██ ▒▒░░░▒▓▓█                    ▓▓▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓██     █▓█   █                      
               ▓█▓▓▒▒▒▒▒▒▓▓██                  ▓▓▓▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓█▓█▓▓▓█▓▓██                           
                 █▒░▒▒▒▒▒ ▓▓█                 ██▓▓▓▓█▓▒▓█▒▓▓▒▓▓▓█▓█▓▓▓▓▓▓                               
                 █▓▓▒▒▒▓▓▓▓██                 ██▓▓▒▒▒▒▒▓▒▒▒▒▓█▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓█         ██            
                ██ ██▓█▓▓██                   ▓▓▓▒█▒▓▒▒▓▓▒▒█▓▓▒▓█▓▓▓▓▓▓▓▓▓▓▓  ██▓▓█                     
                  ████▓███ ▓██               █▓▒▓▒▒▓░▒▓▒▒▒▓▓▓▒▒▒▓█▓▓▓▓█▓▓▓▓▒▓▓    ▓▓▒▓                  
                   █▓▓████▓██                ▓█▓▒▒▒▒█▓▓▓▓▓▒▓▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ █▓▓▓                 
                  █▓███████                  ▓█▓▓▒▒▓▓▒░▒▓▓▓▓▓▒▓▓▓▓▓▓▓█▓████▓▒▓▓▓▒▓▓▓ █   ▓█             
                   ███████                 ▓▓▓▓▓▒▒▓▒▒░░░▒▒▒▓▓▓▒▓▓▓▓▓▓▓█▓▓▓▓▓▓▓██▓▓▒▒▓▓████▓▓            
                     ████▓█              █▒▓▓▓▓█▒▒▒▒▒░░░▒▒▒▓▓▒▒▓▓▓█▓▓█▓▓▒▒██▓▓█▓▓▓▓▓▓▓▓████▓▓▓▓▓        
                     ███▓█▓█            ▓▓▓▓▓▓█▓▒▒▒░▒▒░▒▒▒▒▓▒▒▓▓▓██▓█▓▓▓█▓▒▒▓▓▓▓██▓▓▓▓▓▓▓▓    █▓█       
                     █████            █▓▓▓▓▓▓██▓▒▒▒▒░▒▒▒▒▒▒▓▒▓▓▓▓█▓▓█▓██▓▓▒▒▒▓▓▓▓▓██▓▓▓▓▓▓▓▓▓█ █        
                     ███▓█           ▓▒▓▓▓█▓▓█▓█▒▓▒▒▒▒▒▒▒▒▒▓▒▓▓▒▓▓▓▓██▓▓▓▓▓▓▒▓▒▒▒▓▓████▓█▓▓▓▓▓▓▓▓▓▓█    
                     █▓▓▓▓█           ▓▓▓▓▓▓██▓▓▒▒▒▒░▒▒▒▓▒▒▓▓▓▓▓██▒██▓▓▓▓▓▓▓▒▓███▓▓██▓▓▓▓▓▓███  █ █▓▓▓  
                      ▓█▓▓            ██▓██▓█▓▓▓▓▒▒▒▒▒▒▓▒▒▓▓▓▓▓██▓▓███▓▓▓▓▓██▓▓▒▓▓▓▓▓█▓▓▓▓▓▒▓▓▓█        
                      █▓▓▓▓          █▒▓▓██▓██▓██▓▓▒▒▒▓▒▒▒▓▓█▓▓██▓▓████████▓▓▓▓███▓▓▓█▓▓▓▓▓▓▓▓▒▒▒▓█     
                      ████           █▓███▓▓██▓██▓▓▓▒▓▓▒▓▓▓█▓▓▓█▓▓████████████▓▓▒▒▒▓▓▓▓▓▓█▓▓▓▓████▓█    
                      ████          █▓▓▓██▓▓██▓█▓██▓▓▓▒▓▓▓██▓▓███▓██▓████████▓▓▓▓▒▓███████▓▓▓▓▓         
                      ███▓█         █▒▓▓██▓▒▓▓▓█▓▓██▓▓▓▓████▓███▓▒▓████████▓█▓▓██▓▓▓▓▓▓█▓▓▓▓ █▓▓        
                      █████         █▓▓███▓▓█▓██████▓▓███▓▓█▓██▓▓▓▓█████████▓▓█▓▓▓▒▒▓█████▓▓ ██         
                     █▓▓▓█▓▓▒█      █▓▓██▓▓▓█▓▒▓█▒▒▓▓▓██▓▓▓▒▒██████▓█████████▓█████████████▓            
                    ▓▒▒▓▓▓▒▓▓▓  █▓▓█▓▓███▓▓▓██▓█████▓███████████████████████████████████████            
                   █▓▒▒▒▓▓██▓▓▓▓▒▒▓▓▓▓█▓████▓▒▓█████▓▒██████▓█▓█████████████████▓████████████           
                   █▓▓▓▓▓▓▓████▓▓▓▓▓█▓█████▒▓▒▓▓██▒▒▒░▒▒▒▓▒▒░▒▒▓▒░▓▒▓▒▓▓░▓█ █▒▒▓░▒▓▓██▓▓▓▓███           
                    ▓▒▒▒▓▓▓█▓████▓▓▓█▓████▓▓▓▒▓███▓▒░▒█▒▒▓▒▓▒▓▒▒▒▒▓▓█▓▒▓░▓ ▓░░▓▓░▒▓███▓█▓▓▓▓██          
                    █▓▒▒▓▓▓█▓██████████████▓██▓███████████████████████████    ████████████████          
                     █████████████████████▓███▓███▓▓▓▓▓█▓▓▓▓█▓▓▒██▓█▓▓▓██      ██████████████▓          
                        ████████████████████▓▓▓▓▓▓▓▓▓█▓████████████████▓▓      ███████▓█████▓█          
                        █▓██     ███████ █▓▓▓▓▓▓▓▓▓██████████████████████       ██████████████          
                        █▓██             █▓▓▓▓▒▓▓▓▓▓▓▓▓██▓▓▓▓██████████▓██      ███████▓▒▓▓▓▒▒▓▓▓       
                        █▓▓█             ▓███▓▓▓▓▓█▓▓▓▓██▓▓▓▓████████████       ███▓▒░░░░▒▒▓▓▓██        
                        █▓▓█         █▓▓█▓▓▓▓██▓▓▓▓▓█▓██████████████████▓█      ▓▒░▒▒░░░▒▓▓█            
                        ██▓█        ████▓███▓▓█████████▓███▓▓▓▓▓▓▓█████████    █▒▒░▒▒▒▒▒▒▒▒▓            
                        ██▓█      ███▓█▓▓▓███▓▓▓███▓▓▓▓███████████▓▓█████▓▓█   █▒▒░▒░▒▒▒▒░▒▓█           
                        ██▓▓    ██████▓▓████▓███████████▓██████▓██▓▓█▓█▓▓█▓▓   █▒▒░▒▒▒░▒▒▓▒▒▒▓          
                        ██▓▓     ██▓█▓▓██▓▓█▓▓▓▓▓▓▓▓▓█▓▓▓███▓███▓█▓▓▓▓▓▓███▓▓█ ▓▒▓▓▒▒▓▓▒▒▓▓▒▒▓          
                        ██▓█▓    ▓▓██▓██▓▒▓█▓▓▒▓▓▓▓▓▓▓▓▓▓███▓█▓██▓▓▓▓▓▓▓▓██▓▓▓▒▒▓▓▓▓▒▒▓▒▒▓▓▒▒▓█         
                        ██▓██   █▓███▓▓▓▒▓██▓▓▓▓▓▓▓▓▓▓▓█████▓▓█▓██▓█▓▓▓▓█▓██▒▓▓█ █▓▒▒▓█▒▒▓▓▓▒▒▓         
                        ██▓▓█   ████▓▓▓▒▓██▓▓▓▓▓▓▓▓▓███▓▓█▓██▒▒▓▓████▓▓▓▓████▓▓██▓▒▒▓█▓▒▒▓██▓▓█         
                        ██▓▓█    ██▓▓▓▒████▓▓▓▓▓▓███▓▓█▓▓█████▓▒▓▓█▓▓█████████▓▓█▓▓█  ▓▓▓█   ██         
                        ███▓█    █▓▓▒▓█████▓▒▓▓▓▓▓▓▓▓▓▓▓█▓█████▓▒▓▓█▓▓▓██████████                       
                         ██▓█    █▓▒▓██████▓█▒▓▓▓▓▓▓▓▓▓██▓▓█████▓▓▒▓██▓▓▓██▓███▒█                       
                         ███▓   █▓▒████▓▓██▓██▓▓▓▓▓▓███▓▓▓████████▓▓▒▓█▓▓▓▓██▓█▓▒█                      
                         ████  █▓▓█████▓███▓▓▓▓█████▓▓▓▓▓▓▓█████████▓▓▓▓█▓▓▓██▓▓▓▓█                     
                         ████ █▓▓█████▓▓███▓▓▓▓▓██▓▓▓▓▓▓█▓██████▓█████▓▓▓▓█▓▓▓██▓▒▓█ ''')

    print()
    narrator(f'Eldric The First {Fore.LIGHTYELLOW_EX}Radiant')

    narrator(f'A man that once defied and banished the Shadow King himself centuries ago...')

    if choice == 'radiant':
        eldric('So you are the one...')
        eldric('My successor')
        eldric('The next radiant')
        eldric('I have been awaiting your return, for many years...')

        player('My return? What do you mean, How could you have known about me?')

        eldric('Our souls are bound by light itself.')
        eldric('As soon as you awakened your radiance,')
        eldric('I felt the surge of power, it called to me.')

        eldric(f'You and I are connected {name},')
        eldric('We are bound by the same flame that once banished the Shadow King himself.')

        player('So, I was chosen...?')

        eldric('You were not chosen, rather awakened.')
        eldric('the light found you now because Asgiaburn needs you, just as the world once needed me...')

        eldric('Now, enough talk, lets see if the radiant within you can handle a fragment of what lies ahead.')
        eldric('Prepare yourself, Radiant. For your first trial will now begin!')

    else:
        eldric(f'A {choice.capitalize()}? Hm not many of your kind reach this place.')
        eldric('I see the resolve in your eyes, one that will never give up no matter the challenge.')
        eldric('I once trained warriors like you - fierce and loyal')
        eldric('Even without the radiant’s gift, you are able to rival them')

        eldric('Now, enough talk let us begin your training.')


choice, player_stats_colour, player_stats = class_selection()
colour = player_stats_colour['colour']
training(choice, player_stats_colour)


# Practice battle training, basic mechanics like attack / defend


def practice_dummy(player_class, player_stats):
    print('\n\n')
    narrator('Get ready to test your skills, we are starting your training.')

    dummy_health = 100
    defend_counter = 0  # This keeps track of how many times the player chose to defend

    narrator(f'Go on {name} let us see if we can put Asgiaburn`s future in your hands.\n')

    first_round = True

    while dummy_health > 0:
        if first_round:
            action = input(
                f'A wooden dummy appears before you... What do you do, {colour}{player_class.capitalize()}? {Fore.RESET}ATTACK or DEFEND? ').strip().lower()
            first_round = False
        else:
            action = input('\nNow, will you ATTACK or DEFEND? ').strip().lower()

        print()

        if action == 'attack':
            damage = player_stats['attack']
            dummy_health -= damage
            if dummy_health < 0:
                dummy_health = 0

            narrator(f'You strike the dummy with all your strength dealing {Fore.LIGHTRED_EX}{damage} damage!')
            narrator(f'The dummy has now got {Fore.LIGHTGREEN_EX}{dummy_health} health remaining!{Fore.RESET}')

            if dummy_health <= 0:
                print()
                narrator('The dummy has been obliterated!')
                eldric(f'Well done, just as I would have expected from a {colour}{player_class.capitalize()}.')
                eldric('You now know the basics of battle.')
                break


        elif action == 'defend':
            defend_counter += 1
            defense = player_stats['defense']

            if defend_counter == 1:
                narrator(f'You use the defensive shield that saves you {defense} health')
                narrator('After waiting and expecting an attack, nothing strikes.')

            elif defend_counter == 2:
                eldric('The dummy is unable to attack,', delay=0.02)
                eldric(f'Attack {name}! a {player_class.capitalize()} never quivers, now strike!')

            else:
                narrator('You hesitate, Eldric shakes his head.')
                eldric('Fear is your only enemy, try again.')



        else:
            slow_print('Invalid action, please try ATTACK or DEFEND.\n')
            continue

        while True:
            defend_to_attack = input('\nWill you ATTACK or DEFEND? ').strip().lower()

            if defend_to_attack == 'attack':
                damage = player_stats['attack']
                dummy_health -= damage
                if dummy_health < 0:
                    dummy_health = 0

                print()
                narrator(f'You swing, with all your might for {Fore.LIGHTRED_EX}{damage} damage!')
                narrator(f'The dummy has{Fore.LIGHTGREEN_EX} {dummy_health} health remaining!{Fore.RESET}')
                break

            elif defend_to_attack == 'defend':
                defend_counter += 1
                defense = player_stats['defense']
                print()

                if defend_counter == 1:
                    narrator(f'You use the defensive shield that saves you {defense} health')
                    narrator('After waiting and expecting an attack, nothing strikes.')

                elif defend_counter == 2:
                    eldric('The dummy is unable to attack,', delay=0.02)
                    eldric(f'Attack {name}! a {player_class.capitalize()} never quivers, now strike!')

                else:
                    narrator('You hesitate, Eldric shakes his head.')
                    eldric('Fear is your only enemy, try again.')

                continue

            else:
                slow_print('Invalid action, please try ATTACK or DEFEND.\n')

        if dummy_health <= 0:
            narrator('The dummy has collapsed into fragments!')
            print()
            eldric(f'Well done, just as I would have expected from a {colour}{player_class.capitalize()}.')
            eldric('You now know the basics of battle and learned that hesitation does not bring anything to battle.\n')
            break


practice_dummy(choice, player_stats)
'\n'

eldric('Even without a weapon, you`ve proven your resolve.')
eldric('Not many can stand unarmed against such challenges and still press forward.')
eldric('Now that you have flawlessly passed,')
eldric('It is time I pass onto you the legacy of light itself...')
narrator(f'Eldric draws out a shimmering blade from the air - {Fore.LIGHTYELLOW_EX}The Radiance Blade.{Fore.RESET}')
eldric(f'Wield it well, {name}. It will guide your strikes and surely increase your battle capabilities.')


def radiance_blade_abilities(player_class, player_stats):

    narrator('The Radiance Blade converges with energy, it merges with your soul.')

# Code below multiplies the players stats because of the radiance blade

    multipliers = {
        'vanguard': {'attack': 2.3, 'defense': 1.5, 'speed': 2, 'health': 2}, # check how the stats look in battle and see if there is good balance
        'wraith': {'attack': 2.5, 'defense': 1.3, 'speed': 1.5, 'health': 2},
        'phantom': {'attack': 2.1, 'defense': 1.2, 'speed': 1.8, 'health': 2},
        'radiant': {'attack': 2.1, 'defense': 1.5, 'speed': 1.5, 'health': 2},
    }

    for stat in ['attack', 'defense', 'speed', 'health']:
        player_stats[stat] = int(player_stats[stat] * multipliers[player_class][stat])

    narrator('Your stats amp up with the power of the Radiance Blade!')
    narrator(
        f"Attack: {player_stats['attack']}, Defense: {player_stats['defense']}, Speed: {player_stats['speed']}, Health: {player_stats['health']}")

    return player_stats

player_stats = radiance_blade_abilities(choice, player_stats)

def start_journey():
    print('\n\n')
    time.sleep(1)

    narrator('You grip the Radiance Blade tightly. You can feel the power flowing through it.')
    eldric('Its time...')
    eldric(f'{name}, the Shadow Realm awaits you.')
    eldric('You must face the Shadow King there and bring back the light to Asgiaburn.')

    player('Im ready to end this.')

    eldric('Good. Remember what I taught you. Attack smart, dont hesitate and defend when needed to.')

    eldric('The light will guide your path.')

    print()
    narrator(f'{Fore.LIGHTBLUE_EX}~ You walk through the destroyed lands... ~')
    narrator('You see the remains of villages that were once full of life.')
    narrator('The sky gets darker as you get closer to the Shadow Realm.')
    narrator('You see a huge dark fortress ahead.')

    print()
    slow_print(f'{Fore.LIGHTRED_EX}A dark figure appears from the shadows...')
    time.sleep(1)


# The Shadow Guard appears
def show_shadow_guard():
    print(f'''{Fore.LIGHTRED_EX}
    ███████╗██╗  ██╗ █████╗ ██████╗  ██████╗ ██╗    ██╗
    ██╔════╝██║  ██║██╔══██╗██╔══██╗██╔═══██╗██║    ██║
    ███████╗███████║███████║██║  ██║██║   ██║██║ █╗ ██║
    ╚════██║██╔══██║██╔══██║██║  ██║██║   ██║██║███╗██║
    ███████║██║  ██║██║  ██║██████╔╝╚██████╔╝╚███╔███╔╝
    ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚══╝╚══╝ 

         ██████╗ ██╗   ██╗ █████╗ ██████╗ ██████╗          
        ██╔════╝ ██║   ██║██╔══██╗██╔══██╗██╔══██╗         
        ██║  ███╗██║   ██║███████║██████╔╝██║  ██║         
        ██║   ██║██║   ██║██╔══██║██╔══██╗██║  ██║         
        ╚██████╔╝╚██████╔╝██║  ██║██║  ██║██████╔╝         
         ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝          
    {Fore.RESET}''')

    print()
    slow_print(f'{Fore.LIGHTRED_EX}Shadow Guard: Another one who wants to die...')

    slow_print(f'Shadow Guard: The King doesnt have interest in weak people.')

    slow_print(f'Shadow Guard: If you want to get to him, you first you have to beat ME, {name}!')

    print()
    narrator('The Shadow Guard pulls out a dark sword.')

    player('Move or fight me!')

    slow_print(f'{Fore.LIGHTRED_EX}Shadow Guard: Lets see if your light is strong enough!\n')


# The main battle function
def battle_system(player_class, player_stats, enemy_name, enemy_health, enemy_damage, enemy_defense):
    # Gets the players stats from the dictionary
    player_health = player_stats['health']
    player_damage = player_stats['attack']
    player_defense = player_stats['defense']
    player_speed = player_stats['speed']

    narrator(f'The battle starts! {enemy_name} is ready to fight!')
    print()

    round_number = 1
    defending = False # This checks if the player is defending or not

    # Keep fighting until someone loses
    while player_health > 0 and enemy_health > 0:
        print(f'{Fore.LIGHTCYAN_EX}--- ROUND {round_number} ---{Fore.RESET}')
        print(f'{Fore.LIGHTGREEN_EX}Your Health: {player_health}{Fore.RESET}')
        print(f'{Fore.LIGHTRED_EX}{enemy_name} Health: {enemy_health}{Fore.RESET}\n')

        # Asks the player what they want to do
        valid_input = False
        while valid_input == False:
            try:
                player_action = input(f'What will you do? [ATTACK / DEFEND / SPECIAL]: ').strip().lower()
                # Checks what action they picked
                if player_action == 'attack':
                    valid_input = True
                    defending = False

                    # Do damage to enemy
                    hit_damage = player_damage
                    enemy_health = enemy_health - hit_damage

                    # Makes sure the health doesnt go negative
                    if enemy_health < 0:
                        enemy_health = 0

                    narrator(
                        f'You attack with the Radiance Blade for {Fore.LIGHTRED_EX}{hit_damage} damage!{Fore.RESET}')
                    narrator(f'{enemy_name} has {Fore.LIGHTGREEN_EX}{enemy_health} health left!{Fore.RESET}')

                elif player_action == 'defend':
                    valid_input = True
                    defending = True
                    narrator(f'You get ready to block the next attack!')

                elif player_action == 'special':
                    valid_input = True
                    defending = False

                    # Check if speed is high enough for special move
                    if player_speed > 35:
                        # Special does more damage
                        special_attack = int(player_damage * 1.6)
                        enemy_health = enemy_health - special_attack

                        if enemy_health < 0:
                            enemy_health = 0

                        narrator(f'{Fore.LIGHTYELLOW_EX}RADIANT STRIKE!{Fore.RESET}')
                        narrator(
                            f'You do a powerful attack for {Fore.LIGHTRED_EX}{special_attack} damage!{Fore.RESET}')
                    else:
                        narrator('Your speed isnt high enough for special attack!')
                        narrator('You do a normal attack instead.')
                        hit_damage = player_damage
                        enemy_health = enemy_health - hit_damage

                else:
                    # If the player types something wrong
                    print(f'{Fore.LIGHTRED_EX}Thats not a valid choice! Pick ATTACK, DEFEND, or SPECIAL.{Fore.RESET}\n')
                    valid_input = False

            except:
                # If something breaks
                print(f'{Fore.LIGHTRED_EX}Something went wrong. Try again.{Fore.RESET}\n')
                valid_input = False

        print()

        # To check if the enemy is dead
        if enemy_health <= 0:
            narrator(f'{Fore.LIGHTYELLOW_EX}{enemy_name} has been defeated!{Fore.RESET}')
            return player_health

        # Now its the enemys turn to attack
        time.sleep(0.5)
        narrator(f'{enemy_name} is attacking!')

        # Calculate how much damage you take
        if defending == True:
            # Defense blocks half the damage
            block_amount = player_defense // 2
            damage_taken = enemy_damage - block_amount

            # Makes sure the damage isnt negative
            if damage_taken < 0:
                damage_taken = 0

            player_health = player_health - damage_taken
            narrator(f'You block most of the attack! You take {Fore.LIGHTRED_EX}{damage_taken} damage!{Fore.RESET}')
        else:
            # Sometimes enemy does a critical hit
            random_number = random.random()
            if random_number < 0.2:
                # Critical does more damage
                damage_taken = int(enemy_damage * 1.5)
                narrator(f'{Fore.LIGHTRED_EX}CRITICAL HIT!{Fore.RESET}')
            else:
                damage_taken = enemy_damage

            player_health = player_health - damage_taken
            narrator(f'{enemy_name} strikes you! You take {Fore.LIGHTRED_EX}{damage_taken} damage!{Fore.RESET}')

        print()

        # To check if the player died
        if player_health <= 0:
            player_health = 0
            narrator(f'{Fore.LIGHTRED_EX}You have been defeated...{Fore.RESET}')
            narrator('The darkness takes over...')
            narrator('Asgiaburn is lost forever.')
            print()
            slow_print(f'{Fore.LIGHTRED_EX}GAME OVER{Fore.RESET}')
            time.sleep(2)
            sys.exit(0) # If the player loses then this ends the game after 'GAME OVER'

        # Go to next round
        round_number = round_number + 1
        time.sleep(1)

    return player_health


# Fight the shadow guard
def fight_shadow_guard(player_class, player_stats):
    show_shadow_guard()

    # Calculate shadow guard stats based on my stats
    guard_health = int(player_stats['health'] * 1.2)
    guard_attack = int(player_stats['attack'] * 0.8)
    guard_defense = int(player_stats['defense'] * 0.7)

    # Start the battle
    health_left = battle_system(
        player_class,
        player_stats,
        'Shadow Guard',
        guard_health,
        guard_attack,
        guard_defense
    )

    # Updates my health after the battle
    player_stats['health'] = health_left

    # Shows what happens after winning
    print('\n')
    narrator('The Shadow Guard falls down, the darkness fading away.')

    slow_print(f'{Fore.LIGHTRED_EX}Shadow Guard: Impossible... the light... it hurts...')

    slow_print(f'Shadow Guard: The Shadow King... is waiting... in the throne room...')

    narrator('The guard turns into shadows and disappears.')

    print()
    eldric(f'Good job {name}! But that was just the start.')
    eldric('The Shadow King is much stronger.')
    eldric('Take a moment to rest and get ready.')

    # Heal a bit before the final battle
    max_health = int(player_stats['health'] * 2.5)

    heal = max_health - player_stats['health']

    player_stats['health'] = max_health

    # Makes sure the players health doesnt go over the max
    if player_stats['health'] > max_health:
        player_stats['health'] = max_health

    narrator(f'The Radiance Blade glows and heals you for {Fore.LIGHTGREEN_EX}{heal} health!{Fore.RESET}')
    narrator(f'You now have {Fore.LIGHTGREEN_EX}{player_stats["health"]} health{Fore.RESET}')

    print()
    input('Press ENTER to go into the throne room...')


# Fight the shadow king
def fight_shadow_king(player_class, player_stats):
    print('\n\n')
    narrator('You open the massive doors to the throne room.')
    narrator('Darkness fills the room and pushes against your light.')
    narrator('You see the Shadow King on his throne, he stands up.')
    narrator('Slowly walking towards you...')

    print(f'''{Fore.LIGHTRED_EX}                                                                                                    
                                                 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                                       
                                              ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                               
                                            ▓▓▓▓▓▓▓▓▒▒▒▒▒▓▓▓▓▓▓▓▒▓▓▓▓▓▓▓▓▓▓▓▓  ▓                        
                                      ▓▓ ▓▓▓▓▓▓▒▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ▓▓                      
                                     ▓  ▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▓█▓▓▓▒▓▒▓▓▓▓▓▓▓▓▓▓▓▓▓ ▓▓▓                    
                                 ▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓█▒▒▒▒▒▒▒▒▒▒▓█▓▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                   
                                 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓██▓▒▒▒▒▒▒███▓▒▒▒▓▓▒▒▒▓▓▓██▓▓▓▓▓▓▓▓▓▓                   
               █                ▓▓▓▓▓▒▓▓▓▓▓▒▓▓▒▒▒▒▓███▓████▓▒▒▒▒▒▒▓▒▒▒▒▒▒▓████▓▓▓▓▓▓▓                   
               ███             ▓▓▓▓▓▓▓█▓▒▒▒▒▓▓▓▒▒▒▓██▓▓████▓▓██▓▒▓▓█▓▒▒▒▒▓███▓▓▓▓▓▓▓▓▓                  
                ███           ▓▓▓▓▓▒██▓▒▒▒▒▒▓█▓▓▒▓█████▓█████████████▓▓▓▓█████▓▓▓▓▓▓▓▓                  
                ████         ▓▓▓▓▓▒▓███▓▓▓▓███▓▓█████████████████████████████▓▓▓▓▓▓▓▓                   
                █████        ▓▓▓▓▒▒██████████████████████████████▓██████████▓▓▓▓▓▓▓▓▓                   
                █████       ▓▓▓▓▓▒▒▓█████████████████████████▓█████████████▓▒▓▓▓▓▓▓▓▒                   
                ██████      ▓▓▓▓▒▒▒▒▓█████████████████████████▓████████████▓▓▓▓▓▓▓▓▓▓                   
                  ███▓▓    ▒ ▓▓▓▓▓▓██████████████████████████████████████████▓▒▓▓▓▓                     
                 ██████     ▓▓▓▓▒▒▒▓██████████████▓▓▓▓▓███████████████████▓▒▒▒▓▓▓▓▓▒                    
                  ████▓     ▓▓▓▓▓▒▒▓▓███████████▓▓▓▒▓▓▓███████████████████▓▓▓▓▓▓▓▓▒▒                    
                   ████▓      ▓▓▓▒▒▒▒▓██████████▓▓▓▓▓▓▓████████████████████▓▒▒▓▓▓▒▒                     
                    ███▓       ▓▓▒▒▒▓█████████████▓▓▓██████████████████████▓▒▓▓▒▒▒                      
                    ████         ▓▓▓██████████████▓▓▓█████████████████████▓▓▓▓▒▒                        
                    ████▓       ▓███████████████████████████████████████▓████▓                          
                     ████    ▓████████████▓▒▓███████████████████▓▒▓███▓▓██████▓█                        
                     ████  ██████████████▓▒▒▓██████████████████▓▒▒▒▓▓███████████                        
                      █████████████████▓▓▒▒▓████████████████████▓▒▒▓▓███████████                        
                    █████████████████▓▓▓▓▓▓▓█████████████████████▓▒▒▓▓██████████                        
                   ██████████████▓▓▓▓  ▓▓ ▓████████████████████████▓▓▓▓██████████                       
                      ███████         ▓▓ ▓███████████████████████████▓▓▓█████████                       
                        █████       ▓▓  █████████████████████████████▓▓▓▓████████                       
                        █████    ▓   ▓▓███████████████████████████████▓▓▓▓▓███████                      
                        ██████▓        █████████████████████████████████▓▓▓████████                     
                        ███████       ▓████████████████████████████████████████████                     
                          █████       ████████████████████████████████████████████                      
                          ██████     █████████████████████████████████████████████                      
                           █████    ██████████████████████████████████████████████                      
                            ████    █████████████████████████████████████████████                       
                             ████ ████████████████████████████████████████  ██████                      
                             ███▓▓█████████████████████████████████████████  ██████                     
                              ██████████████████████████████████████████████ ██████                     
                           █████████████████████████████████████████████████  █████                     
                        █████████████████████████████████████████████████████ ▓▓████                    
                        ██████████████████████████████████████████████████████ ▓▓███▓                   
           ████   █████████████████████████████████████████████████████████████ ▓▓▓██▓▓▓                
         ████████████████████████████ █████████████████████████████████████████▓▓▓▓▓█▓▓▓▓▓▓▓            
               ███████████████████████████████████████████████████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓          
                    ▓▓▓███████████████████████████████████████████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓         
                           ██████ ███████████████████████████████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓       
                          ▓▓█████  ▓▓███████████████████████████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓       
                            ▓▓▓███▓▓████████████████████████████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      
                             ▓ ▓███▓▓▓██████████████████████████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓       
                                ▓▓▓  ███████████▓█████    █████████████████ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███▓       
                                     █████████▓▓ ▓          ███████████████   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███▓       
                                   ███████████▓                ████████████     ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓       
                              ████████████████▓                  ██████████          ▓▓▓▓▓▓▓▓▓▓▓        
                             █████████████████▓                  ███████████             ▓▓▓▓           
                            █████████████ ████                   ███████████        ▒▓▓▓▓▓▓▓            
                                            ████                  ██████████            ▓▓              
                                                █                ████████████                           
                                                                 █████████████                          
                                                                  ███████████                           
                                                                       ██                                                                                                                         
                                                                                                        ''')

    print()
    slow_print(f'{Fore.LIGHTRED_EX}Shadow King: So... the light comes back eh...')
    slow_print(f'Shadow King: I remember this. Eldric thought he beat me, and now he brings his successor?')
    slow_print(f'Shadow King: How ridiculous HAHAHAHAHA. I will end this in an instant.')

    print()
    player('This will end now! I will bring peace to Asgiaburn by defeating you!')

    slow_print(f'{Fore.LIGHTRED_EX}Shadow King: Come then. Let me put out your light.\n')

    # Shadow king's stats based on the players stats
    king_health = int(player_stats['health'] * 1.3)
    king_attack = int(player_stats['attack'] * 1)
    king_defense = int(player_stats['defense'] * 1.1)

    # Start the final battle
    battle_system(
        player_class,
        player_stats,
        'Shadow King',
        king_health,
        king_attack,
        king_defense
    )

    # YOU WIN show ending
    print('\n\n')
    narrator('The Shadow King falls, turning into dust.')

    slow_print(f'{Fore.LIGHTRED_EX}Shadow King: No... this cant... happen...')

    narrator('The Shadow Kings dark magic starts breaking apart.')

    print()
    narrator(f'Light fills the Shadow Realm, removing all the darkness.{Fore.RESET}')
    narrator('The shadows covering Asgiaburn start to disappear.')
    narrator('You can hear sounds of people celebrating.')

    print()
    narrator(f'The dark fog over the villages goes away.{Fore.RESET}')
    narrator('Families who were hiding come out from the ruins.')
    narrator('The Shadow Kings dark soldiers fall down, free from his control.')
    narrator('Plants start growing again in the dead ground.')
    narrator('The sky becomes clear and you can see the stars.')

    print()
    narrator('People all over Asgiaburn see the light returning.')
    narrator('Everyone hears the news - the Radiant is back.')
    narrator('The Shadow King is gone.')

    print()
    eldric('You really did it...')
    eldric(f'{name}, you broke the curse on our land.')
    eldric('The people who survived can finally come out and rebuild.')
    eldric('The Shadow Kings dark magic that killed the plants and blocked the sun... its all gone.')
    eldric('Asgiaburn can recover now. It will take time, but we have hope again.')

    print()
    narrator('Over the next few days, people return to their homes.')
    narrator('Villages start getting rebuilt.')
    narrator('The Radiance Blade shines bright, showing everyone the light is back.')

    print()
    narrator(f'You, {colour}{player_class.capitalize()}, are now known as the hero of Asgiaburn.')
    narrator('People will tell stories about you forever.')
    narrator('The days of darkness are now over.')
    narrator(f'{Fore.LIGHTYELLOW_EX}The time of light starts now.{Fore.RESET}')
    narrator(f'We truly thank you {name}.')

    print()
    slow_print(f'{Fore.LIGHTYELLOW_EX}THE END{Fore.RESET}')
    print()
    slow_print('Thanks for playing Echoes of the Forgotten!')
    time.sleep(2)


# Starts the final part of the game
start_journey()
fight_shadow_guard(choice, player_stats)
fight_shadow_king(choice, player_stats)
