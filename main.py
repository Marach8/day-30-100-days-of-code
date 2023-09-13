import time
print('\033[4m30 Days Down\033[0m')
print()
for i in range (1, 31):
  print()
  print(f'\033[4mDay {i}:\033[0m')
  time.sleep(2)
  print()
  ask = input(f'\033[32mWhat do you think about Day {i}: \033[0m')
  time.sleep(1)
  print()
  a = f'You thought that Day {i} was {ask}'
  print(f'\033[1;33m     {a: ^10} \033[0m')
  print('\033[31m---------------------------------------------\033[0m')
  time.sleep(3)