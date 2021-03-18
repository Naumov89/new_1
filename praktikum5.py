##################################################### 1

# ser = ['The Walking Death', 'The Sopranos', 'Dexter']

# for show in ser:
#     print(show)

################################################################ 2
# for i in range  (25, 51):
#     print(i)

####################################################################### 3

# ser = ['The Walking Death', 'The Sopranos', 'Dexter']

# for index, value in enumerate(ser):
#     print(f'{index} : {value}')

########################################################################### 4

# numbers = [1, 5, 8, 10, 13, 18, 20]

# print('Enter x to exit!')
# print('Guess the number (0 - 20)!')

# while True:
#     answer = input('Enter : ')    
#     if answer == 'x':
#         break
#     try:
#         answer = int(answer)
#     except ValueError:
#         print('ValueError')
#     if answer in numbers:            
#         print('You guessed it!')
#     else:
#         print('You do not guessed it!')


#####

# numbers = [11, 32, 33, 15, 1]

# while True:
#     answer = input("Guess a number or type q to quit.")
#     if answer == "q":
#         break
#     try:
#         answer = int(answer)
#     except ValueError:
#         print("please type a number or q to quit.")
#     if answer in numbers:
#         print("You guessed correctly!")
#     else:
#         print("You guessed incorrectly!")

################################################################################# 5

list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 88]
result = []

for i in list1:
    for j in list2:
        result.append(i * j)
print(result)

###################################################################################

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie':{
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    }

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = f"{user_info['location']}"
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
