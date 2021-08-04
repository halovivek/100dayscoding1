while True:
    print('Enter your age')
    age = input()
    if age.isdecimal():
        break
    print('Enter enter a number for your age')

while True:
    print('select a password (letter and numbers only  ):')
    password = input()
    if password.isalnum():
        break
    print('password can be numbers and letters only')

