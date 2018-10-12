def pigLatin(original):
    pig_latin_suffix = 'ay'
    vowels = list('aeiou')
    new_word = ''
    # original = input('Enter a word: ')

    if len(original) > 0 and original.isalpha():
        word = original.lower()
        first = word[0]
        if first in vowels:
            new_word = word + 'way'
        else:
            start = 0
            for letter in list(word):
                    if letter in vowels:
                        break
                    else:
                        start += 1
            new_word += word[start:] + word[:start] + pig_latin_suffix
        return(new_word)
    else:
       return "empty"

print(pigLatin("andela"))
