print("Enter the sentence to change into the pig latin:")
message = input()
VOWELS = ('a', 'e', 'i', 'o', 'u')
pigLatin = []
for word in message.split():
    prefixNonLetters=''
    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetters += word[0]
        word = word[1:]
    if len(word) == 0:
        pigLatin.append(prefixNonLetters)
        continue
    suffixnonLetters = ''
    while not word[-1].isalpha():
        suffixnoLetters += word[-1]
        word = word[:-1]
    # Remember if the word was in uppercase or title case.
    wasUpper = word.isupper()
    wasTitle = word.istitle()
    word = word.lower()  # Make the word lowercase for translation.
# Separate the consonants at the start of this word:
    prefixConsonants = ''
    while len(word) > 0 and not word[0] in VOWELS:
        prefixConsonants += word[0]
        word = word[1:]
# Add the Pig Latin ending to the word:
    if prefixConsonants != '':
        word += prefixConsonants + 'ay'
    else:
         word += 'yay'
# Set the word back to uppercase or title case:
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()
# Add the non-letters back to the start or end of the word.
    pigLatin.append(prefixNonLetters + word + suffixNonLetters)
# Join all the words back together into a single string:
print(' '.join(pigLatin))