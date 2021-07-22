while True:
    print("who are you")
    name = input()
    if name != 'Joe':
        continue
    print("hello what is the password?(it is fish ?)")
    password = input()
    if password == "swordfish":
        break
print("access granted")
