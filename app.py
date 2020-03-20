import random


def pass_generator(pass_len=6, use_uppercase=False, use_special=False, use_numbers=False):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if use_uppercase:
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if use_special:
        characters.extend(list('!@#$%^&*()+=-?><'))
    if use_numbers:
        characters.extend(list('0123456789'))

    res_pass = ''
    for _ in range(pass_len):
        res_pass += random.choice(characters)

    return res_pass


print("\n########## Password generator ##########")
print("To generate better password you can choose more options below:\n")
while True:
    pass_lenght = int(input("How long should be your password: "))
    if pass_lenght < 12:
        print("\nPlease specify a password longer than 12")
        continue
    else:
        break
uppercase_usage = input("\nUse uppercase? y/n (default: n): ")
if uppercase_usage == 'y':
    uppercase_usage = True
else:
    uppercase_usage = False


special_usage = input("\nUse special characters? y/n (default: n): ")
if special_usage == 'y':
    special_usage = True
else:
    special_usage = False

numbers_usage = input("\nUse numbers? y/n (default: n)")
if numbers_usage == 'y':
    numbers_usage = True
else:
    numbers_usage = False


new_password = pass_generator(
    pass_len=int(pass_lenght), use_uppercase=uppercase_usage, use_special=special_usage, use_numbers=numbers_usage)
print(f'\nGenerated password is: \n{new_password}\n')
