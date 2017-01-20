vowels = 'aeiouAEIOU'
consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'


gan = input("Enter a string: ")


gan = gan.casefold()


vowelcount = {}.fromkeys(vowels,0)
consonantcount = {}.fromkeys(consonants,0)

for char in gan:
    if char in vowelcount:
        vowelcount[char] += 1
    elif char in consonantcount:
        consonantcount[char] +=1 
        

print('length of string :', len(str(gan)) , "\n") 
print(vowelcount , "\n")
print(consonantcount, "\n")
