import time
from dir.func import slow_text
from colorama import init, Fore

print(Fore.GREEN + 'This is green text')
print(Fore.BLUE + 'This is blue text')
print(Fore.CYAN + 'This is cyan text')
print(Fore.LIGHTBLUE_EX + 'This is light blue text')
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

print("""
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

print()
input('Press ENTER to continue...')

slow_text('We have been defeated... our armies shattered, our cities burned.')
time.sleep(1)
print()

slow_text('The Shadow Kings guards hunting us down like heartless creatures. Families torn apart... hope slowly fading.')
time.sleep(1)
print()

slow_text('Our lives now lie in ruins, and we will soon become nothing but whispers in the dark.')
time.sleep(1)
print()

slow_text('But there is hope... one soul that could change everything, that could stand against the darkness.')
time.sleep(1)
print()

slow_text('A warrior... someone with the willpower and heart to defy the Shadow King himself.')
time.sleep(1)
print()

input('Will you help us... warrior?')
time.sleep(1)

print()
time.sleep(0.5)
print()
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
