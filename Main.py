import time
from Scripts.func import slow_text

slow_text('Loading...')
time.sleep(0.3)
print()
slow_text('25%...')
time.sleep(0.2)
print()
slow_text('50%...')
time.sleep(0.1)
print()
slow_text('75%...')
time.sleep(0.05)
print()
slow_text('100%...')
print()
time.sleep(0.01)
print()
slow_text('Welcome player to the...')
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
print()
time.sleep(0.5)
print()
name = input('Please enter your name: ')
print()
time.sleep(1)
name = name.strip()
slow_text(f'{name} eh, a fine name for a warrior... We need you!')
time.sleep(1)
print()
print()
print()

print()
slow_text(f'Before we begin {name} choose your class!')
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
user_input = input('Enter your choice: ')
print()
print()
print()

if user_input == '1':
    slow_text(f'Vanguard, I see you are a brave warrior. An excellent choice {name}!')

    time.sleep(1)

elif user_input == '2':
    slow_text(f'Wraith, a wise decision {name}! I see you like to keep distance in battle. ')

    time.sleep(1)

elif user_input == '3':
    slow_text(f'Phantom, a great choice {name}! a sneaky aggressor I see eh?')

    time.sleep(1)
else:
    slow_text('Invalid input, please try again.')

print()
print()

#Introduction to the story line:

time.sleep(1)

slow_text(f'Now that you have chosen your class')
print()
time.sleep(1)

print()
slow_text(f'Listen closely {name}...')
print()

time.sleep(1)

print()
slow_text('our land has fallen into the darkness,')
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
slow_text('but beware... this is not an easy journey.')
print()
time.sleep(1)
