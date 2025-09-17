import time
from dir.func import slow_text

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
slow_text('Welcome player to the Echoes of The Forgotten!')
print()

print()
input('Press ENTER to continue...')
print()
time.sleep(0.5)
slow_text('Enter your name: ')
name = input()
print()
time.sleep(1)
name = name.strip()
print(name, 'eh, a fine name for a warrior we need you!')
time.sleep(1)
print()


slow_text(f'Before we begin {name} choose your path!')
print()
time.sleep(1)
print()
slow_text('1. Vanguard - Front line attacker, Deals medium-high damage, Medium defense')
time.sleep(1)
print()
slow_text('2. Wraith - Magic user, Ranged attack, low-medium damage, low defense')
time.sleep(1)
print()
slow_text('3. Phantom - Speedy attacker, Stealthy, Medium damage, Medium-low defense')
print()

user_input = input('Enter your choice: ')
print()

if user_input == '1':
    slow_text('Good choice! Vanguard is a strong option!')

elif user_input == '2':
    print()
