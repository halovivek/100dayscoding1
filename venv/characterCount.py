message = 'This is the largest thing which is done for The good for the people and the thing which is done for sure'
count ={}
for characters in message:
    count.setdefault(characters, 0)
    count[characters] = count[characters]  + 1
print(count)
